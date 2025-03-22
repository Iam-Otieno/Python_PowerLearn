my_list = [] # Creating an empty list
# Adding elements to the list using a loop
for i in range(10, 50, 10):
    my_list.append(i) # Adding elements to the list
print(my_list)
my_list.append(15) # Adding an element to the list
print(my_list)
my_list.extend([50, 60, 70]) # Adding more elements to the list
print(my_list)
my_list.pop() # Removing the last element from the list
print(my_list)
my_list.sort() # Sorting the list
my_list.index(30) # Finding the index of an element in the list