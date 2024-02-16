"""6. Write a Python program to get the maximum and minimum values of a dictionary """


d1={'key1':['a','b','c','d','e'],'key2':[4,5,2,8,3],'key3':[True,False,False,True,True]}

print("Maximum = ",max(d1['key2']))
print("Minimum = ",min(d1['key2']))

#Another Method

d2={'a': 0, 'b': 4, 'c': 6, 'd': 3}

print("Maximum = ",max(d2.values()))
print("Minimum = ",min(d2.values()))
