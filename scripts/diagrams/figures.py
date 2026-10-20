"""The book's figures, hand-laid out with dg.py and chartkit.py. Run build.py to write _includes/diagrams/.

Every figure is its own module in figs/ (fig_<chapter>_<n>.py), which registers itself with @figure.
FIG_CHAPTER=<n> in the environment loads only that chapter's modules (to build one chapter while
others are being edited).
"""
import importlib
import os
import pkgutil

from registry import FIGURES  # noqa: F401  (re-exported for build.py)

_figs = os.path.join(os.path.dirname(__file__), "figs")
_only = os.environ.get("FIG_CHAPTER")
for _m in sorted(pkgutil.iter_modules([_figs]), key=lambda m: m.name):
    if _only and not _m.name.startswith(f"fig_{_only}_"):
        continue
    importlib.import_module(f"figs.{_m.name}")
