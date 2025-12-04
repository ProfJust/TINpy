from datetime import time
from datetime import datetime

# time ist ein Teil von datetime
jetzt = datetime.now()      # Datum + Uhrzeit
uhrzeit = jetzt.time()      # nur die Uhrzeit
print("Aktuelle Uhrzeit:", uhrzeit)

# time(hour, minute, second)
t2 = time(14, 30, 0)
print("Nachmittags:", t2)           # 14:30:00

# time(hour, minute, second, microsecond)
t3 = time(23, 59, 59, 123456)
print("Fast Mitternacht:", t3)      # 23:59:59.123456

# Attribute auslesen
print("Stunde:", t2.hour)
print("Minute:", t2.minute)
print("Sekunde:", t2.second)

