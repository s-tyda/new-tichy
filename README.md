# quicktichy

* [quicktichy](#quicktichy)
  * [Co to quicktichy?](#co-to-quicktichy)
  * [Wymagania](#wymagania)
  * [Konfiguracja](#konfiguracja)
  * [Użycie](#użycie)
  * [Ważniejsze przykłady](#ważniejsze-przykłady)

## Co to quicktichy?

**Quicktichy** to napisany przez [h-okon](https://github.com/h-okon) i rozbudowany przeze mnie skrypt w języku Python, który pozwala na wysyłanie zadań na **Tichy** (sprawdzarkę algorytmiczną UMCS) za pomocą konsoli. Zwraca on wynik testów po sprawdzeniu.

## Wymagania
   * Python 3.7 +
   * Moduły: re, mechanize, time, bs4, sys

## Konfiguracja

Odpalając skrypt po raz pierwszy (nieważne jaką komendą) konsola sama poprowadzi cię przez wstępną konfigurację i wygeneruje odpowiedni plik konfiguracyjny w folderze ze skryptem.

Polecam wrzucać sobie skrypt do folderu każdego projektu z C/C+ i tam go sobie oddzielnie konfigurować.

![tichy_first](images/tichy_first.gif?raw=true)

**Nie zapomnij potem ustawić aktualnego kursu za pomocą komendy **tichy course -set** (użycie poniżej), poniewż domyślnie żaden kurs nie jest wybrany!**

## Użycie:
    python tichy.py <komenda> [opcje] [<argumenty>]
    tichy <komenda> [opcje] [<argumenty>]
    
Druga (zalecana) opcja jest dostępna tylko na linuxie, bądź przy dobrym ustawieniu zmiennych środowiskowych systemu Windows oraz trzymaniu skryptu w folderze projektu.
## Ważniejsze przykłady:
Żeby zobaczyć inne komendy użyj jednej z poniższych opcji, albo przejdź do [dokumentacji](docs/documentation.md).
```python
#Wyświetla informacje o użyciu
tichy 
tichy -h
tichy --help
tichy --pomoc
```
    
![tichy_help](images/tichy_help.gif?raw=true)

```python
#Ustawia ID kursu w konfiguracji na 'id'
#Argument 'id' jest opcjonalny
tichy <course, c, kurs> -s [<id>]
tichy <course, c, kurs> --set [<id>]
tichy <course, c, kurs> --ustaw [<id>]
```

![tichy_help](images/tichy_course_set.gif?raw=true)

```python
#Wysyła zadanie o relatywnej ścieżce 'path' na sprawdzarkę
#Argument 'nr' jest opcjonalny
tichy <exercise, e, zadanie, zad> -s <path> [<nr]
tichy <exercise, e, zadanie, zad> --send <path> [<nr]
tichy <exercise, e, zadanie, zad> --wyslij <path> [<nr]
```

![tichy_help](images/tichy_exercise_send.gif?raw=true)
