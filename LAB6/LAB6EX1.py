def Limbajul1(cuvant):
    i = cuvant.count('0')
    j = cuvant.count('1')
    if '1' in cuvant[:i]:
        return False
    if '0' in cuvant[i:]:
        return False
    if i > j:
        return True
    else:
        return False

def Limbajul2(cuvant):
    i = cuvant.count('a')
    j = cuvant.count('b')
    if 'b' in cuvant[:i]:
        return False
    if 'a' in cuvant[i:]:
        return False
    if i <= j:
        return True
    else:
        return False
    
def Limbajul3(cuvant):
    nr_a = cuvant.count('a')
    nr_b = cuvant.count('b')
    nr_c = cuvant.count('c')
    if nr_a == nr_b and nr_b == nr_c and nr_a > 0:
        if cuvant == 'a' * nr_a + 'b' * nr_b + 'c' * nr_c:
            return True
        else:
            return False
    else:
        return False

def main():
    print("Alege limbajul:")
    print("1. L = { 0^i 1^j | i > j }")
    print("2. L = { a^i b^j | i <= j }")
    print("3. L = { a^n b^n c^n | n > 0 }")

    nr_limbaj = input("Introdu numărul limbajului (1/2/3): ")
    cuvant = input("Introdu cuvântul: ")

    if nr_limbaj == "1":
        rez = Limbajul1(cuvant)
    elif nr_limbaj == "2":
        rez = Limbajul2(cuvant)
    elif nr_limbaj == "3":
        rez = Limbajul3(cuvant)
    else:
        print("Alegere invalidă.")
        return

    if rez:
        print("Cuvântul aparține limbajului.")
    else:
        print("Cuvântul nu aparține limbajului.")

if __name__ == "__main__":
    main()
