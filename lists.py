

# 1.This code initializes an empty list 
my_list = []

# 2.Appending integers 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)  

# 3.Insert the value 15 at the second position in the list.
my_list.insert(1 , 15) 
print(my_list)  

# 4.Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# 5.Remove the last element from my_list.
my_list.remove(my_list[-1])
print(my_list)

# 6.Sort my_list in ascending order.
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")
