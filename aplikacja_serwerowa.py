import random
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


## WCZYTYWANIE
def wczytywanie():
    baza_uzytkownikow = open("konta_uzytkownikow","r")
    lista_uzytkownikow = baza_uzytkownikow.readlines()
    baza_uzytkownikow.close()
    return lista_uzytkownikow
def wczytywanie_pracownikow():
    baza_pracownikow = open("konta_pracownikow","r")
    lista_pracownikow = baza_pracownikow.readlines()
    baza_pracownikow.close()
    return lista_pracownikow

## OPERACJE NA KONTACH

def platnosc(nr_karty,wartosc):
    lista_uzytkownikow = wczytywanie()
    for x in range(0, len(lista_uzytkownikow)):
        nr = lista_uzytkownikow[x].split()
        if (int(nr_karty) == int(nr[4])):
            print("Wykonano platnosc karta o nr: ", nr_karty)
            print("Saldo przed operacją: ", nr[5])
            nowe_saldo = int(nr[5]) - int(wartosc)
            lista_uzytkownikow[x] = nr[0] + " " + nr[1] + " " + nr[2] + " " + nr[3] + " " + str(nr_karty) + " " + str(
                nowe_saldo)+" " +nr[6]+" "+nr[7]+" "+nr[8]+ "\n"
            print("Saldo po operacji: ", nowe_saldo, "\n")
            baza = open("konta_uzytkownikow", "w")
            baza.write(''.join(lista_uzytkownikow))
            baza.close()

def bankomat(nr_karty,wartosc):
    lista_uzytkownikow = wczytywanie()
    for x in range(0, len(lista_uzytkownikow)):
        nr = lista_uzytkownikow[x].split()
        if (int(nr_karty) == int(nr[4])):
            print("Wypłata w bankomacie za pomocą karty nr: ", nr_karty)
            print("Saldo przed operacją: ", nr[5])
            nowe_saldo = int(nr[5]) - int(wartosc)
            lista_uzytkownikow[x] = nr[0] + " " + nr[1] + " " + nr[2] + " " + nr[3] + " " + str(nr_karty) + " " + str(
                nowe_saldo)+" " +nr[6]+" "+nr[7]+" "+nr[8]+ "\n"
            print("Saldo po operacji: ", nowe_saldo, "\n")
            baza = open("konta_uzytkownikow", "w")
            baza.write(''.join(lista_uzytkownikow))
            baza.close()

def wplatomat(nr_karty,wartosc):
    lista_uzytkownikow = wczytywanie()
    for x in range(0, len(lista_uzytkownikow)):
        nr = lista_uzytkownikow[x].split()
        if (int(nr_karty) == int(nr[4])):
            print("Wpłata w bankomacie za pomocą karty nr: ", nr_karty)
            print("Saldo przed operacją: ", nr[5])
            nowe_saldo = int(nr[5]) + int(wartosc)
            lista_uzytkownikow[x] = nr[0] + " " + nr[1] + " " + nr[2] + " " + nr[3] + " " + str(nr_karty) + " " + str(
                nowe_saldo)+" "+nr[6]+" "+nr[7]+" "+nr[8]+ "\n"
            print("Saldo po operacji: ", nowe_saldo, "\n")
            baza = open("konta_uzytkownikow", "w")
            baza.write(''.join(lista_uzytkownikow))
            baza.close()

def przelew(nr_konta1,nr_konta2, wartosc):
    lista_uzytkownikow = wczytywanie()
    for x in range(0,len(lista_uzytkownikow)):
        nr = lista_uzytkownikow[x].split()
        if(int(nr_konta1) == int(nr[3])):
            for i in range(0, len(lista_uzytkownikow)):
                nr2 = lista_uzytkownikow[i].split()
                if (int(nr_konta2) == int(nr2[3])):

                    print("Wykonano przelew z konta o nr:",nr_konta1," na konto o nr: ",nr_konta2)
                    print()
                    print("Saldo konta o nr: ",nr_konta1," przed operacją: ",nr[5])
                    print("Saldo konta o nr: ",nr_konta2," przed operacją: ",nr2[5])
                    print()

                    nowe_saldo1 = int(nr[5]) - int(wartosc)
                    nowe_saldo2 = int(nr2[5]) + int(wartosc)

                    lista_uzytkownikow[x] = nr[0]+" "+nr[1]+" "+nr[2]+" "+str(nr_konta1)+" "+nr[4]+" "+str(nowe_saldo1)+" "+nr[6]+" "+nr[7]+" "+nr[8]+"\n"
                    lista_uzytkownikow[i] = nr2[0] + " " + nr2[1] + " " + nr2[2] + " " + str(nr_konta2) + " " + nr2[4] + " " + str(nowe_saldo2)+" "+nr2[6]+" "+nr2[7]+" "+nr2[8]+"\n"
                    print("Saldo konta o nr: ", nr_konta1, " po operacji: ", nowe_saldo1)
                    print("Saldo konta o nr: ", nr_konta2, " po operacji: ", nowe_saldo2)
                    baza = open("konta_uzytkownikow","w")
                    baza.write(''.join(lista_uzytkownikow))
                    baza.close()

