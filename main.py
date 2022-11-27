# Goal:
# get the Cartesian product (every possible combination of values) from a group of lists

# Source: https://stackoverflow.com/questions/533905/how-to-get-the-cartesian-product-of-a-series-of-lists

# How can I get the Cartesian product (every possible combination of values) from a group of lists?

# Input:

# somelists = [
#    [1, 2, 3],
#    ['a', 'b'],
#    [4, 5]
# ]

# Desired output:

# [(1, 'a', 4), (1, 'a', 5), (1, 'b', 4), (1, 'b', 5), (2, 'a', 4), (2, 'a', 5), ...]

# li = [1, 2, 3, 3, 1] #beginning list
# print(li)
# lis = set(li) # remove all dups by typecasting a list as a set
# print(lis) #typecast back as a list
# li = list(lis)
# print(li)
# # tests = set()
# # print(tests)

#Input
# somelists = [
   # [1, 2, 3, 3, 2, 1],
   # ['a', 'b'],
   # [4, 5, 6, 4]
 # ]
# somelists = [["Mary", "The rock climber", "Piggy on the railway"],
#              ["went", "ate", "wrote"],
#              ["to the market", "a pie", "a poem"]
#             ]
# somelists= [
#   ["eyes", "hands", "tongue", "cheek", "lips", "brows", "forehead", "eyelids", "chin", "ears"],
#   ["of", "for", "by", "on", "at", "in"],
#   ["gods", "men", "beasts", "ghosts", "birds", "flowers", "sky", "rivers", "seas"]
# ]
# somelists= [
#   ["romeo", "othello", "hamlet", "caesar","macbeth"],
#   ["loves", "hates", "kills", "slaps", "pays", "kicks", "begs", "woos", "dyes", "paints"],
#   ["juliette", "ophelia", "brutus", "cassius", "iago", "desdemona" ]
# ]
# somelists = [
#  ["oggy", "cockroach1", "cockroach2", "cockroach3"],
#  ["oggy", "cockroach1", "cockroach2", "cockroach3"],  
#  ["oggy", "cockroach1", "cockroach2", "cockroach3"]  
#   # [],
#   # []
# ]

somelists = [
 ["cinderella", "prince charming", "stepmother", "stepsisters", "mice", "fairy godmother", "carriage people", "father", "mother"],
  ["cinderella", "prince charming", "stepmother", "stepsisters", "mice", "fairy godmother", "carriage people", "father", "mother"],
["cinderella", "prince charming", "stepmother", "stepsisters", "mice", "fairy godmother", "carriage people", "father", "mother"]
]
somelists1 = []
# print(somelists)
# cleanup - remove duplicates if any, from the input lists
for l in somelists:
  # print(l)
  ls = set(l)
  # print(ls)
  l = list(ls)
  # print(l)
  # print("------")  
  somelists1.append(l)
# print(somelists)
# print(somelists1)
somelists = somelists1
# print(somelists)
  # print(f"{l} {ls} {ll} {l}")  
# print(somelists)  

# cartesian product of the lists in somelists1
# using list comprehension
cart_prod = [[a,b,c] for a in somelists[0] for b in somelists[1] for c in somelists[2]]
# print(cart_prod)
for s in cart_prod:
  str = ''
  l = list(s)
  # print(l)
  str = ' '.join(l)
  print(str)

list1 = [9, 8 ,5, 1, 1, 7 ,6, 5]
set1 = set(list1)
print(set1)