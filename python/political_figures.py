presidents = {"Abraham Lincoln": 1809, "Andrew Johnson": 1808, "Ulysses S. Grant": 1822, "Lyndon B. Johnson": 1908, "John F. Kennedy": 1917, "Richard Nixon": 1913}
nineteenth_century = 0
twentieth_century = 0
eighteenth_century = 0

for person, year in presidents.items():
    if year in range (1800, 1900):
        eighteenth_century += 1
    elif year in range (1900, 2000):
        nineteenth_century += 1
    else:
        twentieth_century += 1

print("There are " + str(eighteenth_century) + " 18th-c. births and " + str(nineteenth_century)
+ " 19th-c. births and " + str(twentieth_century) + " 20th-c. births in my collection.")
