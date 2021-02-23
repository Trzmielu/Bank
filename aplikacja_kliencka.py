import zmq

login = input("Login: ")
haslo = input("Hasło: ")

context = zmq.Context()

print("Łączenie z serwerem ...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Wysyłanie zapytania do serwera ...")

socket.send(b"login %s %s " % (bytes(login, 'cp1252'),bytes(haslo, 'cp1252')))

#  Get the reply.
message = socket.recv()
if(message != b"blad"):
    print("Zalogowano!")
    lista_uzytkownikow = message
    nr = lista_uzytkownikow.split()


    operacja = input("Jaką operację chcesz wykonać? (1- przelew, 2- stan konta): ")
    if(operacja == "1"):
        konto = input("Podaj numer konta: ")
        kwota = input("Podaj kwotę: ")
        print()
        socket.send(b"przelew %d %d %d " % (int(nr[3]),int(konto),int(kwota)))
        message = socket.recv()
        print(message.decode("cp1252"))
    elif(operacja == "2"):
        print("Twój stan konta to: ",nr[5].decode("cp1252") )
    else:
        print("Błąd!")
else:
    print("Błędne dane!")
