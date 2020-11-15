## Instalacja Pythona (Windows) 
   - Wchodzimy na stronę https://docs.conda.io/en/latest/miniconda.html
   - Pobieramy minicondę3.

![img_01](../images/img_01.png?raw=true)

- Instalujemy zostawiając wszystkie opcje domyślne.
- W pasku wyszikuwania wyszukujemy **Anaconda Prompt** i odpalamy. Jest to konsola condy.

![img_02](../images/img_02.png?raw=true)

![img_03](../images/img_03.png?raw=true)

- Pobieramy wszystkie potrzebne moduły, wpisując kolejno:
```console
conda install -c anaconda colorama
conda install -c omnia termcolor
conda install -c anaconda beautifulsoup4
pip install mechanize
```
- Poprawność pobrania potrzebnych modułów można najszybciej sprawdzić próbując użyć skryptu poprzez komendę:
```console
python path\tichy.py
```

- Jeśli tak jak u mnie wyświetla się komunikat o błędzie użycia, a nie o brakujących modułach, to wszystko jest ok i nasz Python jest gotowy do uruchomienia skryptu.

---

####Zobacz też:
[Konfiguracja zmiennych środowiskowych Pythona na Windows](python_environmental.md)