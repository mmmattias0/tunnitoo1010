"""Matemaatilised tehted"""


import math


# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)


a =float(input("Sisesta kaatet a:"))
b =float(input("Sisesta kaateb b:"))

c = math.sqrt(a**2 + b**2)

ümbermõõt = a + b + c

pindala = 0.5 * a * b

c = round(c, 2)
ümbermõõt = round(ümbermõõt, 2)
pindala = round(pindala, 2)

print(f"hüpotenuus c: {c}")
print(f"ümbermõõt: {ümbermõõt}")
print(f"pindala: {pindala}")
