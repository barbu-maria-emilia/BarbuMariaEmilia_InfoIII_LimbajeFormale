from collections import Counter

stare_initiala = 'q0'
stare_finala = 'q3'

def generare(stare_curenta,simbol):
    if stare_curenta == 'q0':
        if simbol == 'a':
            return 'q1'
        return 'q0'
    elif stare_curenta == 'q1':
        if simbol == 'b':
            return 'q2'
        return 'q1'
    elif stare_curenta == 'q2':
        if simbol == 'c':
            return 'q2'
        elif simbol == 'd':
            return 'q3'
        return 'q2'
    elif stare_curenta == 'q3':
        return 'q3'

def verificare_cuvant(cuvant):
    stare_curenta = stare_initiala
    nr_litere = Counter(cuvant)
    
    for simbol in cuvant:
        stare_curenta = generare(stare_curenta, simbol)
        if stare_curenta is None:
            return False
        
    litere_duble = sum(1 for numar in nr_litere.values() if numar == 2)
    
    return stare_curenta == stare_finala and litere_duble == 3

def main():
    cuvinte = ['aabbcc', 'aaa', 'bbbaac', 'aabbcd', 'ddbbcc', 'aabbdd']
    for cuvant in cuvinte:
        print(f'Cuvantul "{cuvant}" este acceptat: {verificare_cuvant(cuvant)}')
        
if __name__ == "__main__":
    main()