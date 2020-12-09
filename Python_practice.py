counties = ["Arapahoe","Denver","Jefferson"]
print(counties[0])
my_list = []
print(counties)
counties[0] 
print(counties[2])
len(counties)
counties[0:1]
counties[:2]
counties[1:2]
counties[1:]
counties[1:3]
counties[1:]
counties
counties.append("El Paso")
counties
counties.insert(2,"El Paso")
counties
counties.remove("El Paso")
counties
counties.pop(2)
counties
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
counties_tuple[1]
counties_tuple[:-1]
counties[2] = "El Paso"
counties


counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(2,"El Paso")
counties
counties.remove("Arapahoe")
counties
counties[2] = "Denver"
counties
counties[1] = "Jefferson"
counties
counties.append("Arapahoe")
counties
counties[0] = "El Paso"
counties
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.keys()
counties_dict.get("Denver") 
counties_dict.get("Arapahoe")

voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
#membership operators in 3.2.9
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
#practice logical operators and mempership operators
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list")
#3.2.5
counties = ["Arapahoe","Denver","Jefferson"]
#declare an empty my_list
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(counties_dict)
counties
len(counties)

#create a dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#get the length of a dictionary
len(counties_dict)
#get all the keys and the values
print(counties_dict)
counties_dict.items()
#get all the keys
counties_dict.keys()
#get all the values
counties_dict.values()
#get a specific value
counties_dict.get("Denver")
counties_dict.get("Arapahoe")
counties_dict.get("Jefferson")
#lists of dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
#If Statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
#logical operators 3.2.9
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
# Repetition Statements 3.2.10
#iterate through lists and tuples
county = ["Arapahoe", "Denver", "Jefferson"]
my_list = []
print(counties)
#iterate through a dictionary 3.2.10
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
#get the values of a dictionary
voters = [422829, 463353, 432438]
for voters in counties_dict.values():
    print(voters)
for key, values in counties_dict.items():
    print(county, voters)
    
# Repetition Statements 3.2.10
#iterate through lists and tuples
county = ["arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)
#iterate through a dictionary 3.2.10
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#get the keys of a dictionary
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)   
    
#get the values of a dictionary
voters = [422829, 463353, 432438]
for voters in counties_dict.values():
    print(voters)   
#Get the Key-Value pairs of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)
    
#Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for county_dict in voting_data:
    print(county)
    
#Get the Values from  list of Dictionaries
for counties_dict in voting_data:
    for value in counties_dict.values():
        print(voters)
        
        
        

