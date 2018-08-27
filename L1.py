import math
import random

random.seed(0)

ROWS = 1000

AGENT = "Z"

print("Top Speed, Brand, Price, Colour, Approved")
for i in range(ROWS):
    topSpeed = math.floor(random.uniform(120, 200))
    brand = random.choice(["Limo", "BMW", "Rolls-Royce",  "Rolls-Royce"])
    price = 1000*math.floor(random.uniform(50, 200))
    if brand=="Limo":
        price = price*1.5
    colour = random.choice(["Green", "Blue", "Red", "Black", "Black",  "Pink"])
    
    approved = "No"
    if AGENT=="J":
        if brand == "Rolls-Royce":
            approved = "Yes"
    if AGENT=="K":
        if topSpeed>180:
            approved = "Yes"
    if AGENT=="X":
        if colour=="Black" and price>130000:
            approved = "Yes"
    if AGENT=="Y":
        if colour=="Pink" or topSpeed>160:
            approved = "Yes"
    if AGENT=="Z":
        if brand=="BMW" or (topSpeed>160 and price>150000):
            approved = "Yes"
    
    print(str(topSpeed) + "," + str(brand) + "," + str(price) + "," + str(colour) + "," + str(approved))
    
