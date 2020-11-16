#!/usr/bin/env python3

import colorama
import mechanize
import time
from bs4 import BeautifulSoup
import sys
import os.path
import subprocess
from termcolor import colored
from configparser import ConfigParser


def help_f(test):
    if test == "zero":
        if lang == "pl":
            print('Użycie: tichy <komenda> [opcje] [<args>]\n')
            print("Komendy:")
            print(
                '   {:<56} {:<s}'.format(
                    "course, c, kurs [opcje] [<args>]", "Obsługa kursów"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "exercise, e, zadanie, zad [opcje] [<args>]", "Obsługa zadań"
                )
            )
            print("\nOpcje:")
            print(
                '   {:<56} {:<s}'.format(
                    "-c, --config, --dane", "Wyświetla zawartość pliku konfiguracji"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-h, --help, --pomoc", "Wyświetla informacjie o użyciu"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-l, --list, --lista", "Wyświetla dostępne kursy"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-p, --password, --haslo [<pswd>]",
                    "Zmienia hasło w konfiguracji na pswd (opcjonalne)",
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-u, --username, --login [<usr>]",
                    "Zmienia login w konfiguracji na usr (opcjonalne)",
                )
            )
        else:
            print('Usage: tichy <command> [options] [<args>]\n')
            print("Commands:")
            print(
                '   {:<56} {:<s}'.format(
                    "course, c, kurs [options] [<args>]", "Course handling"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "exercise, e, zadanie, zad [options] [<args>]", "Exercise handling"
                )
            )
            print("\nOptions:")
            print(
                '   {:<56} {:<s}'.format(
                    "-c, --config, --dane", "Shows content of config file"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-h, --help, --pomoc", "Shows usage information"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-l, --list, --lista", "Shows available courses"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-p, --password, --haslo [<pswd>]",
                    "Change config password to pswd (optional)",
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-u, --username, --login [<usr>]",
                    "Change config username to usr (optional)",
                )
            )
        return 1
    if test == "course":
        if lang == "pl":
            print('Użycie: tichy <course, c, kurs> [opcje] [<args>]\n')
            print("Opcje:")
            print(
                '   {:<56} {:<s}'.format(
                    "-h, --help, --pomoc", "Wyświetla informacjie o użyciu"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-l, --list, --lista", "Wyświetla dostępne zadania"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-s, --set, --ustaw [<id>]",
                    "Ustawia ID kursu w konfiguracji na id (argument opcjonalny)",
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-v, --view, --zobacz", "Wyświetla aktualnie wybrany kurs"
                )
            )
        else:
            print('Usage: tichy <course, c, kurs> [options] [<args>]\n')
            print("Options:")
            print(
                '   {:<56} {:<s}'.format(
                    "-h, --help, --pomoc", "Shows usage information"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-l, --list, --lista", "Shows all exercises on course"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-s, --set, --ustaw [<id>]",
                    "Sets current course in config to id (optional)",
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-v, --view, --zobacz", "Shows currently selected course"
                )
            )
        return 1
    if test == "exercise":
        if lang == "pl":
            print('Użycie: tichy <exercise, e , zadanie, zad> [opcje]' '[<args>]\n')
            print("Opcje:")
            print(
                '   {:<56} {:<s}'.format(
                    "-h, --help, --pomoc", "Wyświetla informacjie o użyciu"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-l, --list, --lista",
                    "Wyświetla wszystki rozwiązania zadania (nie działa jeszcze)",
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-s, --send, --wyslij <plik> [<nr_zadania>]",
                    "Wysyła rozwiązanie plik na sprawdzarkę i wyświetla wynik",
                )
            )
            print('   {:<56} {:<s}'.format("", "Numer zadania jest opcjonalny"))
        else:
            print('Usage: tichy <exercise, e , zadanie, zad> [options]' '[<args>]\n')
            print("Options:")
            print(
                '   {:<56} {:<s}'.format(
                    "-h, --help, --pomoc", "Shows usage information"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-l, --list, --lista", "Shows all exercise answers (don't work yet)"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "-s, --send, --wyslij <path> [<nr>]",
                    "Sends answer to tichy and shows results",
                )
            )
            print('   {:<56} {:<s}'.format("", "Exercise number is optional"))
        return 1
    if test == "send":
        return 1


# Otwieranie strony logowania
def open_tichy():
    br.open("https://tichy.umcs.lublin.pl/accounts/login/")
    if lang == "pl":
        print(colored(br.title() + ", " + username + '!', attrs=['bold']))
    else:
        print(colored("Welcome on tichy, " + username + '!', attrs=['bold']))


# Logowanie na sprawdzarce
def login():
    if lang == "pl":
        print("[  ]Logowanie do sprawdzarki...")
    else:
        print("[  ]Logging to tichy...")
    br.select_form(nr=0)
    control = br.form.find_control("username")
    control.value = username
    control = br.form.find_control("password")
    control.value = passwd
    br.submit()
    if br.title() == "Witamy na tichym":
        if lang == "pl":
            print(colored("Niepoprawny login lub hasło.", 'red', attrs=['bold']))
        else:
            print(colored("Wrong login or password.", 'red', attrs=['bold']))
        sys.exit(1)
    if lang == "pl":
        print(f"[{OK}]Zalogowano poprawnie.")
    else:
        print(f"[{OK}]Logged successfully.")


# Otworzenie kursu
def open_course(temp_course_id):
    if lang == "pl":
        print("[  ]Otwieranie strony kursu...")
    else:
        print("[  ]Opening course...")
    try:
        link = course_find(temp_course_id)
        br.open(link)
    except Exception:
        if lang == "pl":
            print(colored("Taki kurs nie istnieje.", 'red', attrs=['bold']))
        else:
            print(colored("This course doesn't exist.", 'red', attrs=['bold']))
        sys.exit(1)
    if lang == "pl":
        print(f"[{OK}]Otworzono kurs " + br.title() + ".")
    else:
        print(f"[{OK}]Successfully opened course " + br.title() + ".")


# Otworzenie strony głównej
def open_main_page():
    br.open("https://tichy.umcs.lublin.pl/course/")


# Wyświetlanie listy kursów
def course_list():
    kursy_response = br.response().read()
    soup = BeautifulSoup(kursy_response, "html.parser")
    kurs_body = soup.find("ul", {"class": "course-list"})
    kurs_list = kurs_body.findAll('li')
    # print (kurs_list[0].get_text(strip=True))
    temp_course_id = 1
    if lang == "pl":
        print("[  ]Pobieranie listy kursów...")
        print(f"[{OK}]Pobrano pomyślnie.\n")
        print(colored("Dostępne kursy:", attrs=['bold']))
    else:
        print("[  ]Downloading course list...")
        print(f"[{OK}]Downloaded successfully.\n")
        print(colored("Available courses:", attrs=['bold']))
    for li in kurs_list:
        print('[' + str(temp_course_id) + '] ' + li.get_text(strip=True))
        ++temp_course_id


# Zwracanie kursu o danym ID
def course_find(temp_course_id, is_print=False):
    kursy_response = br.response().read()
    soup = BeautifulSoup(kursy_response, "html.parser")
    kurs_body = soup.find("ul", {"class": "course-list"})
    kurs_list = kurs_body.findAll('li')
    if not is_print:
        link = kurs_list[temp_course_id - 1].find('a')['href']
        return 'https://tichy.umcs.lublin.pl' + link
    else:
        print(colored("\nAktualnie wybrany kurs:", attrs=['bold']))
        print(
            '['
            + str(temp_course_id)
            + '] '
            + kurs_list[temp_course_id - 1].get_text(strip=True)
        )


# Wyświetlanie listy zadań
def task_list():
    kursy_response = br.response().read()
    soup = BeautifulSoup(kursy_response, "html.parser")
    kurs_body = soup.find("table", {"class": "table table-striped"}).find('tbody')
    kurs_list = kurs_body.findAll('tr')
    if lang == "pl":
        print("[  ]Pobieranie listy zadań...")
        print(f"[{OK}]Pobrano pomyślnie.\n")
        print(colored("Dostępne zadania:", attrs=['bold']))
    else:
        print("[  ]Downloading exercise list...")
        print(f"[{OK}]Downloaded successfully.\n")
        print(colored("Available exercises:", attrs=['bold']))
    for tr in kurs_list:
        tds = tr.findAll('td')
        kurs = tds[1].get_text(strip=True)
        print('[' + tds[0].text + '] ' + kurs)


# Testowanie z przykładowymi danymi
def exercise_test(ex_number, plik):
    found = False
    kursy_response = br.response().read()
    soup = BeautifulSoup(kursy_response, "html.parser")
    kurs_body = soup.find("table", {"class": "table table-striped"}).find('tbody')
    kurs_list = kurs_body.findAll('tr')
    for tr in kurs_list:
        tds = tr.findAll('td')
        if str(ex_number) == tds[0].text:
            found = True
            el = tds[1].find('a')['href']
            zadanie = 'https://tichy.umcs.lublin.pl' + el
            zad_name = tds[1].get_text(strip=True)

    if not found:
        if lang == "pl":
            print(
                colored(f"Nie znaleziono zadania nr {ex_number}", 'red', attrs=['bold'])
            )
        else:
            print(colored(f"Cannot find exercise {ex_number}", 'red', attrs=['bold']))
        exit(1)
    if lang == "pl":
        print("[  ]Otwieranie strony zadania " + zad_name + "...")
    else:
        print("[  ]Opening exercise " + zad_name + "...")
    br.open(zadanie)
    if lang == "pl":
        print(f"[{OK}]Otworzono zadanie " + zad_name + ".")
    else:
        print(f"[{OK}]Successfully opened exercise " + zad_name + ".")
    ex_response = br.response().read()
    soup = BeautifulSoup(ex_response, "html.parser")
    ex_body = soup.findAll("div", {"class": "panel-body"})[1]
    paragraphs = ex_body.findAll('pre')
    inputs = []
    outputs = []
    for idx, par in enumerate(paragraphs):
        if int(idx) % 2 == 0:
            inputs.append(par.get_text(strip=True))
        else:
            outputs.append(par.get_text(strip=True))
    subprocess.run('g++ ' + plik)
    # result = subprocess.run(['a.exe'], capture_output=True, text=True, input=inputs[0])
    for idx, inp in enumerate(inputs):
        result = subprocess.run(['a.exe'], capture_output=True, text=True, input=inp)
        print("Przykładowe dane " + str(idx + 1) + ": ", end="")
        if "".join(result.stdout.split()) == "".join(outputs[idx].split()):
            print(colored("zaliczone", 'green', attrs=['bold']))
        else:
            print(colored("niezaliczone", 'red', attrs=['bold']))


# Wysyłanie pliku
def send_file(ex_number, plik, results=None):
    if results is None:
        results = []
    with open(plik, 'r') as file:
        data = file.read().replace('\n', '\n  ')
    found = False
    kursy_response = br.response().read()
    soup = BeautifulSoup(kursy_response, "html.parser")
    kurs_body = soup.find("table", {"class": "table table-striped"}).find('tbody')
    kurs_list = kurs_body.findAll('tr')
    for tr in kurs_list:
        tds = tr.findAll('td')
        if str(ex_number) == tds[0].text:
            found = True
            el = tds[1].find('a')['href']
            zadanie = 'https://tichy.umcs.lublin.pl' + el
            zad_name = tds[1].get_text(strip=True)

    if not found:
        if lang == "pl":
            print(
                colored(f"Nie znaleziono zadania nr {ex_number}", 'red', attrs=['bold'])
            )
        else:
            print(colored(f"Cannot find exercise {ex_number}", 'red', attrs=['bold']))
        exit(1)

    if lang == "pl":
        print("[  ]Otwieranie strony zadania " + zad_name + "...")
    else:
        print("[  ]Opening exercise " + zad_name + "...")
    br.open(zadanie)
    if lang == "pl":
        print(f"[{OK}]Otworzono zadanie " + zad_name + ".")
    else:
        print(f"[{OK}]Successfully opened exercise " + zad_name + ".")
    req = br.click_link(text='Wyślij rozwiązanie')
    if lang == "pl":
        print("[  ]Wysyłanie rozwiązania zadania " + zad_name + "...")
    else:
        print("[  ]Sending answer of exercise " + zad_name + "...")
    br.open(req)
    # print(" " + br.title())
    br.select_form(nr=0)
    rozwiazanie = br.form.find_control("src")
    rozwiazanie.value = str(data)
    br.submit()
    if lang == "pl":
        print(f"[{OK}]Wysłano rozwiązanie.")
    else:
        print(f"[{OK}]Sent.")
    link_to_exercise = br.geturl()
    sprawdzany = True
    if lang == "pl":
        print("[  ]Oczekiwanie na wyniki...")
    else:
        print("[  ]Waiting for results...")
    while sprawdzany:
        sprawdzany = False
        time.sleep(0.5)
        br.open(link_to_exercise)
        response = br.response().read()
        soup = BeautifulSoup(response, "html.parser")
        for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
            tds = tr.findAll('td')
            if tds[1].text.strip() == 'Sprawdzany':
                sprawdzany = True
    if lang == "pl":
        print(f"[{OK}]Otrzymano wyniki.\n")
    else:
        print(f"[{OK}]Results received.\n")

    br.open(link_to_exercise)
    response = br.response().read()
    soup = BeautifulSoup(response, "html.parser")
    # print("ID | Result    | Time (s)        | Memory (kB)")
    for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
        tds = tr.findAll('td')
        results.append(tds[1].text.strip())

    longest = max(results, key=len)

    if longest == "Naruszenie ochrony pamięci":
        print(
            "%2s | %-26s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Błąd wykonania":
        print(
            "%2s | %-14s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Niedozwolona instrukcja":
        print(
            "%2s | %-23s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Przekroczona pamięć":
        print(
            "%2s | %-19s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Zła odpowiedź":
        print(
            "%2s | %-13s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Zaliczone":
        print(
            "%2s | %-9s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Przekroczony czas":
        print(
            "%2s | %-17s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )
    elif longest == "Błąd kompilacji":
        print(
            "%2s | %-15s | %-15s | %s"
            % (
                "ID",
                "Result",
                "Time (s)",
                "Memory (kB)",
            )
        )

    for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
        tds = tr.findAll('td')
        if tds[1].text.strip() != "Zaliczone":
            status = colored(tds[1].text.strip(), 'red', attrs=['bold'])
        else:
            status = colored(tds[1].text.strip(), 'green', attrs=['bold'])

        if longest == "Niedozwolona instrukcja":
            row_format = '{:>2} | {:<36} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Naruszenie ochrony pamięci":
            row_format = '{:>2} | {:<39} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Błąd wykonania":
            row_format = '{:>2} | {:<27} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Przekroczona pamięć":
            row_format = '{:>2} | {:<32} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Zła odpowiedź":
            row_format = '{:>2} | {:<26} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Zaliczone":
            row_format = '{:>2} | {:<22} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Przekroczony czas":
            row_format = '{:>2} | {:<30} | {:<6s} / {:<6s} | {:>s} / {:>s}'
        elif longest == "Błąd kompilacji":
            row_format = '{:>2} | {:<28} | {:<6s} / {:<6s} | {:>s} / {:>s}'

        print(
            row_format.format(
                tds[0].text,
                status,
                tds[3].text.strip(),
                tds[4].text.strip(),
                tds[5].text.strip(),
                tds[6].text.strip(),
            )
        )


if __name__ == '__main__':
    colorama.init(strip=False)
    global OK
    OK = colored("OK", 'green', attrs=['bold'])
    args = sys.argv

    # Sprawdzanie istnienia pliku konfiguracyjnego
    if not os.path.exists("config.ini"):
        print(
            "It semms it's your first time using tichy script. You have"
            "to set your config to proceed.\n"
            "Wygląda na to, że używasz skryptu tichy po raz"
            "pierwszy. Musisz wprowadzić swoje dane logowania żeby"
            "kontynuować.\n"
            "Choose your language. Wybierz język.\n"
            "[pl] polski\n[en] english"
        )

        lang = input()
        if lang == "pl":
            usr = input("Twój login: ")
            psw = input("Twoje hasło: ")
        else:
            usr = input("Your username: ")
            psw = input("Your password: ")
        f = open("config.ini", "x")
        f = open("config.ini", "a")
        f.write("[CONFIG]\n")
        f.write("username = " + usr + '\n')
        f.write("password = " + psw + '\n')
        f.write("course_id = \n")
        f.write("language = " + lang)
        f.close()
        if lang == "pl":
            print(f"[{OK}]Teraz możesz już  korzystać ze skryptu.")
            print(
                "Nie zapomnij ustawić ID kursu, za pomocą komendy 'tichy course --set'!"
            )
        else:
            print(f"[{OK}]Now you can proceed with running a script.")
            print("Don't forgt to set course ID, using command 'tichy course --set'!")
        sys.exit(0)

    # Odczytanie danych z konfiguracji
    config_object = ConfigParser()
    config_object.read("config.ini")

    # Dane
    userinfo = config_object["CONFIG"]
    username = userinfo["username"]
    passwd = userinfo["password"]
    course_id = userinfo["course_id"]
    lang = userinfo["language"]

    # Włączanie przeglądarki
    br = mechanize.Browser()

    if len(args) == 1:
        help_f("zero")
    elif args[1].startswith("-"):
        if args[1] == '--list' or args[1] == '-l' or args[1] == '--lista':
            open_tichy()
            login()
            open_main_page()
            course_list()
        elif args[1] in ('--username', '-u', '--login'):
            if len(args) == 2:
                if lang == "pl":
                    usr = input("Nowy login: ")
                else:
                    usr = input("New username: ")
            else:
                usr = args[2]
            userinfo["username"] = usr
            if lang == "pl":
                print("[  ]Zapisywanie nowej nazwy użytkownika...")
            else:
                print("[  ]Saving new username...")
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
            if lang == "pl":
                print(f"[{OK}]Zapisano pomyślnie")
            else:
                print(f"[{OK}]Saved successfully")
        elif args[1] in ('--password', '-p', '--haslo'):
            if len(args) == 2:
                if lang == "pl":
                    passw = input("Nowe hasło: ")
                else:
                    passw = input("New password: ")
            else:
                passw = args[2]
            userinfo["password"] = passw
            if lang == "pl":
                print("[  ]Zapisywanie nowego hasła...")
            else:
                print("[  ]Saving new password...")
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
            if lang == "pl":
                print(f"[{OK}]Zapisano pomyślnie.")
            else:
                print(f"[{OK}]Saved successfully.")
        elif args[1] == '--config' or args[1] == '-c' or args[1] == '--dane':
            if lang == "pl":
                print(colored("Zawartość pliku konfiguracji:", attrs=['bold']))
            else:
                print(colored("Contents of config file:", attrs=['bold']))
            f = open('config.ini', 'r')
            for p in f:
                if p.startswith('[') or p.endswith(']'):
                    print(colored(p, 'red', attrs=['bold']), end="")
                else:
                    print(p, end="")
        elif args[1] == '--help' or args[1] == '-h' or args[1] == '--pomoc':
            help_f("zero")
        else:
            help_f("zero")

    elif args[1] in ('course', 'kurs', 'c'):
        if len(args) == 2 or args[2] in ('--help', '-h', '--pomoc'):
            help_f("course")
        elif args[2] == '--list' or args[2] == '-l' or args[2] == '--lista':
            open_tichy()
            login()
            open_main_page()
            open_course(int(course_id))
            task_list()
        elif args[2] == '--view' or args[2] == '-v' or args[2] == '--zobacz':
            open_tichy()
            login()
            open_main_page()
            course_find(int(course_id), True)
        elif args[2] == '--set' or args[2] == '-s' or args[2] == '--ustaw':
            if len(args) == 3:
                if lang == "pl":
                    new_id = input("Nowe ID kursu: ")
                else:
                    new_id = input("New course ID: ")
            else:
                new_id = args[3]
            userinfo["course_id"] = new_id
            if lang == "pl":
                print("[  ]Zapisywanie nowego ID kursu...")
            else:
                print("[  ]Saving new course ID...")
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
            if lang == "pl":
                print(f"[{OK}]Zapisano pomyślnie.")
            else:
                print(f"[{OK}]Saved successfully.")
        elif args[2] in ('--points', '-p', '--punkty'):
            print("Not implemented yet")
        else:
            help_f("course")
    elif args[1] in ('exercise', 'zadanie', 'zad', 'e'):
        if len(args) == 2 or args[2] in ('--help', '-h', '--pomoc'):
            help_f("exercise")
        elif args[2] in ('--list', '-l', '--lista'):
            print('list')
        elif args[2] in ('--send', '-s', '--wyslij'):
            if len(args) < 4 or len(args) > 5:
                print("Error")
                sys.exit(1)

            open_tichy()
            login()
            open_main_page()
            open_course(int(course_id))
            if not os.path.exists(args[3]):
                if lang == "pl":
                    print(colored("Nie znaleziono pliku.", 'red', attrs=['bold']))
                else:
                    print(colored("File not found.", 'red', attrs=['bold']))
                sys.exit(1)

            if len(args) == 5:
                nr_zad = args[4]
            else:
                task_list()
                if lang == "pl":
                    nr_zad = input("\nNumer zadania: ")
                else:
                    nr_zad = input("\nExercise number: ")
            send_file(nr_zad, args[3])
        elif args[2] in ('--test', '-t'):
            open_tichy()
            login()
            open_main_page()
            open_course(int(course_id))
            exercise_test(args[3], args[4])
        else:
            help_f("exercise")
