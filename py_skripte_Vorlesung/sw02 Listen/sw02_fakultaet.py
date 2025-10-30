def factorial(n): # Fakultät
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))
    
faku = factorial(4)
print("Ergebnis", faku)
