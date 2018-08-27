import math
import random

random.seed(0)

ROWS = 1000

CITY= "Detroit"

print("Top Speed, Age, Security Rating, Efficiency Rating, Price")
for i in range(ROWS):
    topSpeed = math.floor(random.gauss(100, 10))
    age = math.floor(1+ random.uniform(0, 5) + random.uniform(0, 2))
    securityRating = math.floor(3 + random.uniform(0, 4) + random.uniform(0, 4))
    efficiencyRating = math.floor(random.uniform(0, 11))
    
    price=3000
    if CITY=="Atlanta":
        price = 2500+30*topSpeed
    if CITY=="Baltimore":
        price = 2000 +200*securityRating-200*age
    if CITY=="Chicago":
        price = 1000 + 50*topSpeed-100*age+40*securityRating+90*efficiencyRating
    if CITY=="Detroit":
        price = 2000 - 80*age+100*securityRating+200*efficiencyRating + random.gauss(0, 400)
    print(str(topSpeed) + "," + str(age) + "," + str(securityRating) + "," + str(efficiencyRating) + "," + str(price))
    
