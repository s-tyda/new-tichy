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
   * Python 3.7 +
   * Moduły: re, mechanize, time, bs4, sys

## Instalacja
[Link do pobrania najnowszej wersji](https://github.com/s-tyda/new-tichy/releases/tag/v.0.7.6)
## Konfiguracja

Odpalając skrypt po raz pierwszy (nieważne jaką komendą) konsola sama poprowadzi cię przez wstępną konfigurację i wygeneruje odpowiedni plik konfiguracyjny w folderze ze skryptem.

Polecam wrzucać sobie skrypt do folderu każdego projektu z C/C+ i tam go sobie oddzielnie konfigurować.

![tichy_first](images/tichy_first.gif?raw=true)

**Nie zapomnij potem ustawić aktualnego kursu za pomocą komendy **tichy course --set** (użycie poniżej), poniewż domyślnie żaden kurs nie jest wybrany!**

## Użycie:
```console
python tichy.py <komenda> [opcje] [<argumenty>]
tichy <komenda> [opcje] [<argumenty>]
```
    
Druga (zalecana) opcja jest dostępna tylko na linuxie, bądź przy dobrym [ustawieniu zmiennych środowiskowych systemu Windows](docs/python_environmental.md) oraz trzymaniu skryptu w folderze projektu.
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
* [Konfiguracja zmiennych środowiskowych Pythona na Windows](docs/python_environmental.md)
* [Konfiguracja skryptu w CLion](docs/clion_config.md)
* [Konfiguracja skryptu w MS Visual Studio](docs/vs_config.md)
* [Konfiguracja skryptu w MS Visual Studio Code](docs/vscode_config.md)