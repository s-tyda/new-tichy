import re
import mechanize
import time
from bs4 import BeautifulSoup
import sys

from termcolor import colored

#linki
kurs = "https://tichy.umcs.lublin.pl/course/2ae9322bea1944e59a218708cfa9a793/"

#wczytaj rozwiazanie z pliku

if len(sys.argv) != 3:
        print("Uzycie:", sys.argv[0], "<nr zadania> <nazwapliku.cpp>")
        exit(0)
with open(sys.argv[2], 'r') as file:
   data = file.read().replace('\n', '\n  ')
#print(str(data))
# przygotuj dane do logowania z pliku
f = open("tichy_dane.txt")
dane = f.readlines()

br = mechanize.Browser()
br.open("https://tichy.umcs.lublin.pl/accounts/login/")
print(br.title())
# zaloguj uzytkownika na sprawdzarce
br.select_form(nr=0)
control = br.form.find_control("username")
control.value = dane[0]
control = br.form.find_control("password")
control.value = dane[1]
response = br.submit()
# kliknij w odpowiedni kurs
br.open(kurs)
print("Zalogowano na kurs: " + br.title())
zadania_response = br.response().read()

soup = BeautifulSoup(zadania_response, "html.parser")
nrzadania = sys.argv[1]
zadanie = ""
found = False
for tr in soup.find("table", {"class": "table table-striped"}).find('tbody').findAll('tr'):
    tds = tr.findAll('td')
    if nrzadania == tds[0].text:
        found = True
        el = tds[1].find('a')['href']
        zadanie = 'https://tichy.umcs.lublin.pl' + el
        

if found == False:
    print("Nie znaleziono zadania nr: " + nrzadania)
    exit(0)

br.open(zadanie)
print("Otwarto zadanie: " + br.title())
req = br.click_link(text='Wyślij rozwiązanie')
br.open(req)
print(" " + br.title())
br.select_form(nr=0)
rozwiazanie = br.form.find_control("src")
rozwiazanie.value = str(data)
response = br.submit()
linkDoRozwiazania = br.geturl()
sprawdzany = True
while sprawdzany == True:
    sprawdzany = False
    time.sleep(0.5)
    br.open(linkDoRozwiazania)
    response = br.response().read()
    soup = BeautifulSoup(response, "html.parser")
    for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
        tds = tr.findAll('td')
        if tds[1].text.strip() == 'Sprawdzany':
            sprawdzany =True

br.open(linkDoRozwiazania)
response = br.response().read()

soup = BeautifulSoup(response, "html.parser")

for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
    tds = tr.findAll('td')
    uid=tr.attrs['id'][3:]
    if(tds[1].text.strip() != "Zaliczone"):
        print( "id testu: " + tds[0].text + " | " + colored(tds[1].text.strip(), 'red', attrs=['bold']))
    else:
        print("id testu: " + tds[0].text + " | " + colored(tds[1].text.strip(), 'green', attrs=['bold']))
    print("rozmiar: " + tds[2].text.strip())
    print("czas: " + tds[3].text.strip() + " / " + str(float(tds[4].text.strip()[:-2].replace(',', '.'))) + " s")
    print("pamięć: " +tds[5].text.strip() + " / " + str(int(tds[6].text.strip()[:-3])) + " kB")
    print('----------------')
