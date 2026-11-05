# Construção do mod

[English](BUILD.md) | Português (Brasil)

Instale Python 3 e o [LSLib 1.20.4 do Norbyte](https://github.com/Norbyte/lslib/releases/tag/v1.20.4), com o runtime .NET exigido. Na raiz do repositório, execute:

```powershell
python verify.py
python -m unittest test_regression
python build.py --divine "C:\caminho\para\Divine.exe"
```

Os arquivos são gerados em `dist/`. O processo verifica os recursos de origem, a ordem dos eventos, o conteúdo do pacote, a conversão binária, a equivalência com os dados testados e o ZIP instalável. O Toolkit Data não é necessário para reconstruir o pacote.
