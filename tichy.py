#!/usr/bin/env python3

import colorama
import getpass
import mechanize
import time
from bs4 import BeautifulSoup
import sys
import os.path
import subprocess
from termcolor import colored
from configparser import ConfigParser
from pathlib import Path
from cryptography.fernet import Fernet


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
            print(
                '   {:<56} {:<s}'.format(
                    "send, s, wyslij <plik> [<nr_zadania>]", "Wysyłanie zadań na sprawdzarkę"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "test, t <plik> [<nr_zadania>]", "Testowanie zadań przykładowymi danymi"
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
                    "-h, --help, --pomoc", "Wyświetla informacje o użyciu"
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
            print("\nCommands:")
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
            print(
                '   {:<56} {:<s}'.format(
                    "send, s, wyslij <path> [<nr>]", "Sending answer to tichy"
                )
            )
            print(
                '   {:<56} {:<s}'.format(
                    "test, t <path> [<nr>]", "Validating file with example test"
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
    elif test == "course":
        if lang == "pl":
            print('Użycie: tichy <course, c, kurs> [opcje] [<args>]\n')
            print("Opis:")
            print("Ta komenda jest odpowiedzialna za obsługę kursów.")
            print("\nOpcje:")
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
            print("Description:")
            print("This command is responsible for course handling.")
            print("\nOptions:")
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
    elif test == "exercise":
        if lang == "pl":
            print('Użycie: tichy <exercise, e , zadanie, zad> [opcje] [<args>]\n')
            print("Opis:")
            print("Ta komenda jest odpowiedzialna za obsługę zadań.")
            print("\nOpcje:")
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
                    "Wysyła rozwiązanie o relatywnej ścieżce <plik> na sprawdzarkę i wyświetla wynik",
                )
            )
            print('   {:<56} {:<s}'.format("", "Numer zadania jest opcjonalny"))
        else:
            print('Usage: tichy <exercise, e , zadanie, zad> [options] [<args>]\n')
            print("Description:")
            print("This command is responsible for exercise handling.")
            print("\nOptions:")
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
                    "Sends answer on relative path <path> to tichy and shows results",
                )
            )
            print('   {:<56} {:<s}'.format("", "Exercise number <nr> is optional"))
            print(
                '   {:<56} {:<s}'.format(
                    "-t, --test <path> [<nr>]",
                    "Validate file on relative path <path> with example test of exercise <nr>",
                )
            )
            print('   {:<56} {:<s}'.format("", "Exercise number <nr> is optional"))
        return 1
    elif test == "send":
        if lang == "pl":
            print('Użycie: tichy <send, s, wyslij> <plik> [<nr_zadania>]\n')
            print("Opis:")
            print("Wysyła rozwiązanie o relatywnej ścieżce <path> na sprawdzarkę i wyświetla wynik.")
            print("Numer zadania <nr_zadania> jest opcjonalny.")
        else:
            print('Usage: tichy <send, s, wyslij> <path> [<nr>]\n')
            print("Description:")
            print("Sends answer on relative path <path> to tichy and shows results.")
            print("Exercise number <nr> is optional.")
        return 1
    elif test == "test":
        if lang == "pl":
            print('Użycie: tichy <test, t> <plik> [<nr_zadania>]\n')
            print("Opis:")
            print("Testuje plik o relatywnej ścieżce <plik> przykładowymi danymi zadania <nr_zadania>.")
            print("Numer zadania <nr_zadania> jest opcjonalny.")
        else:
            print('Usage: tichy <test, t> <path> [<nr>]\n')
            print("Description:")
            print("Validate file on relative path <path> with example test of exercise <nr>.")
            print("Exercise number <nr> is optional.")
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


# Sprawdzanie liczby argumentów
def check_for_args(min_number, max_number, help_string):
    if len(args) == (min_number - 1) or args[min_number - 1] in ('--help', '-h', '--pomoc'):
        help_f(help_string)
        sys.exit(1)
    elif len(args) < min_number:
        if lang == "pl":
            print(colored("Za mało argumentów.\n", 'red', attrs=['bold']))
        else:
            print(colored("Too few arguments.\n", 'red', attrs=['bold']))
        help_f(help_string)
        sys.exit(1)
    elif len(args) > max_number:
        if lang == "pl":
            print(colored("Za dużo argumentów.\n", 'red', attrs=['bold']))
        else:
            print(colored("Too many arguments.\n", 'red', attrs=['bold']))
        help_f(help_string)
        sys.exit(1)


