from codfisc.codFiscale import CodFiscale

from datetime import date as dt

def main():
    f = CodFiscale("Luongo", 'Roberto', 'M', dt.fromisoformat('1968-06-01'), 'Pozzuoli')

    print(f.creaParteCognome()+f.creaParteNome()+f.creaParteData() + f.creaParteLuogo() + f.creaCin())
    print(f"Il codice fiscale è: \033[32m{f.stampaCF()}")

if __name__ == "__main__":
    main()
