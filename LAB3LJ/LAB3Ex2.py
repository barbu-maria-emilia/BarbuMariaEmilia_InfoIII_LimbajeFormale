import random

q0 = "Parcare goala"
q1 = "Parcare partial ocupata"
q2 = "Parcare plina"
locuri_parcare = []

def parcheaza():
    global locuri_parcare
    nr_loc = len(locuri_parcare) + 1
    locuri_parcare.append(nr_loc)
    print(f"Masian este parcata pe locul {nr_loc}.")
    
def elibereaza():
    global locuri_parcare
    if locuri_parcare:
        print(f"Masina pleaca de pe locul {locuri_parcare.pop()}.")
    else:
        print("Parcarea este goala!")
        
def determina_stare():
    if len(locuri_parcare) == 0:
        return q0
    elif len(locuri_parcare) > 0:
        return q1

def afisare():
    if locuri_parcare:
        print("Stare parcare: ") 
        for nr_loc in sorted(locuri_parcare):
            print(f"Nr. loc {nr_loc}: Ocupat")
    else:
        print("Parcarea este goala.")
    print(f"Stare curentă: {determina_stare()}\n")
        
def main():
    while True:
      print("Alege o actiune:\n1.Parcare:\n2.Eliberare:\n3.Afisare:\n4.Iesire:\n")
      intrare = input("Introduceti o optiune: ").strip()
    
      if intrare == '1':
        parcheaza()
      elif intrare == '2':
        elibereaza()
      elif intrare == '3':
        afisare()
      elif intrare == '4':
        print("Programul este inchis.")
        break
      else:
        print("Optiune invalida.")
        

if __name__ == "__main__":
    main()
