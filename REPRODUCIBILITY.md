# Reproducibility

Run from the source directory.

```sh
python3 scripts/verify_repository.py
python3 verification/src/replay.py
```

The exact rational replay checks the seed, exterior and connector inequalities and the polynomial identity on rational unit-circle points. The proof supplies the continuation and winding argument.

See [paper build](paper/BUILD.md) for LaTeX reconstruction. Open [the illustration](visualization/index.html) in a browser. It uses no external libraries.