# Obsługa błędów wysyłania pliku
def check_for_file(arg_nr, help_string):
    if not os.path.exists(args[arg_nr]):
        if lang == "pl":
            print(colored("Nie znaleziono pliku.\n", 'red', attrs=['bold']))
        else:
            print(colored("File not found.\n", 'red', attrs=['bold']))
        help_f(help_string)
        sys.exit(1)


# Pobieranie od użytkownika numeru zadania
def get_exercise_number(expected):
    if len(args) == expected:
        return args[expected - 1]
    else:
        task_list()
        if lang == "pl":
            exercise_number = input("\nNumer zadania: ")
        else:
            exercise_number = input("\nExercise number: ")
        return exercise_number


# Pobieranie od użytkownika numeru kursu
def get_new_id():
    if len(args) == 4:
        return args[3]
    else:
        open_tichy()
        login()
        open_main_page()
        course_list()
        if lang == "pl":
            new_id = input("\nNowe ID kursu: ")
        else:
            new_id = input("\nNew course ID: ")
        return new_id


# Pobieranie od użytkownika nowej nazwy użytkownika
def get_new_username():
    if len(args) == 3:
        return args[2]
    else:
        if lang == "pl":
            new_username = input("Nowy login: ")
        else:
            new_username = input("New username: ")
        return new_username


# Pobieranie od użytkownika nowego hasła
def get_new_password():
    if len(args) == 3:
        return args[2]
    else:
        if lang == "pl":
            new_password = getpass.getpass(prompt="Nowe hasło: ")
        else:
            new_password = getpass.getpass(prompt="New password: ")
        return new_password


# Wyświetlanie listy kursów
def course_list():
    kursy_response = br.response().read()
    soup = BeautifulSoup(kursy_response, "html.parser")
    kurs_body = soup.find("ul", {"class": "course-list"})
    kurs_list = kurs_body.findAll('li')
    # print (kurs_list[0].get_text(strip=True))
    if lang == "pl":
        print("[  ]Pobieranie listy kursów...")
        print(f"[{OK}]Pobrano pomyślnie.\n")
        print(colored("Dostępne kursy:", attrs=['bold']))
    else:
        print("[  ]Downloading course list...")
        print(f"[{OK}]Downloaded successfully.\n")
        print(colored("Available courses:", attrs=['bold']))
    for i, li in enumerate(kurs_list, start=1):
        print(f'[{i}] ' + li.get_text(strip=True))


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
            f'[{temp_course_id}] ' + kurs_list[temp_course_id - 1].get_text(strip=True)
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


# Zwracanie nazwy zadania oraz jego linku
def get_exercise(ex_number):
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

    return zadanie, zad_name


# Otwieranie strony zadania
def open_exercise(exercise):
    if lang == "pl":
        print("[  ]Otwieranie strony zadania " + exercise[1] + "...")
    else:
        print("[  ]Opening exercise " + exercise[1] + "...")
    br.open(exercise[0])
    if lang == "pl":
        print(f"[{OK}]Otworzono zadanie " + exercise[1] + ".")
    else:
        print(f"[{OK}]Successfully opened exercise " + exercise[1] + ".")


# Testowanie z przykładowymi danymi
def exercise_test(ex_number, plik):
    exercise = get_exercise(ex_number)
    open_exercise(exercise)
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
    for idx, inp in enumerate(inputs):
        result = subprocess.run(['a.exe'], capture_output=True, text=True, input=inp)
        print("Przykładowe dane " + str(idx + 1) + ": ", end="")
        if " ".join(result.stdout.split()) == " ".join(outputs[idx].split()):
            print(colored("zaliczone", 'green', attrs=['bold']))
        else:
            print(colored("niezaliczone", 'red', attrs=['bold']))


