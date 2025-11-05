import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("all cities in Germany")
for i in cities:
    country = i["country"]
    city = i["city"]
    if country == "Germany":
        print(i,end=", ")
print()
print()
# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C")
for i in cities:
    temperature = float(i["temperature"])
    country = i["country"]
    city = i["city"]
    if country == "Spain" and temperature > 12:
        print(i,end=", ")
print()
print()

# Count the number of unique countries
print("Count the number of unique countries")
temps = []
for i in cities:
    country = i["country"]
    temps.append(country)

tempss = set(temps)
new_temp = list(tempss)
print(len(new_temp))
print()

# Print the average temperature for all the cities in Germany

temps = []
for i in cities:
    temperature = float(i["temperature"])
    country = i["country"]
    city = i["city"]
    if country == "Germany":
        temps.append(temperature)
print("average temperature for all the cities in Germany")
print(sum(temps)/len(temps))
print()

# Print the max temperature for all the cities in Italy

temps = []
for i in cities:
    temperature = float(i["temperature"])
    country = i["country"]
    if country == "Italy":
        temps.append(temperature)
print("max temperature for all the cities in Italy")
print(max(temps))
print()
