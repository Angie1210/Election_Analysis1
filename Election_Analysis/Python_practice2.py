# #print ("Hello World")
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1



# # #counties_dict = [{"county":"Arapahoe","voters":288973},{"county":"Denver","voters":2873982},{"county":"Jefferson","voters":8717829}]
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# # # # KEYS
# # # for county in counties_dict:
# # #      print(county)
# # # for county in counties_dict.keys():
# # #      print (county)
# # # # #VALUES
# # for x in counties_dict.values():
# #     print (x)
# # 422829
# # 463353
# # 432438

# # for x in counties_dict:
# #      print(counties_dict[x])

# # for county in counties_dict:
# #       print(counties_dict.get(county))

# # PAIRS OF KEYS AN VALUES
# for county, voters in counties_dict.items():
#      print(county, voters)






# get each dictionary in a list of dictionaries

# for x in voting_data:
#        print(x)

# # {'county': 'Arapahoe', 'registered_voters': 422829}
# # {'county': 'Denver', 'registered_voters': 463353}
# # {'county': 'Jefferson', 'registered_voters': 432438}

# for x in range(len(voting_data)):
#      print (voting_data[x])

# {'county': 'Arapahoe', 'registered_voters': 422829}
# {'county': 'Denver', 'registered_voters': 463353}
# {'county': 'Jefferson', 'registered_voters': 432438}

# #GET the values(counties) over the list of dictionaries

# for x in range(len(voting_data)):
#      print (voting_data[x]["county"])
# # # Arapahoe
# # # Denver
# # # Jefferson

# #get the values(registeres_cotes) ove the list of dict
# for x in range(len(voting_data)):
#      print (voting_data[x]["registered_voters"])
# # # 422829
# # # 463353
# # # 432438

#get ALL the VALUES from a list of dictionaries

# for x in voting_data:
#     for y in x.values():
#         print(y)

# Arapahoe
# 422829
# Denver
# 463353
# Jefferson
# 432438 

# for county_dict in voting_data:  
#       print(county_dict.values())
# dict_values(['Arapahoe', 422829])
# dict_values(['Denver', 463353])
# dict_values(['Jefferson', 432438])

# for x in voting_data:    
#     for y in x:      
#         print(y)
    

# # county
# # registered_voters
# # county
# # registered_voters
# # county
# # registered_voters

# for x in voting_data:    

#     for y in x.keys():      

#         print(y)

# Arapahoe
# 422829
# Denver
# 463353
# Jefferson
# 432438

# for county_dict in voting_data:

#      print(county_dict['registered_voters'])

# 422829
# 463353
# 432438

# for county_dict in voting_data:

#      for key, value in county_dict.items():

#           print(key, value)

# # county Arapahoe
# # registered_voters 422829
# # county Denver
# # registered_voters 463353
# # county Jefferson
# # registered_voters 432438

# for county_dict in voting_data:

#      for key, value in county_dict.items():

#          print(value)

# Arapahoe
# 422829
# Denver
# 463353
# Jefferson
# 432438
# for county_dict in voting_data:
#     print(county_dict['county'])
# Arapahoe
# Denver
# Jefferson

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# # message_to_candidate = (
# #     f"You received {candidate_votes} number of votes. "
# #     f"The total number of votes in the election was {total_votes}. "
# #     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# # print(message_to_candidate)
# # You received 3345 number of votes. The total number of votes in the election was 23123. You received 14.466115988409808% of the total votes.

# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

# for x in range(len(voting_data)):
#     print(f'{voting_data[x]["county"]} county has {voting_data[x]["registered_voters"]} registered voter')
    

#         #for y in x.values():
#        # print (voting_data[y])
import csv
dir (csv)

