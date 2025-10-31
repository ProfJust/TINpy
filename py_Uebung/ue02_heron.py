def w(n , x):
    if n==0:
        return 1
    if n>=1:
        return 1/2*(w(n-1, x) + x/w(n-1, x) )
    
# main
x  = int(input("Geben Sie x ein "))
n  = int(input("Geben Sie n ein "))
print("Ergebnis: ", w(n,x))
