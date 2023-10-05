from collections import Counter

blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O', 'C']
# blood_dict = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}

# for blood in blood_dict.keys():
    
#     blood_dict[blood] = blood_list.count(blood)

# print(blood_dict)

#===========================================

blood_dict = {}
counts = Counter(blood_list)
#print(blood_dict)    #<- Counter({'A': 3, 'O': 3, 'B': 2, 'AB': 2, 'C': 1})

for element, count in counts.items():
    blood_dict[element] = count

print(blood_dict)