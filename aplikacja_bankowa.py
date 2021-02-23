import zmq

login = input("Login: ")
haslo = input("Hasło: ")

context = zmq.Context()

print("Łączenie z serwerem ...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Wysyłanie zapytania do serwera ...")

socket.send(b"banklogin %s %s " % (bytes(login, 'cp1252'),bytes(haslo, 'cp1252')))

#  Get the reply.
message = socket.recv()
if(message != b"blad"):
    print("Zalogowano!")
    operacja = input("Jaką operację chcesz wykonać? (1- zmiana_pinu, 2- nowy_uzytkownik): ")
    if(operacja == "1"):
        konto = input("Podaj nr konta: ")
        nowy_pin = input("Podaj nowy pin: ")
        print()
        socket.send(b"zmiana_pinu %d %d " % (int(konto), int(nowy_pin)))
        message = socket.recv()
        print(message.decode("cp1252"))
    elif(operacja == "2"):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        pesel = input("Podaj pesel: ")
        saldo = input("Podaj wkład wstępny: ")
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        pin = input("Podaj pin: ")
        socket.send(b"nowy_uzytkownik %s %s %d %d %s %s %d " % (bytes(imie, 'cp1252'),bytes(nazwisko, 'cp1252'),int(pesel),int(saldo),bytes(login, 'cp1252'),bytes(haslo, 'cp1252'),int(pin)))
        message = socket.recv()
        print(message.decode("cp1252"))
else:
    print("Błędne dane!")