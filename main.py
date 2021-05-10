from codFiscale import CodFiscale
from datetime import date as dt

def main():
    f = CodFiscale("Luongo", 'Roberta', 'M', dt.fromisoformat('1968-06-01'), 'Pozzuoli')

    print(f.creaParteCognome()+f.creaParteNome()+f.creaParteData())


if __name__ == "__main__":
    main()
