def concat(s1: str,s2: str):
    return s2 + s1

def repeat(s: str,n: int):
    return s * n

def reverse(s: str):
    return s[::-1]

def extract(s: str, i: int, j: int):
    return s[i:j+1]

def replace(s: str, sub: str, new_sub)->str:
    return s.replace(sub, new_sub, 1)

def main():
    print("\n---Concatenare: ---")
    print(concat("abc","012"))
    print(concat("345","gij"))
    print(concat("x1y1","abc"))
    
    print("\n---Repetarea---")
    print(repeat("x1y1y2",4))
    print(repeat("abcd",2))
    print(repeat("123",5))
    
    print("\n---Inversare: ---")
    print(reverse("ABC"))
    print(reverse("1a2b3c"))
    print(reverse("x3abc"))
    
    print("\n---Extractie: ---")
    print(extract("12345", 1, 3))
    print(extract("abcdefg", 2,5))
    print(extract("x1y1x5y5x4",0,3))
    
    print("\n---Inlocuire: ---")
    print(replace("x1y1x2y2","y2x3","123"))
    print(replace("abcdefg","def","xyz"))
    print(replace("1234567","2345","abcd"))
    
if __name__ == "__main__":

    main()
