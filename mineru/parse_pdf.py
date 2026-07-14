#!/usr/bin/env python3
"""
MinerU online API PDF parser (MyST / Solid State Physics experiment branch).

Flow for a LOCAL pdf:
  1. POST /api/v4/file-urls/batch        -> get {batch_id, pre-signed PUT url, task_ids}
  2. PUT  <file bytes> to that url        -> upload
  3. GET  /api/v4/extract-results/batch/{batch_id}  -> poll until done
  4. download full_zip_url -> extract markdown
  (NOTE: file-urls/batch already returns batch_id; do NOT call extract/task/batch,
   the uploaded pre-signed PUT url is not a GET-able resource for MinerU.)

Flow for a REMOTE url:
  1. POST /api/v4/extract/task            -> task_id
  2. GET  /api/v4/extract/task/{task_id}  -> poll until done
  3. download full_zip_url -> extract markdown

Token is read from MINERU_TOKEN env var (never hard-coded / committed).
Rate-limit safe: submits ONE file, polls at <=4 req/min, downloads one zip.

Usage:
  # local file
  MINERU_TOKEN=xxx python mineru/parse_pdf.py --pdf path/to/book.pdf --out mineru/output
  # remote url
  MINERU_TOKEN=xxx python mineru/parse_pdf.py --url https://.../book.pdf --out mineru/output
"""
import os
import sys
import json
import time
import zipfile
import argparse
import urllib.request
import urllib.error

BASE = "https://mineru.net"
POLL_SECONDS = 15          # gentle polling, well under 1000/min query limit
PUT_TIMEOUT = 600
API_TIMEOUT = 120


def api(method, path, json_body=None, token=None, extra_headers=None):
    url = BASE + path
    data = json.dumps(json_body).encode("utf-8") if json_body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    if extra_headers:
        for k, v in extra_headers.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as r:
            raw = r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise SystemExit(f"HTTP {e.code} on {method} {path}: {body[:1000]}")
    return json.loads(raw)


def first_match(d, keys):
    """Return first non-null value for any of `keys` nested under dict/list `d`."""
    if isinstance(d, dict):
        for k, v in d.items():
            if k in keys and v:
                return v
            if isinstance(v, (dict, list)):
                r = first_match(v, keys)
                if r:
                    return r
    elif isinstance(d, list):
        for item in d:
            r = first_match(item, keys)
            if r:
                return r
    return None


def upload_local(pdf_path, token, model_version, language, enable_formula, enable_table):
    name = os.path.basename(pdf_path)
    data_id = "local-" + str(int(time.time()))
    print(f"[1/4] request pre-signed url for {name} ...", flush=True)
    resp = api("POST", "/api/v4/file-urls/batch",
               {"files": [{"name": name, "data_id": data_id}], "model_version": model_version},
               token=token)
    print("  file-urls/batch ->", json.dumps(resp, ensure_ascii=False)[:800])
    data = resp.get("data") or {}
    file_urls = data.get("file_urls") or []
    file_url = file_urls[0] if file_urls else first_match(data, {"file_url", "url", "upload_url"})
    batch_id = data.get("batch_id")
    if not file_url:
        raise SystemExit("could not find pre-signed file_url in response")
    if not batch_id:
        raise SystemExit("could not find batch_id in response")
    print(f"[2/4] PUT upload -> {file_url[:80]}...", flush=True)
    with open(pdf_path, "rb") as fh:
        body = fh.read()
    req = urllib.request.Request(file_url, data=body, method="PUT")
    req.add_header("Content-Type", "application/pdf")
    with urllib.request.urlopen(req, timeout=PUT_TIMEOUT) as r:
        print(f"  PUT status {r.status}", flush=True)
    print(f"[3/4] batch {batch_id} ready, poll after upload ...", flush=True)
    return batch_id


def poll_batch(batch_id, token):
    print(f"[4/4] poll batch {batch_id} ...", flush=True)
    while True:
        resp = api("GET", f"/api/v4/extract-results/batch/{batch_id}", token=token)
        results = (resp.get("data") or {}).get("extract_result") or []
        states = [r.get("state") for r in results]
        print(f"  states={states}", flush=True)
        if results and all(s == "done" for s in states):
            return results
        if any(s == "failed" for s in states):
            raise SystemExit(f"task failed: {json.dumps(results, ensure_ascii=False)[:800]}")
        time.sleep(POLL_SECONDS)


def submit_url(url, token, model_version, language, enable_formula, enable_table):
    print(f"[1/3] submit url {url[:80]}...", flush=True)
    resp = api("POST", "/api/v4/extract/task",
               {"url": url, "model_version": model_version, "language": language,
                "enable_formula": enable_formula, "enable_table": enable_table},
               token=token)
    print("  extract/task ->", json.dumps(resp, ensure_ascii=False)[:800])
    task_id = first_match(resp, {"task_id"})
    if not task_id:
        raise SystemExit("could not find task_id in response")
    return task_id


def poll_task(task_id, token):
    print(f"[2/3] poll task {task_id} ...", flush=True)
    while True:
        resp = api("GET", f"/api/v4/extract/task/{task_id}", token=token)
        d = resp.get("data") or {}
        state = d.get("state")
        print(f"  state={state}", flush=True)
        if state == "done":
            return d
        if state == "failed":
            raise SystemExit(f"task failed: {d.get('err_msg')}")
        time.sleep(POLL_SECONDS)


def download_zip(zip_url, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    zip_path = os.path.join(out_dir, "mineru_result.zip")
    print(f"[final] download zip -> {zip_path}", flush=True)
    req = urllib.request.Request(zip_url, method="GET")
    with urllib.request.urlopen(req, timeout=300) as r:
        with open(zip_path, "wb") as fh:
            fh.write(r.read())
    # extract
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(out_dir)
    print(f"  extracted to {out_dir}", flush=True)
    md = [n for n in os.listdir(out_dir) if n.endswith(".md")]
    print(f"  markdown files: {md}", flush=True)
    return zip_path


def main():
    ap = argparse.ArgumentParser(description="MinerU PDF parser")
    ap.add_argument("--pdf", help="local PDF path")
    ap.add_argument("--url", help="remote PDF url")
    ap.add_argument("--out", default="mineru/output", help="output directory")
    ap.add_argument("--model", default="vlm", choices=["pipeline", "vlm", "MinerU-HTML"])
    ap.add_argument("--language", default="en", help="content language (en/ch/...)")
    ap.add_argument("--no-formula", action="store_true")
    ap.add_argument("--no-table", action="store_true")
    args = ap.parse_args()

    token = os.environ.get("MINERU_TOKEN")
    if not token:
        raise SystemExit("MINERU_TOKEN env var required")

    if args.pdf:
        if not os.path.exists(args.pdf):
            raise SystemExit(f"pdf not found: {args.pdf}")
        batch_id = upload_local(args.pdf, token, args.model, args.language,
                                not args.no_formula, not args.no_table)
        results = poll_batch(batch_id, token)
        zip_url = first_match(results, {"full_zip_url", "zip_url"})
        if not zip_url:
            raise SystemExit("no full_zip_url in result")
        download_zip(zip_url, args.out)
    elif args.url:
        task_id = submit_url(args.url, token, args.model, args.language,
                             not args.no_formula, not args.no_table)
        d = poll_task(task_id, token)
        zip_url = first_match(d, {"full_zip_url", "zip_url"})
        if not zip_url:
            raise SystemExit("no full_zip_url in result")
        download_zip(zip_url, args.out)
    else:
        raise SystemExit("provide --pdf or --url")


if __name__ == "__main__":
    main()
