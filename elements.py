print("\t\t\t\t********Adding items*********")
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati') # append() adds to the end of the list
print("After adding to the list:", motorcycles)

motorcycles.insert(0,'toyota') # insert() opens space at position 0.
print("After adding to the list:", motorcycles)


# Removing an Item using the del statement
print("\n\t\t\t\t********Removing items*********")
del motorcycles[0]
print("After removing:", motorcycles)

# Removing an item using pop() method
popped_motorcycle = motorcycles.pop() # pop() removes last item in a list.
print("After removing:", motorcycles)
print("Removed item:", popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")

# Popping items from any position in a list
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")

# Removing item by value
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print("\n\t\t\t\t*****Removing item by value*******")
print("A " + too_expensive.title() + " is too expensive for me.")