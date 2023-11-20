# Creating a dictionary.

# Create a function called make_country, which takes in a country’s name and capital as parameters. 
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
# Make the function print out the values of the dictionary to make sure that it works as intended.
capitals = dict()
def my_county(**countries):
    for key, value in countries.items():
        print(key)
        print(value)
        capitals.update(countries)
        

my_county(Ukraine = "Kyiv", Poland = "Warsaw", France = "Paris")
print(capitals)