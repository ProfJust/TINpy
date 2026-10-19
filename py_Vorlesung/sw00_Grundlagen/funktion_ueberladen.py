"""int verdoppeln(int x) {
    return x * 2;
}

double verdoppeln(double x) {
    return x * 2;
}
"""


def verdoppeln(x):
    return x * 2


print(verdoppeln(5))
print(verdoppeln(2.5))
print(verdoppeln("Hallo"))


def addiere(x, y=0):
    return x + y


print(addiere(5))
print(addiere(5, 10))