# Wysyłanie pliku
def send_file(ex_number, plik):
    exercise = get_exercise(ex_number)
    open_exercise(exercise)
    req = br.click_link(text='Wyślij rozwiązanie')
    if lang == "pl":
        print("[  ]Wysyłanie rozwiązania zadania " + exercise[1] + "...")
    else:
        print("[  ]Sending answer of exercise " + exercise[1] + "...")
    br.open(req)
    br.select_form(nr=0)
    with open(plik, 'r') as file:
        data = file.read()
    answer = br.form.find_control("src")
    answer.value = str(data)
    br.submit()
    if lang == "pl":
        print(f"[{OK}]Wysłano rozwiązanie.")
    else:
        print(f"[{OK}]Sent.")
    link_to_exercise = br.geturl()
    validating = True
    if lang == "pl":
        print("[  ]Oczekiwanie na wyniki...")
    else:
        print("[  ]Waiting for results...")
    while validating:
        validating = False
        time.sleep(0.5)
        br.open(link_to_exercise)
        response = br.response().read()
        soup = BeautifulSoup(response, "html.parser")
        for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
            tds = tr.findAll('td')
            if tds[1].text.strip() == 'Sprawdzany':
                validating = True
    if lang == "pl":
        print(f"[{OK}]Otrzymano wyniki.\n")
    else:
        print(f"[{OK}]Results received.\n")

    br.open(link_to_exercise)
    response = br.response().read()
    soup = BeautifulSoup(response, "html.parser")
    results = []
    for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
        tds = tr.findAll('td')
        results.append(tds[1].text.strip())

    max_status_len = max(len(r) for r in results)
    print(f'ID | {"Result":<{max_status_len}} | {"Time (s)":<15} | Memory (kB)')
    row_format = (
        f'{{:>2}} | {{:<{max_status_len+13}}} | {{:<6s}} / {{:<6s}} | {{:>s}} / {{:>s}}'
    )

    for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
        tds = tr.findAll('td')
        if tds[1].text.strip() != "Zaliczone":
            status = colored(tds[1].text.strip(), 'red', attrs=['bold'])
        else:
            status = colored(tds[1].text.strip(), 'green', attrs=['bold'])

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


def file_encrypt(key, file_path):
    f = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    with open(file_path, 'wb') as file:
        file.write(encrypted)


def file_decrypt(key, file_path):
    f = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    with open(file_path, 'wb') as file:
        file.write(decrypted)

