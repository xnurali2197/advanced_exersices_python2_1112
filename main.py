print("5.")
name = input("5. Enter a name: ").strip()
name_lower = name.lower()
if name_lower in ("ali", "vali", "soli"):
    print("5. This is my friend")
elif len(name) > 5:
    print("5. Person with a long name")
else:
    print("5. I don't know them")

print("6.")
age_input = input("6. Enter your age: ").strip()
genre = input("6. Enter movie genre (comedy, thriller, sci-fi): ").strip().lower()
try:
    age = int(age_input)
except Exception:
    age = None
if age is None:
    print("6. Invalid age")
else:
    if age > 18 and genre == "thriller":
        print("6. Movie suitable for you")
    elif age < 12 and genre == "thriller":
        print("6. Not for you")
    else:
        print("6. Movie is available")

print("7.")
price_input = input("7. Enter product price: ").strip()
promo = input("7. Enter promo code (if any): ").strip()
try:
    price = float(price_input)
except Exception:
    price = None
if price is None:
    print("7. Invalid price")
else:
    if price > 50 and promo.upper() == "SALE":
        print("7. 20% discount applied")
    else:
        print("7. No discount")

print("8.")
dist_input = input("8. Enter distance (km): ").strip()
time_input = input("8. Enter time (hours): ").strip()
try:
    dist = float(dist_input)
    t = float(time_input)
except Exception:
    dist = None
    t = None
if dist is None or t is None:
    print("8. Invalid distance or time")
else:
    if dist < 10 or t > 1:
        print("8. Bicycle is suitable")
    elif dist > 10 and t < 1:
        print("8. Car is suitable")
    else:
        print("8. Walk")
