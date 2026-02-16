# Repository Guidelines

## Project Structure & Module Organization
Course content lives at the repository root as numbered Jupyter notebooks (`Mod0.ipynb`, `Mod1_cw.ipynb`, etc.), which the `_toc.yml` file assembles into the book; keep new lessons in this pattern so navigation remains predictable. Supporting assets (slides, screenshots, helper scripts like `triangle.py`) sit in `src/`, while `_images/`, `_static/`, and `_sphinx_design_static/` hold book-wide media and theme files—reuse existing folders rather than creating ad‑hoc ones. Publication metadata resides in `_config.yml`, and citations in `references.bib`. Place long-form reports or exports under `reports/` and keep raw experimentation in `tmp/` so builds stay clean.

Course is in Polish. Course is Targeted for student of "Satellite and Space Data Engineering". When adding examples, somehow link with satellite and space applications when possible.
## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate`: create/use an isolated environment.
- `pip install -r requirements.txt`: install Jupyter Book plus notebook dependencies.
- `jupyter-book build .`: rebuilds the full site, re-executing every notebook because `execute_notebooks: force` is enabled—treat this as the primary verification step before pushing.
- `jupyter-book clean .`: purge the `_build/` artifacts if you see stale outputs or switching branches.

## Coding Style & Naming Conventions
Follow PEP 8 for scripts (4-space indents, snake_case functions, UpperCamelCase classes) and fence outputs in notebooks with concise markdown explanations so the rendered book stays readable. Keep notebook filenames short, prefixed with the module number (`Mod7_cw.ipynb` for coursework, `Mod7.ipynb` for lecture). When adding images, prefer lowercase dash-separated names (e.g., `mod7-shell-demo.png`) and reference them via relative paths to `src/` or `_images/`.

## Testing Guidelines
Because builds execute notebooks, treat warnings as blockers—ensure every cell runs top to bottom without manual intervention. For standalone scripts, add quick self-checks (e.g., `python src/triangle.py --help`) and note them in the notebook narrative. If you introduce automated tests, place them in `tests/` mirroring the module structure and invoke them with `pytest` before the book build.

## Commit & Pull Request Guidelines
Recent history shows short, imperative commits (`fix`, `update cw6`); continue that style but add scope when useful (`fix: update Mod6 toc`). Reference related notebook names or issue numbers in the body. Pull requests should describe the affected modules, list verification commands (`jupyter-book build .`), and mention any unresolved merge artifacts (such as conflicts in `_toc.yml`) so reviewers can focus on the right sections. Include screenshots or rendered HTML diffs when visual changes matter.
