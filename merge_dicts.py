n1 = int(input("Enter number of keys for d1:"))
d1 = {}

for i in range(n1):
    keys = input("Key(d1):") #str value for key
    values = int(input("Value(d1):")) # int for value
    d1[keys] = values

n2 = int(input("Enter number of keys for d2:"))
d2 = {}
for i in range(n2):
    keys = input("Key(d2):") #str value for key
    values = int(input("Value(d2):")) # int for value
    d2[keys] = values


def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

d3 = Merge(d1,d2)
print(d3)