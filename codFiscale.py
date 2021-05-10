from datetime import date as dt


class CodFiscale:

    def __init__(self, cognome, nome, sesso, dataNascita, luogoNascita):
        """Costruttore delle clase CodFiscale"""

        self.__cognome = cognome.upper()
        self.__nome = nome.upper()
        self.__sesso = sesso
        self.__dataNascita = dataNascita
        self.__luogoNascita = luogoNascita

    def __dividiConsVoc(self, cogNom):
        """Metodo private per separare consonanti e vocali in Cognoeme / Nome"""

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
        """Metodo private per unire Consonanti +Vocali"""

        parte = consonanti + vocali
        parte = (parte.ljust(3, 'X'))[0:3]
        return parte

    def creaParteCognome(self):
        """Metodo public che restituisce Parte Cognome"""

        parteC, parteV = self.__dividiConsVoc(self.__cognome)
        return self.__restaParte(parteC, parteV)

    def creaParteNome(self):
        """Metodo public che restituisce Parte Nome"""

        parteC, parteV=self.__dividiConsVoc(self.__nome)
        l= len(parteC)

        if l>=4:
             parteC=parteC[0:1]+parteC[2:3]+parteC[3:4]
             return parteC

        return self.__restaParte(parteC, parteV)

    def creaParteData(self):
        """Metodo public che restituisce Parte Data"""

        tbMese={'Jan':'A','Feb':'B','Mar':'C','Apr':'D','May':'E','Jun':'H','Jul':'L','Aug':'M','Sep':'P','Oct':'R','Nov':'S','Dec':'T'}
        
        if self.__sesso=='F':
            gg=40
        elif self.__sesso=='M':
            gg=0
        
        giorno=int(self.__dataNascita.strftime('%d'))+gg
        parteData=self.__dataNascita.strftime('%y')+tbMese[self.__dataNascita.strftime('%b')]+ str(giorno).rjust(2,'0')
        
        return parteData