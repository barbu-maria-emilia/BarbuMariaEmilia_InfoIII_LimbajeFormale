A={"a","b","c"}
B={"x","y","z"}
C={1,2,3}

def concatenare(s1,s2):
    return str(s1)+str(s2)

def inversare(s):
    return str(s)[::-1]

def substitutie(s,a,b):
    return s.replace(a,b) if a !=b else s

def lungime(s):
    return len(s)

def main(): 
   print("---Concatenare: ---")
   print(concatenare("a","x"))
   print(concatenare("y",3))
   print(concatenare(1,"b"))
   
   print("\n---Inversarea: ---")
   print(inversare("123"))
   print(inversare("by2"))
   print(inversare("ax1"))

   print("\n---Substitutie: ---")
   print(substitutie("c1ac2a", "a", "b"))
   print(substitutie("bcxb3", "b", "z"))
   print(substitutie("aca2an3", "a", "x"))
   
   print("\n---Lungimea: ---")
   print(lungime("abc123"))
   print(lungime("123"))
   print(lungime("ax1by2cz3"))
   
if __name__ == "__main__":
    main()
