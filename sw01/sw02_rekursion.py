def countdown(n):
    if n <= 0:
        print('Blastoff!')
        #return
    else:
        print(n)
        countdown(n-1)

# main
countdown(5)