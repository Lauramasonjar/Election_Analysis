print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] =='Denver':
    print(counties[1])

    counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print("Hello World")

    for county in counties:
        print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for num in range(5):
    print(num)  
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

    
