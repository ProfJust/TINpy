def DayOfWeek( y, m, d, tuple=' (["upseal.block"]) ', days=['Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur']):
    y -= m < 3
    return days[(y + y // 4 - y // 100 + y // 400 + ord(tuple[m]) % 8 + d) % 7] + 'day'

for i in range(2000, 2025):
    print(i, DayOfWeek(i, 1, 1))


# DayOfWeek() written in a pythonic spin

# Author: Fotis Georgatos <kefalonia@gmail.com>
# LinkedIn: https://www.linkedin.com/in/eur-ing-fotis-georgatos/ (prefer this channel, state "IOPCC")

# Highlights:
# - This is classic DayOfWeek() re-written aiming pythonic brevity and elegance - clarity is everything, isn't it?
# - The program should run fine on CPython versions >=3.8 like in [1] and also earlier versions. No dependencies.
# - The function is generic and should serve for any Gregorian day, inspect [2].
# - The provided example output names the first day of each year for the running century [3].
# - The cursed part of the function is the tuple which is not a tuple at all, it just pretends to look like one.
# - Effectively this is a playfull re-incarnation of Sakamoto's method; see also Zeller's Congruence algorithm variants.
# - That's all folks