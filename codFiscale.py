import datetime


class CodFiscale:

    def __init__(self, cognome, nome, sesso, data_nascita, luogo_nascita):
        """Costruttore delle clase CodFiscale"""

        self.__cognome = cognome.upper()
        self.__nome = nome.upper()
        self.__sesso = sesso
        self.__data_nascita = data_nascita
        self.__luogo_nascita = luogo_nascita

    def __dividiConsVoc(self, cogNom):
        """Metodo privato per separare consonanti e vocali in Cognoeme / Nome"""

        VOCALI = 'AEIOU'
        parteV = ''
        parteC = ''
        cogNom = cogNom.replace(" ", "")
        cogNom = cogNom.replace("'", "")

        for c in cogNom:
            if c not in VOCALI:
                parteC += c
            else:
                parteV += c
        return parteC, parteV

    def __restaParte(self, consonanti, vocali):
        """Metodo privato per unire Consonanti +Vocali"""

        parte = consonanti + vocali
        parte = (parte.ljust(3, 'X'))[0:3]
        return parte

    def creaParteCognome(self):
        """Metodo publico che restituisce Parte Cognome"""

        parteC, parteV = self.__dividiConsVoc(self.__cognome)
        return self.__restaParte(parteC, parteV)
