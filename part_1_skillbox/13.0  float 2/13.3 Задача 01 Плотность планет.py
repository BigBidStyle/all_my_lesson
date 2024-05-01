vFirstPlanet = 1.43128e15
vSecondPlanet = 6.254e13
pEarth = 5.5153e12

mFirstPlanet = float(input("Масса первой планеты: "))
mSecondPlanet = float(input("Масса второй планеты: "))

pFirstPlanet = mFirstPlanet / vFirstPlanet
pSecondPlanet = mSecondPlanet / vSecondPlanet

print(f"Плотность первой планеты: {pFirstPlanet}")
print(f"Плотность второй планеты: {pSecondPlanet}")

if abs(pEarth - pFirstPlanet) < abs(pEarth - pSecondPlanet):
    print("Плотность первой планеты ближе к плотностти Земли.")
else:
    print("Плотность второй планеты ближе к плотности Земли.")