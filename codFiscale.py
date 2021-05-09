import datetime

class CodFiscale:
    
    def __init__(self,cognome, nome,sesso, data_nascita, luogo_nascita):
        self.__cognome=cognome
        self.__nome=nome
        self.__sesso=sesso
        self.__data_nascita=data_nascita
        self.__luogo_nascita=luogo_nascita

    def stampaNome(self):
        return self.__nome
