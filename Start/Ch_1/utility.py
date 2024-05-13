# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates the use of the any, all, and sum functions
import json

values = [0, 1, 2, 3, 4, 5]
value =[1,2,3,4,5,6]
# TODO: any() can be used to see if any value in a sequence is True
print("1:",any(values))
print("2:",any(value))
if any(num == 3 for num in values):
    print("3:",any(values))

# TODO: all() will detect if all of the values in a sequence are True
print("4:",all(values))
print("5:",all(value))
if all(values):
    print("6:",all(values))
# TODO: sum() can be use to add all of the values in a sequence
print("7:",sum(values))



# these utility functions don't have callbacks like min or max,
# but we can use a generator for more fine control

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# TODO: are there any quake reports that were felt by more than 25,000 people?
print("Generator function output:",any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 25000 for quake in data["features"]))

#this above line will work as generator.

# TODO: how many quakes were felt by more than 500 people?
print("Generator function output:",sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 500 for quake in data["features"]))

# TODO: how many quakes had a magnitude of 6 or larger?
print("Generator function output:",sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] >= 6 for quake in data["features"]))