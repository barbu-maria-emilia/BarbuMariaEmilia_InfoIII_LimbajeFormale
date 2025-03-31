def citeste_limbaj(nume):
    sir = input(f"Introdu limbajul {nume}: ")
    limbaj = set(sir.replace(" ", "").split(","))
    return limbaj

def afiseaza_meniu():
    print("\n Meniu: ")
    print("1. Reuniune (L1 ∪ L2)")
    print("2. Intersecție (L1 ∩ L2)")
    print("3. Diferență (L1 - L2)")
    print("4. Concatenare (L1L2)")
    print("5. Produs Cartezian (L1 x L2)")
    print("0. Ieșire")

def main():
    
    print("Operații pe Limbaje Regulate\n")
    L1 = citeste_limbaj("L1")
    L2 = citeste_limbaj("L2")

    while True:
        afiseaza_meniu()
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            print("Rezultat Reuniune:", L1.union(L2))
        elif optiune == "2":
            print("Rezultat Intersecție:", L1.intersection(L2))
        elif optiune == "3":
            print("Rezultat Diferență (L1 - L2):", L1.difference(L2))
        elif optiune == "4":
            concatenare = {x + y for x in L1 for y in L2}
            print("Rezultat Concatenare:", concatenare)
        elif optiune == "5":
            produs_cartezian = {(x, y) for x in L1 for y in L2}
            print("Rezultat Produs Cartezian L1 x L2:", produs_cartezian)
        elif optiune == "0":
            print("Ieșire.")
            break
        else:
            print("Eroare. Încearcă din nou.")

if __name__ == "__main__":
    main()
