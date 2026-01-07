```mermaid
classDiagram
    class Vektor {
        - werte : list[float]
        - name : str
        + __init__(name="no name", a=0.0, b=0.0, c=0.0)
        + ausgabe() void
        + skalarprodukt(v1: Vektor, v2: Vektor) float
        + __mul__(other: Vektor) float
        + vektorprodukt(other: Vektor) Vektor
        + __pow__(other: Vektor) Vektor
        + vektoraddition(other: Vektor) Vektor
        + betrag() float
        + __add__(other: Vektor) Vektor
    }
