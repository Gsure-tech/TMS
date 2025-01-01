# Combine and Sort Lists
# Beginner Level Project

# Step 1: Define the two lists
list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

# Step 2: Combine the lists
combined_list = list1 + list2

print("Combined_list", combined_list)

# Step 3: Remove duplicates by converting the list to a set
unique_list = list(set(combined_list))

# Step 4: Sort the list in ascending order
unique_list.sort()

# Step 5: Print the sorted list
print("Sorted list without duplicates:", unique_list)
