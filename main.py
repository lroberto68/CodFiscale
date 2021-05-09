from codFiscale import CodFiscale

def main():
    print(__name__)
    f=CodFiscale('Luongo','Roberto','M','1968-06-01','Pozzuoli')
    print(f.stampaNome())

if __name__=="__main__":
    main()