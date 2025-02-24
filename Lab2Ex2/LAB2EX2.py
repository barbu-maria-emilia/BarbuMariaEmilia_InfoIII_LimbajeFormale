def verificare(sir):
    stare_initiala = "q0"
    stare_finala = "q3"
    stare_curenta = stare_initiala
    
    print(f"Stare initiala: {stare_curenta}")
    
    for char in sir:
        print(f"Caracter citit: '{char}',Stare curenta: {stare_curenta}")
        
        if stare_curenta == "q0":
            if char == 'c':
                stare_curenta = "q1"
                
        elif stare_curenta == "q1":
            if char == 'a':
                stare_curenta = "q2"
            elif char == 'c':
                stare_curenta = "q1"
            else:
                stare_curenta = "q0"
                
        elif stare_curenta == "q2":
            if char == 't':
                stare_curenta = stare_finala
                print(f"Stare finala: {stare_finala} (Cuvantul 'cat' detectat!)")
                return True
            elif char == 'c':
                stare_curenta = "q1"
            else:
                stare_curenta = "q0"
                
    print(f"Nu am gasit in starea finala {stare_finala}.")
    return False

def main():
    
    sir = input("Introduceti un sir de caractere: ")
    
    if verificare(sir):
        print("Cuvantul 'cat' a fost detectat in sir!")
    else:
        print("Cuvantul 'cat' nu a fost gasit in sir.")
        
if __name__ == "__main__":
    main()
        