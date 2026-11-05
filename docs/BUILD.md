# Building the mod

English | [Português (Brasil)](BUILD.pt-BR.md)

Install Python 3 and [Norbyte's LSLib 1.20.4](https://github.com/Norbyte/lslib/releases/tag/v1.20.4), including its required .NET runtime. From the repository root, run:

```powershell
python verify.py
python -m unittest test_regression
python build.py --divine "C:\path\to\Divine.exe"
```

Outputs appear in `dist/`. The build verifies the source resources, event ordering, package contents, binary conversion, equivalence with the tested animation data, and installer ZIP. Toolkit Data is not needed to rebuild this package.
