print("=" * 50)
print("LIST OPERATIONS")
print("=" * 50)

fruits = ["Apple","Orange","Grapes"] #created a new list
print (f"this is ur initial list{fruits}")

#ADD

fruits.append("Mango") #add at the end only one item can add
print(f"this is ur list after append{fruits}")

fruits.insert(1, "Mango") # add in a position
print(f"this is ur list add mango at index1 {fruits}")

fruits.extend(["kiwi", "Apricot"]) # add more items at the end
print(f"this is ur list after adding multiple items at end {fruits}")


#Update

fruits[0]="Blueberry"
print(f"this is ur list after adding blueberry at 0th position {fruits}")

#Delete

fruits.remove("Apricot")#remove by value
print(f"this is list after removing apricot {fruits}")

deleted = fruits.pop()# Remove and return last item
print(f"after pop (removed {deleted}) {fruits} ")

# TRAVERSE (Display)
print("\nTraversing list:")
for i , fruit in enumerate (fruits):
    print(f"index{i} : {fruit}")

#Sorting
fruits.sort()
print(f" sorted list {fruits}")

fruits.sort(reverse=True) #sorting in reverse
print(f"sorting in reverse { fruits}")

print("\n" + "=" * 50)
print("TUPLE OPERATIONS")
print("\n" + "=" * 50)

colors = ("red" , "blue" , "green") #created a tuple
print (f"initial tuple {colors}")

# ADD(Create new tuple)
colors = colors + ("yellow",) # Concatenation
print(f" add a yellow at end {colors}")

# UPDATE (Cannot update - immutable, must create new)
colors = colors[:2]+("purple",)+colors[2:]
print(f"updted purple at index 2 {colors}")

# DELETE (Cannot delete individual items - immutable)
# Can only delete entire tuple: del colors

# TRAVERSE
print("\nTraversing tuple:")
for i, color in enumerate(colors):
    print(f"  Index {i}: {color}")

# SORTING (Returns list)
colors = sorted(colors)
print(f"Sorted : {colors}")

print("\n" + "=" * 50)
print("DICTIONARY OPERATIONS")
print("=" * 50)

# Create a dictionary
student = {"name" : 'Aisha' , "age" : 30 , "grade" : "A"}
print(f"Initial Dictionary{student}")

#Add
student ["city"] = "Kerala" # Add new key-value
print(f"Dictionary after add city{student}")

student.update({"major" : "cs", "year": "2015"}) #Add multiple key values
print(f"Dictionary after add multiple values{student}")

#Update
student["age"] = "32"
print(f"Dictionary after update age {student}")

student.update({"grade": "A+"})  # Update using update()
print(f"After updating 'grade': {student}")

# DELETE
del student["year"]  # Delete by key
print(f"After del 'year': {student}")

removed= student.pop("major")  # Remove and return value
print(f"After pop 'major' (removed '{removed}'): {student}")

# TRAVERSE
print("\nTraversing dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\nTraversing keys only:")
for key in student.keys():
    print(f"  {key}")

print("\nTraversing values only:")
for value in student.values():
    print(f"  {value}")

#Sorting
student = { "aisha": "10", "thejus": "12" , "abi" : "40"}
print(f"Dictionary before sorting: {student}")

sorted_by_keys = dict(sorted(student.items()))
print(f"Sorted by keys: {sorted_by_keys}")

sorted_by_values = dict(sorted(student.items(), key=lambda x: x[1]))
print(f"Sorted by values: {sorted_by_values}")

# Sort descending
sorted_desc = dict(sorted(student.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted by values (desc): {sorted_desc}")

from itertools import groupby

students = [
    {"name": "Aisha", "grade": "A", "age": 20},
    {"name": "thejus", "grade": "B", "age": 21},
    {"name": "test", "grade": "A", "age": 20},
    {"name": "abi", "grade": "B", "age": 22},
]

# Must sort by the grouping key first
students_sorted = sorted(students, key=lambda x: x["grade"])

print("\nGrouping students by grade:")
for grade, group in groupby(students_sorted, key=lambda x: x["grade"]):
    print(f"  Grade {grade}:")
    for student in group:
        print(f"    - {student['name']}")


print("\n" + "=" * 50)
print("SET OPERATIONS")
print("=" * 50)

# creating a set
numbers = { "1", "2", "3"}
print(f"initial set {numbers}")

# add
numbers.add("5")  # Add single item
print(f"After add '5': {numbers}")

numbers.update(["6", "7"])  # Add multiple items
print(f"After update with multiple: {numbers}")

numbers.add("5")  # Adding duplicate (ignored)
print(f"After adding duplicate '5': {numbers}")

# UPDATE (Sets don't have index-based update)
# Remove old value and add new one
if "5" in numbers:
    numbers.remove("5")
    numbers.add("55")
print(f"After 'updating' 5 to 55: {numbers}")

# DELETE
numbers.remove("6")  # Remove (raises error if not found)
print(f"After remove '6': {numbers}")

numbers.discard("55")  # Remove (no error if not found)
print(f"After discard '55': {numbers}")

popped = numbers.pop()  # Remove random item
print(f"After pop (removed '{popped}'): {numbers}")

# TRAVERSE
print("\nTraversing set:")
for number in numbers:
    print(f"  {number}")

# SORTING (Returns list)
nums_set = {5, 2, 8, 1, 9}
print(f"\nOriginal set: {nums_set}")
sorted_set = sorted(nums_set)  # Returns sorted list
print(f"Sorted (returns list): {sorted_set}")

# SET OPERATIONS
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"\nSet1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

