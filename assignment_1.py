# ==========================================
# 1. LIST OPERATIONS (Mutable & Ordered)
# ==========================================
print("--- LIST OF STUDENTS ---")
students_list = ["Aarav", "Sanchita", "Rohan"]
print("Initial List:", students_list)

# Add a student
students_list.append("Priya")
print("After Add ('Priya'):", students_list)

# Update a student (by index)
students_list[1] = "Sanchita Sharma"
print("After Update (index 1):", students_list)

# Delete a student (by value)
students_list.remove("Rohan")
print("After Delete ('Rohan'):", students_list)


# ==========================================
# 2. DICTIONARY OPERATIONS (Key-Value Pairs)
# ==========================================
print("\n--- DICTIONARY OF STUDENTS (Roll No: Name) ---")
students_dict = {101: "Aarav", 102: "Sanchita", 103: "Rohan"}
print("Initial Dictionary:", students_dict)

# Add a student
students_dict[104] = "Priya"
print("After Add (104: 'Priya'):", students_dict)

# Update a student's name using their key
students_dict[102] = "Sanchita Sharma"
print("After Update (102):", students_dict)

# Delete a student using their key
del students_dict[103]
print("After Delete (103):", students_dict)


# ==========================================
# 3. TUPLE OPERATIONS (Immutable)
# ==========================================
print("\n--- TUPLE OF STUDENTS ---")
students_tuple = ("Aarav", "Sanchita", "Rohan")
print("Initial Tuple:", students_tuple)

# Add a student (via tuple concatenation)
students_tuple = students_tuple + ("Priya",)
print("After Add ('Priya'):", students_tuple)

# Update a student (convert to list -> modify -> convert back to tuple)
temp_list = list(students_tuple)
temp_list[1] = "Sanchita Sharma"
students_tuple = tuple(temp_list)
print("After Update (index 1):", students_tuple)

# Delete a student (convert to list -> remove -> convert back to tuple)
temp_list = list(students_tuple)
temp_list.remove("Rohan")
students_tuple = tuple(temp_list)
print("After Delete ('Rohan'):", students_tuple)
