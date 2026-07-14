# MinerU PDF Parsing Experiment (branch `mineru`)

This branch experiments with [MinerU](https://mineru.net) online API to parse the
MIT 6.732 *Solid State Physics* PDF source into Markdown (with LaTeX formulas and
extracted figures), as an alternative to the hand-authored MyST content on `main`.

## Verified result (local run, 2026-07-14)

Parsed `6.732-pt3.pdf` (Part III — Magnetic Properties of Solids, ~143 pp) with:

- model `vlm`, language `en`, `enable_formula` + `enable_table` on
- **Output**: `full.md` (343 KB, 4102 lines) + `images/` (592 figures) +
  MIDDLE-JSON (`content_list`, `content_list_v2`, `model`, `layout`)
- **Quality**: title/author/TOC with page numbers accurate; **970 block `$$`
  formulas extracted as numbered LaTeX** (`\tag{1.16}` etc.), directly MyST/MathJax
  compatible. Minor vlm OCR quirks (occasional `¯h` instead of `\hbar`, a few empty
  `$$` blocks, stray backslash) — correctable, expected.

## How it works (`mineru/parse_pdf.py`)

Local-file flow (validated against MinerU v4):

1. `POST /api/v4/file-urls/batch` → `{ batch_id, file_urls[], task_ids[] }`
2. `PUT` the PDF bytes to the pre-signed `file_urls[0]`
3. `GET  /api/v4/extract-results/batch/{batch_id}` → poll until `state == done`
4. Download `full_zip_url` → extract markdown + images

Remote-URL flow (`--url`): `POST /api/v4/extract/task` → poll
`/api/v4/extract/task/{task_id}` → download.

Auth: `Authorization: Bearer <token>` (token from `MINERU_TOKEN` env var / secret,
**never committed**).

## Rate limits (MinerU precise API — stay under)

- Submit: 50 files / minute
- Result query: 1000 / minute (script polls every 15 s — far below)
- Per user: ≤ 5000 files / day, ≤ 1000 pages / day (high priority)
- Single file: ≤ 200 MB, ≤ 200 pages

→ Parsing one chapter per run is well within quota.

## CI workflow (`.github/workflows/mineru.yml`)

Triggers on push to `mineru` (and `workflow_dispatch` for on-demand runs).
Resolves the PDF source in this order:

1. `workflow_dispatch` input `pdf_url`
2. repo secret `MINERU_PDF_URL`
3. first non-empty `url` in `mineru/sources.json`

Then runs the parser and uploads `mineru/output` as a build artifact.

### Repo secrets to set (Settings → Secrets and variables → Actions)

- `MINERU_TOKEN` — your MinerU API token (required)
- `MINERU_PDF_URL` — (optional) a hosted PDF URL to parse on push

## Local usage

```bash
export MINERU_TOKEN='sk-...'
python mineru/parse_pdf.py --pdf /path/to/book.pdf --out mineru/output --language en --model vlm
# or remote:
python mineru/parse_pdf.py --url https://example.com/book.pdf --out mineru/output
```
