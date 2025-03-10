def bauturi():
    stare_initiala = "q0"
    stare_finala = "q4"
    stare_curenta = stare_initiala
    
    comanda =""
    while comanda != "STOP":
        comanda = input("Introduceti comanda de bauturi: ").strip().upper()
        
        if comanda == "STOP":
            print("Automatul de bauturi s-a oprit.\n")
            break
        
        if stare_curenta == stare_initiala:
            if comanda == "C":
                stare_curenta = "q1"
                print(f"Ati selectat: Cafea. Stare curenta = {stare_curenta}\n")   
            elif comanda == "T":
                stare_curenta = "q2"
                print(f"Ati selectat: Ceai. Stare curenta = {stare_curenta}\n")
            elif comanda == "A":
                stare_curenta = "q3"
                print(f"Ati selectat: Cappucino. Stare curenta = {stare_curenta}\n")
            elif comanda == "H":
                stare_curenta = stare_finala
                print(f"Ati primit bautura: Ciocolata calda. Stare finala.Apasa OK pentru a reveni la selecția initiala.")
            elif comanda == "OK":
                print(f"Nu ai selectat nicio bautura! Stare curenta = {stare_curenta}\n")
            else:
                print(f"Nu inteleg aceasta comanda.Introdu C,T,A Sau H.\n")
                
        elif stare_curenta in ["q1","q2","q3"] and comanda == "OK":
            stare_curenta = stare_finala
            print(f"Ati primit bautura!Apasa OK pentru a reveni.")
            
        elif stare_curenta in ["q4", stare_finala] and comanda == "OK":
            stare_curenta = stare_initiala
            print("Revine la starea initiala.Selectati o bautura noua.")
            
        elif stare_curenta in ["q1","q2","q3","q4"]:
            print("Apasa OK pentru a continua.")
                
def main():
    print("\nAutomatul de bauturi este pornit.\n")
    print("Asteapta selectia unei bauturi(stare initiala:q0).\n")
    print("Optiuni: C=Cafea,T=Ceai,A=Cappuccino,H=Ciocolata calda,OK=Confirmare.\n")
    print("Automatul se opreste daca scrii 'STOP'.\n")
    
    bauturi()
    
if __name__ == "__main__":
    main()
    