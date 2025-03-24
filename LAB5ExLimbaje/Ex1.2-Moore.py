def automat_moore(intrari):
    stare_curenta = "S0"
    print(f"Stare inițială: {stare_curenta}")

    while intrari:
        intrare = intrari.pop(0)
        stradaA, stradaB = intrare
        iesire = None

        if stare_curenta == "S0":
            iesire = 0
        elif stare_curenta == "S1":
            iesire = 1

        print(f"Intrare: {intrare}, Stare curentă: {stare_curenta}, Ieșire: {iesire}")

        if stare_curenta == "S0":
            if stradaA == 0 and stradaB == 0:
                stare_curenta = "S0"
            elif stradaA == 0 and stradaB == 1:
                stare_curenta = "S1"
            elif stradaA == 1 and stradaB == 0:
                stare_curenta = "S0"
            elif stradaA == 1 and stradaB == 1:
                stare_curenta = "S1"

        elif stare_curenta == "S1":
            if stradaA == 0 and stradaB == 0:
                stare_curenta = "S0"
            elif stradaA == 0 and stradaB == 1:
                stare_curenta = "S1"
            elif stradaA == 1 and stradaB == 0:
                stare_curenta = "S1"
            elif stradaA == 1 and stradaB == 1:
                stare_curenta = "S0"

    if stare_curenta == "S0":
        iesire = 0
    elif stare_curenta == "S1":
        iesire = 1
    print(f"Stare finală: {stare_curenta}, Ieșire: {iesire}")

def main():
    intrari = [(0, 1), (1, 0), (1, 1), (0, 0)]
    automat_moore(intrari)

if __name__ == "__main__":
    main()
