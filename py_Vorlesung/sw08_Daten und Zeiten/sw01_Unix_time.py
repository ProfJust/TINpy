import time

unix_zeit_jetzt = time.time()

print("Sekunden seit dem 1.1.1970 (UTC)", unix_zeit_jetzt)



# aktuelle Zeit als struct_time (lokale Zeit)
lokale_zeit = time.localtime()
# formatiert ausgeben
zeit_string = time.strftime("%Y-%m-%d %H:%M:%S", lokale_zeit)
print("Aktuelle lokale Zeit:", zeit_string)


t = time.localtime()   # aktuelle lokale Zeit als struct_time
print(t)
