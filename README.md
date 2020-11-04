# quicktichy

* [quicktichy](#quicktichy)
  * [Co to quicktichy?](#co-to-quicktichy?)
  * [Wymagania](#wymagania)
  * [Konfiguracja](#konfiguracja)
  * [Użycie:](#użycie)
  * [Przykład:](#przykład)
  * [Instalacja Pythona (Windows)](#instalacja-pythona-(windows))
  * [Konfiguracja CLion](#konfiguracja-clion)

## Co to quicktichy?

**Quicktichy** to skrypt napisany w języku Python, który pozwala na wysyłanie zadań na **Tichy** (sprawdzarkę algorytmiczną UMCS) za pomocą konsoli. Zwraca on wynik testów po sprawdzeniu.

## Wymagania
   * Python 3.7 +
   * Moduły: re, mechanize, time, bs4, sys

## Konfiguracja

* W pliku **tichy.py** w linijce **10** zamieniamy link do kursu na sprawdzarce. W plikach znajduje się link do kursu **AiSD I 2020/2021**. Również zmieniamy pola **login** i **hasło** (linijki **21** i **22**) na swoje dane do sprawdzarki.
```python
kurs = "https://tichy.umcs.lublin.pl/course/2ae9322bea1944e59a218708cfa9a793/"
username = 'login'
passwd = 'haslo'
```

## Użycie
    python tichy.py <numer zadania> <rozwiązanie>
## Przykład

![przyklad](https://i.imgur.com/ZJZnuPO.png)


## Instalacja Pythona (Windows)
- Wchodzimy na stronę https://docs.conda.io/en/latest/miniconda.html
- Pobieramy minicondę3.

![img_01](images/img_01.png?raw=true)

- Instalujemy zostawiając wszystkie opcje domyślne.
- W pasku wyszikuwania wyszukujemy **Anaconda Prompt** i odpalamy. Jest to konsola condy.

![img_02](images/img_02.png?raw=true)

![img_03](images/img_03.png?raw=true)

- Pobieramy wszystkie potrzebne moduły, wpisując kolejno:
```
conda install -c anaconda colorama
conda install -c omnia termcolor
conda install -c anaconda beautifulsoup4
pip install mechanize
```
- Poprawność pobrania potrzebnych modułów można najszybciej sprawdzić próbując użyć skroptu poprzez komendę:
```
python path\tichy.py
```
![img_04](images/img_04.png?raw=true)

Jeśli tak jak u mnie wyświetla się komunikat o błędzie użycia, a nie o brakujących modułach, to wszystko jest ok i nasz Python jest gotowy do uruchomienia skryptu. Możemy to przetestować podając w parametrach odpowiednie dane.

![img_05](images/img_05.png?raw=true)

## Konfiguracja CLion
- Upewniamy się, że mamy zainstalowaną wtyczkę **Python Community Edition**. W tym celu otwieramy **File->Settings->Plugins->Installed** (ctrl+alt+S) i wyszukujemy **Python Community Edition**.

![img_06](images/img_06.png?raw=true)

- Następnie przechodzimy do zakładaki **Build, Execution, Deployment->Python Interpreter**, w rozwijanej liście wybieramy **Show all**, a nastęnie klikamy **add**.

![img_07](images/img_07.png?raw=true)

- W menu po lewej wybieramy **System Interpreter** i w rozwijanej liście wybieramy naszą minicondę. Jeśli jej nie ma to trzeba ją dodać ręcznie. W tym celu trzeba nacisnąć **trzy kropki** (shift+enter) i wskazać ścieżkę do pliku **python.exe** w folderze z condą (domyślnie jest to **C:\Users\user\miniconda3\python.exe**).

![img_08](images/img_08.png?raw=true)

- Wybieramy nowo dodany interpretator i zatwierdzamy podwójnie **OK**. Po zatwierdzeniu odczekujemy chwilę aż środowisko załaduje interpretator.
- Następnie wystarczy już tylko dodać konfigurację uruchamiania. Na głównym pasku wybieramy **Run->Edit Configurations**. Plusikiem dodajemy nową konfigurację, wybierając jako szablon **Python**. W polu **Script path** wybieramy ścieżkę do skryptu. W polu **Parameters** ustawiamy kolejno parametry: **nr_zadania** (np. 4) **$FilePath$**. Na koniec w polu **Python interpreter** zaznaczamy **Use specified interpreter** i wybieramy naszą minicondę.

![img_09](images/img_09.png?raw=true)