def verificare_sir(sir):
    pozitie_initiala = "q0"
    pozitie_finala = "q3"
    pozitia = pozitie_initiala
    for char in sir:
        print(f"Caracter citit: {char}, pozitia: {pozitia}")
        
        if pozitia == "q0":
            if char == "0":
                pozitia = "q1"
            elif char == "1":
                pozitia = "q2"
              
        elif pozitia == "q1":
            if char == "0":
                pozitia = "q3"
            elif char == "1":
                pozitia = "q0"
                
        elif pozitia == "q2":
            if char == "0":
                pozitia = "q1"
            elif char == "1":
                pozitia = "q3"
                
        elif pozitia == "q3":
            break
        
    print(f"Pozitia: {pozitia}")
    
    return pozitia == pozitie_finala
           
def main():
     for sir in ["00", "11", "010", "0100", "101", "110", "001", "100"]:
          print(f"Șirul {sir} este {'Accept' if verificare_sir(sir) else 'Respins'}")

if __name__ == "__main__":
    main()
        