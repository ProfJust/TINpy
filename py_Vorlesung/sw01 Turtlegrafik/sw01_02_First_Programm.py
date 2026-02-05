int a = 2 # Speicherzelle mit Namen a und Wert 2 versehen 
int b = 3 # Speicherzelle mit Namen b und Wert 3 versehen 
int c     # Speicherzelle mit Namen c 

int main() {
	//--- Eingabe ---
	cout << "Eingabe a :";	cin >> a;
	cout << "Eingabe b :";	cin >> b;
	
	//--- Verarbeitung ----
	c = a + b; // Berechnung

	//---- Ausgabe -----
	cout << a << " + " << b << " = " << c << endl;

	system("pause"); //Windows wartet auf Taste	
	return 0;
}
