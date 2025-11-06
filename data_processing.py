import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class DataLoader():
    def __init__(self):
        self.cities = []
    def load_data(self):
        with open(os.path.join(__location__, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.cities.append(dict(r))
        return self.cities


class Table():
    def __init__(self):
        pass
    def filter(self,condition,dict_list):
        temps = []
        for item in dict_list:
            if condition(item):
                temps.append(item)
        return temps
    
    def aggregation(self,aggregation_key, aggregation_function, dict_list):
        temps = []
        for i in dict_list:
            try:
                temps.append(float(i[aggregation_key]))
            except ValueError:
                temps.append(i[aggregation_key])
        return aggregation_function(temps)

loader = DataLoader()
cities = loader.load_data()
table = Table()



# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()


# Print all cities in Germany
print("All cities in Germany")
filter_list = table.filter(lambda x: x["country"] == "Germany",cities)
print(filter_list)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
filter_list = table.filter(lambda x: x["country"] == "Spain" and float(x["temperature"]) > 12  ,cities)
print(filter_list)
print()



# Count the number of unique countries
print("Count the number of unique countries")
list_country = table.aggregation("country", list, cities)
new_list_temp = set(list_country)
newer_list_temp = list(new_list_temp)
print(len(newer_list_temp))
print()

# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany")
filter_list = table.filter(lambda x: x["country"] == "Germany" ,cities)
lists_temp = table.aggregation("temperature", list, filter_list)
new_list_temp = list(map(float, lists_temp))
avg = sum(new_list_temp)/len(new_list_temp)
print(avg)
print()
# Print the max temperature for all the cities in Italy

print("Max temperature for all the cities in Italy")
filter_list = table.filter(lambda x: x["country"] == "Italy" ,cities)
lists_temp = table.aggregation("temperature", list, filter_list)
new_list_temp = list(map(float, lists_temp))
print(max(new_list_temp))
print()



