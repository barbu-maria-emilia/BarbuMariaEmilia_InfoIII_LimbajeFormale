def automat_mealy(intrari):
    starea_curenta = "S0"
    print(f"Stare initiala: ")
    
    while intrari:
        input = intrari.pop(0)
        stradaA,stradaB = input
        starea_urmatoare = starea_curenta
        iesire = None
        
        if starea_curenta == "S0":
            if stradaA == 0 and stradaB == 0:
                starea_curenta = "S0"
                iesire = 0
            elif stradaA == 0 and stradaB == 1:
                starea_curenta = "S1"
                iesire = 1
            elif stradaA == 1 and stradaB == 0:
                starea_curenta = "S0"
                iesire = 0
            elif stradaA == 1 and stradaB == 1:
                starea_curenta = "S1"
                iesire = 1
                
        elif starea_curenta == "S1":
            if stradaA == 0 and stradaB == 0:
                starea_curenta = "S0"
                iesire = 0
            elif stradaA == 0 and stradaB == 1:
                starea_curenta = "S1"
                iesire = 1
            elif stradaA == 1 and stradaB == 0:
                starea_curenta = "S1"
                iesire = 1
            elif stradaA == 1 and stradaB == 1:
                starea_curenta = "S0"
                iesire = 0
                
        if iesire is not None:
            print(f"Intrare: {input}, Stare curentă: {starea_urmatoare}, Stare următoare: {starea_curenta}, Ieșire: {iesire}")
        else:
            print(f"Intrare invalidă: {input}")
            
def main():
    intrari = [(0, 1), (1, 0), (1, 1), (0, 0), (0, 1)]
    automat_mealy(intrari)
    
    
if __name__ == "__main__":
    main()