# new-tichy

* [new-tichy](#new-tichy)
  * [Co to new-tichy?](#co-to-new-tichy)
  * [Wymagania](#wymagania)
  * [Konfiguracja](#konfiguracja)
  * [Użycie](#użycie)
  * [Ważniejsze przykłady](#ważniejsze-przykłady)
  * [Przydatne poradniki](#przydatne-poradniki)

## Co to new-tichy?

**New-tichy** to napisany przez [h-okon](https://github.com/h-okon) i rozbudowany oraz odnowiony przeze mnie skrypt w języku Python, który pozwala na wysyłanie zadań na **Tichy** (sprawdzarkę algorytmiczną UMCS) za pomocą konsoli. Zwraca on wynik testów po sprawdzeniu.

## Wymagania
Skrypt (.py):
* Python 3.8 +
* Moduły: mechanize, bs4, cryptography, colorama, termcolor

Windows (.exe):
* brak
* (opcjonalne i zalecane) [Konfiguracja zmiennych środowiskowych pliku .exe na Windows](docs/windows_environmental.md)
  (dzięki czemu można odpalać skrypt w każdym miejscu za pomocą konsoli Windowsa)

## Instalacja
[Link do pobrania najnowszej wersji](https://github.com/s-tyda/new-tichy/releases/tag/v.0.8.0)
## Konfiguracja

Odpalając skrypt po raz pierwszy (nieważne jaką komendą) konsola sama poprowadzi cię przez wstępną konfigurację i wygeneruje odpowiedni plik konfiguracyjny w katalog głównym.
Plik konfiguracyjny jest tworzony globalnie i znajduje się w folderze: "<katalog główny>\.config\new-tichy"
Cały plik konfiguracyjny jest zaszyfrowany, a plik z kluczem szyfrującym znajduje się również w powyższym folderze.

Nie ma aktualnie żadnej potrzeby dodawać dodatkowych plików do folderów z projektem.

![tichy_first](images/tichy_first.gif?raw=true)

**Nie zapomnij potem ustawić aktualnego kursu za pomocą komendy **tichy course --set** (użycie poniżej), poniewż domyślnie żaden kurs nie jest wybrany!**

## Użycie:
```console
python tichy.py <komenda> [opcje] [<argumenty>]
tichy <komenda> [opcje] [<argumenty>]
```
    
Druga (zalecana) opcja jest dostępna tylko na linuxie, bądź przy dobrym [ustawieniu zmiennych środowiskowych systemu Windows](docs/python_environmental.md).
## Ważniejsze przykłady:
```console
#Wyświetla informacje o użyciu
tichy 
tichy -h
tichy --help
tichy --pomoc
```
    
![tichy_help](images/tichy_help.gif?raw=true)

```console
#Ustawia ID kursu w konfiguracji na <id>
#Argument <id> jest opcjonalny
tichy <course, c, kurs> -s [<id>]
tichy <course, c, kurs> --set [<id>]
tichy <course, c, kurs> --ustaw [<id>]
```

![tichy_help](images/tichy_course_set.gif?raw=true)

```console
#Wysyła zadanie o relatywnej ścieżce <path> na sprawdzarkę
#Argument <nr> jest opcjonalny
tichy <exercise, e, zadanie, zad> -s <path> [<nr]
tichy <exercise, e, zadanie, zad> --send <path> [<nr]
tichy <exercise, e, zadanie, zad> --wyslij <path> [<nr]
```

![tichy_help](images/tichy_exercise_send.gif?raw=true)

**Żeby zobaczyć inne komendy przejdź do [dokumentacji](docs/documentation.md).**

## Przydatne poradniki
* [Instalacja Pythona na Windows](docs/python_installation.md)
* [Konfiguracja zmiennych środowiskowych pliku .exe na Windows](docs/windows_environmental.md)
* [Konfiguracja zmiennych środowiskowych Pythona na Windows](docs/python_environmental.md)
* [Konfiguracja skryptu w CLion](docs/clion_config.md)
* [Konfiguracja skryptu w MS Visual Studio](docs/vs_config.md)
* [Konfiguracja skryptu w MS Visual Studio Code](docs/vscode_config.md)