if __name__ == '__main__':
    colorama.init(strip=False)
    global OK
    OK = colored("OK", 'green', attrs=['bold'])
    global args
    args = sys.argv

    user_config_dir = str(Path.home()) + "/.config/new-tichy"
    user_config = user_config_dir + "/config.ini"
    key_path = user_config_dir + "/.key"
    # Sprawdzanie istnienia pliku konfiguracyjnego
    # if not os.path.exists("config.ini"):
    if not os.path.exists(user_config):
        print(
            "It seems it's your first time using tichy script. You have"
            " to set your config to proceed.\n"
            "Wygląda na to, że używasz skryptu tichy po raz"
            " pierwszy. Musisz wprowadzić swoje dane logowania, żeby"
            " kontynuować.\n"
            "Choose your language. Wybierz język.\n"
            "[pl] polski\n[en] english"
        )
        lang = input()
        if lang == "pl":
            usr = input("Twój login: ")
            psw = getpass.getpass(prompt="Twoje hasło: ")
        else:
            usr = input("Your username: ")
            psw = getpass.getpass(prompt="Your password: ")
        key = Fernet.generate_key()
        with open(key_path, 'wb') as mykey:
            mykey.write(key)
        with open(user_config, "w") as f:
            f.write("[CONFIG]\n")
            f.write("username = " + usr + '\n')
            f.write("password = " + psw + '\n')
            f.write("course_id = \n")
            f.write("language = " + lang)
        file_encrypt(key, user_config)

        if lang == "pl":
            print(f"[{OK}]Teraz możesz już korzystać ze skryptu.")
            print(
                "Nie zapomnij ustawić ID kursu za pomocą komendy 'tichy course --set'!"
            )
        else:
            print(f"[{OK}]Now you can proceed with running a script.")
            print("Don't forget to set course ID, using command 'tichy course --set'!")
        sys.exit(0)

    # Odczytanie danych z konfiguracji
    with open(key_path, 'rb') as mykey:
        key = mykey.read()
    file_decrypt(key, user_config)
    config_object = ConfigParser()
    config_object.read(user_config)
    file_encrypt(key, user_config)

    # Dane
    userinfo = config_object["CONFIG"]
    username = userinfo["username"]
    passwd = userinfo["password"]
    course_id = userinfo["course_id"]
    lang = userinfo["language"]

    # Włączanie przeglądarki
    br = mechanize.Browser()

    # Rozpatrywanie argumentów skryptu
    check_for_args(2, 5, "zero")
    if args[1].startswith("-"):
        if args[1] in ('--list', '-l', '--lista'):
            check_for_args(2, 2, "zero")
            open_tichy()
            login()
            open_main_page()
            course_list()
        elif args[1] in ('--username', '-u', '--login'):
            check_for_args(2, 3, "zero")
            userinfo["username"] = get_new_username()
            if lang == "pl":
                print("[  ]Zapisywanie nowej nazwy użytkownika...")
            else:
                print("[  ]Saving new username...")
            file_decrypt(key, user_config)
            with open(user_config, 'w') as conf:
                config_object.write(conf)
            file_encrypt(key, user_config)
            if lang == "pl":
                print(f"[{OK}]Zapisano pomyślnie")
            else:
                print(f"[{OK}]Saved successfully")
        elif args[1] in ('--password', '-p', '--haslo'):
            check_for_args(2, 3, "zero")
            userinfo["password"] = get_new_password()
            if lang == "pl":
                print("[  ]Zapisywanie nowego hasła...")
            else:
                print("[  ]Saving new password...")
            file_decrypt(key, user_config)
            with open(user_config, 'w') as conf:
                config_object.write(conf)
            file_encrypt(key, user_config)
            if lang == "pl":
                print(f"[{OK}]Zapisano pomyślnie.")
            else:
                print(f"[{OK}]Saved successfully.")
        elif args[1] == '--config' or args[1] == '-c' or args[1] == '--dane':
            check_for_args(2, 2, "zero")
            if lang == "pl":
                print(colored("Zawartość pliku konfiguracji:", attrs=['bold']))
            else:
                print(colored("Contents of config file:", attrs=['bold']))
            file_decrypt(key, user_config)
            f = open(user_config, 'r')
            for p in f:
                if p.startswith('[') or p.endswith(']'):
                    print(colored(p, 'red', attrs=['bold']), end="")
                else:
                    print(p, end="")
            file_encrypt(key, user_config)
        else:
            help_f("zero")

    elif args[1] in ('course', 'kurs', 'c'):
        check_for_args(3, 4, "course")
        if args[2] in ('--list', '-l', '--lista'):
            check_for_args(3, 3, "course")
            open_tichy()
            login()
            open_main_page()
            open_course(int(course_id))
            task_list()
        elif args[2] in ('--view', '-v', '--zobacz'):
            check_for_args(3, 3, "course")
            open_tichy()
            login()
            open_main_page()
            course_find(int(course_id), True)
        elif args[2] == '--set' or args[2] == '-s' or args[2] == '--ustaw':
            check_for_args(3, 4, "course")
            userinfo["course_id"] = get_new_id()
            if lang == "pl":
                print("[  ]Zapisywanie nowego ID kursu...")
            else:
                print("[  ]Saving new course ID...")
            file_decrypt(key, user_config)
            with open(user_config, 'w') as conf:
                config_object.write(conf)
            file_encrypt(key, user_config)
            if lang == "pl":
                print(f"[{OK}]Zapisano pomyślnie.")
            else:
                print(f"[{OK}]Saved successfully.")
        elif args[2] in ('--points', '-p', '--punkty'):
            print("Not implemented yet")
        else:
            help_f("course")
    elif args[1] in ('exercise', 'zadanie', 'zad', 'e'):
        check_for_args(3, 5, "exercise")
        if args[2] in ('--list', '-l', '--lista'):
            check_for_args(3, 3, "exercise")
            print('list')
        elif args[2] in ('--send', '-s', '--wyslij'):
            check_for_args(4, 5, "exercise")
            check_for_file(3, "exercise")
            open_tichy()
            login()
            open_main_page()
            open_course(int(course_id))
            ex_nr = get_exercise_number()
            send_file(ex_nr, args[3])
        elif args[2] in ('--test', '-t'):
            check_for_args(4, 5, "exercise")
            check_for_file(3, "exercise")
            open_tichy()
            login()
            open_main_page()
            open_course(int(course_id))
            ex_nr = get_exercise_number(5)
            exercise_test(ex_nr, args[3])
        else:
            help_f("exercise")
    elif args[1] in ('s', 'send', 'wyslij'):
        check_for_args(3, 4, "send")
        check_for_file(2, "send")
        open_tichy()
        login()
        open_main_page()
        open_course(int(course_id))
        ex_nr = get_exercise_number(4)
        send_file(ex_nr, args[2])
    elif args[1] in ('t', 'test'):
        check_for_args(3, 4, "test")
        check_for_file(2, "test")
        open_tichy()
        login()
        open_main_page()
        open_course(int(course_id))
        ex_nr = get_exercise_number()
        exercise_test(ex_nr, args[2])
