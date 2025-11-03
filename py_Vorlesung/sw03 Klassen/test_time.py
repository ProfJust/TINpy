from TimeKlasse import Time

#--------------------------------------------------------------------
if __name__ == '__main__':
    start = Time(9, 20, 0)    
    
    dauer = Time(-9, 20, -20)
    print(dauer.is_valid())
    ende = start + dauer

    einstring = str(ende)
    print("ende", einstring)