def zmiana_pinu(nr_konta,pin):
    lista_uzytkownikow = wczytywanie()
    for x in range(0,len(lista_uzytkownikow)):
        nr = lista_uzytkownikow[x].split()
        if(int(nr_konta) == int(nr[3])):
            print("Zmiana pinu dla nr konta: ", nr_konta)
            print("Pin przed zmianą: ", nr[8])
            lista_uzytkownikow[x] = nr[0] + " " + nr[1] + " " + nr[2] + " " + nr[3] + " " + nr[4] + " " + nr[5]+" " +nr[6]+" "+nr[7]+" "+str(pin)+ "\n"
            print("Pin po zmianie: ", pin, "\n")
            baza = open("konta_uzytkownikow", "w")
            baza.write(''.join(lista_uzytkownikow))
            baza.close()

## TWORZENIE UŻYTKOWNIKA

class Uzytkownicy:
    def __init__(self, imie, nazwisko, pesel, saldo, login, haslo, pin):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.nr_konta = random.randrange(10000000000000000000000000, 99999999999999999999999999)
        self.nr_karty = random.randrange(1000000000000000, 9999999999999999)
        self.saldo = saldo
        self.login = login
        self.haslo = haslo
        self.pin = pin

def tworzenie_uzytkownika(imie,nazwisko,pesel,saldo,login,haslo,pin):
    baza_uzytkownikow = open('konta_uzytkownikow', "a")
    uzytkownik = Uzytkownicy(imie,nazwisko,pesel,saldo,login,haslo,pin)
    baza_uzytkownikow.write(uzytkownik.imie + " " + uzytkownik.nazwisko + " " + str(uzytkownik.pesel) + " " + str(uzytkownik.nr_konta) + " " + str(uzytkownik.nr_karty) + " "+ str(uzytkownik.saldo)+" "+ uzytkownik.login+" "+ uzytkownik.haslo+" "+ str(uzytkownik.pin)+"\n")
    baza_uzytkownikow.close()



while True:
    #  CZEKANIE NA REQUEST
    message = socket.recv()
    print("Otrzymano zgłoszenie: %s" % message)

    #  ODPOCZYNEK
    time.sleep(1)
    message = str(message)
    if(message.startswith("b'login") is True):
        message = str(message).split()
        login = message[1]
        haslo = message[2]

        lista_uzytkownikow = wczytywanie()
        zalogowano = False
        for x in range(0, len(lista_uzytkownikow)):
            nr = lista_uzytkownikow[x].split()
            if(login == nr[6] and haslo == nr[7] ):
                zalogowano = True
                uzytkownik = x
                break
        if(zalogowano is True):
            print("Zalogowano:",login)
            user = lista_uzytkownikow[uzytkownik]
            socket.send(bytes(user, 'cp1252'))
        else:
            socket.send(b"blad")
    elif(message.startswith("b'przelew") is True):
        message = str(message).split()
        konto1 = message[1]
        konto2 = message[2]
        kwota = message[3]
        przelew(konto1,konto2,kwota)
        socket.send(b"Wykonano przelew")
    elif(message.startswith("b'banklogin") is True):
        message = str(message).split()
        login = message[1]
        haslo = message[2]
        lista_pracownikow = wczytywanie_pracownikow()
        zalogowano = False
        for x in range(0, len(lista_pracownikow)):
            nr = lista_pracownikow[x].split()
            if(login == nr[0] and haslo == nr[1] ):
                zalogowano = True
                break
        if(zalogowano is True):
            print("Zalogowano:", login)
            socket.send(b"Zalogowano")
        else:
            socket.send(b"blad")
    elif(message.startswith("b'zmiana_pinu") is True):
        message = str(message).split()
        konto = message[1]
        nowy_pin = message[2]
        zmiana_pinu(konto,nowy_pin)
        socket.send(b"Wykonano zmiane pinu!")
    elif (message.startswith("b'nowy_uzytkownik") is True):
        message = str(message).split()
        imie = message[1]
        nazwisko = message[2]
        pesel = message[3]
        saldo = message[4]
        login = message[5]
        haslo = message[6]
        pin = message[7]
        tworzenie_uzytkownika(imie,nazwisko,pesel,saldo,login,haslo,pin)
        socket.send(b"Utworzono nowego uzytkownika!")