from codFiscale import CodFiscale

def main():
    
    f=CodFiscale("Luongo",'Roberto','M','1968-06-01','Pozzuoli')
    
    print(f.CreaParteCognome())

if __name__=="__main__":
    main()