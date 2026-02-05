def zweiteFunktion(my_string):
    print(my_string)
    print_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


# zweiteFunktion("Hello World")
def Strophe():
    print(i+1, "te Strophe")  # nutzt globalen Wert i
    print("Spam, " * 4) 
    print("Spam, " * 4)
    print("Spam, " * 2)
    print("(Lovely Spam, Wonderful Spam!)")
    print("Spam, " * 2)

# Hauptprogramm main
for i in range(6):
    Strophe()
