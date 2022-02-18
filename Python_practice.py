
# Run a Python file in the command line or VS Code.
print("Hello World")

# Perform Calculations.
print(5+2*3)
print(8//5-3)
print(8+22*2-4)
print(16-3/2+7-1)
print(3**3%5)
print(5+9*3/2-4)

print((5+2)*3)
print((8//5)-3)
print(8+(22*(2-4)))
print(16-3/(2+7)-1)
print(3**(3%5))
print(5+(9*3/2-4))
print(5+(9*3/(2-4)))

# Create and add to a list.
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
# to get first item of the list 
counties[0]
# print the statement with 3rd item of the list
print(counties[2])
# print the last time of the list
print(counties[-1])
# find the lenght of a list
len(counties)
# slice lists(find 1st and 2nd items of the list)
counties[0:2]
counties[:2]
# add items to list
counties.append("El Paso")
# print updated list
print(counties)
# specify where to add new item on  the list(to appear 3rd on list)
counties.insert(2,"El Paso")
# print updated list
print(counties)
# remove item from list
counties.remove("El Paso")
# print updated list
print(counties)
# remove last instance of "El Paso" by using pop() method
counties.pop(3)
# print updated list
print(counties)
# change element of the list(Jefferson replaced by El Paso)
counties[2] = "El Paso"
# print updated list
print(counties)


# data structures: Tuples
my_tuple = tuple()
counties_tuple = ("Arapahoe","Denver","Jefferson")
# lenght of a tuple
len(counties_tuple)
# apply indexing and slicing
counties_tuple[1]
counties_tuple[:-2]

# data structures: Dictionaries

# create a dictionary
counties_dict= {}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
# lenght of a dictionary
len(counties_dict)
# get all items of the dictionary
counties_dict.items()
# get all keys of the dictionary
counties_dict.keys()
# get all keys of the dictionary
counties_dict.values()
# get a specifiv value(value of the number of registered voters in Denver County)
counties_dict.get("Denver")
# get number of registered voters in Arapahoe County
counties_dict["Arapahoe"]

# list of dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})


# For the  voting_data list of dictionaries, do the following:
# Add the new county “El Paso” and its registered voters, 461149, to the second position in voting_data.
voting_data.insert(1,{"county":"El Paso","registered_voters": 461149})
# Remove “Arapahoe” and its registered voters from voting_data.
voting_data.pop(0)
# ake “Denver” and its registered voters the third item in voting_data, but keep “Jefferson” and its registered voters as the second item.   
voting_data.pop(1)
voting_data.append({"county":"Denver", "registered_voters": 463353})
# Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# see the output
voting_data

len(voting_data)

#______________________
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("turn on the ac.")
else:
    print("Open the windows.")

#  What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')



# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')




# Membership operators

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso"in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


# Logical Operators

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# exercise
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# iterate through lists and Tuples
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

# iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# get the keys of a dictionary
# get the counties
for county in counties_dict:
    print(county)
# get the keys
for county in counties_dict.keys():
    print(county)

# get values of a dictionary
# using values
for voters in counties_dict.values():
    print(voters)
# using key to reference the value
for county in counties_dict:
    print(counties_dict[county])
# using get() method
for county in counties_dict:
    print(counties_dict.get(county))

# GET  THE KEY-VALUE PAIRS OF A DICTIONARY
for county, voters in counties_dict.items():
    print(county, voters)
# skill-drill
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county," county has ", voters," registered voters.")

# get each dictionary in a list of dictionaries
voting_data = [
                {"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# get values form a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# print  only county name from each directory
for county_dict in voting_data:
    print(county_dict['county'])

# PRINTING FORMATS

# edited code using f string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes/total_votes*100}% of the total votes.")

# using f-strings with dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# multiline f-string
candidate_votes = int(input("How many votes did the candidate get in the election? "))
# 3345 number of votes

total_votes = int(input("What is the total number of votes in the election? "))
# 23123 total votes


message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


