# Read number of rows and columns from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty list to store the matrix
matrix = []

print("Enter the elements of the matrix row-wise (space separated):")

# Take matrix input row by row
for i in range(rows):
    while True:
        # Read one complete row as space-separated integers
        row = list(map(int, input().split()))

        # Check if the number of elements entered is correct
        if len(row) == cols:
            matrix.append(row)   # Add the valid row to the matrix
            break
        else:
            print(f"Please enter exactly {cols} elements.")

# Display the matrix
print("\nThe matrix is:")
for row in matrix:
    print(row)

# Calculate and display row-wise sums
print("\nRow-wise sums:")
for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]   # Add elements of the current row
    print(f"Sum of row {i + 1}: {row_sum}")

# Calculate and display column-wise sums
print("\nColumn-wise sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]   # Add elements of the current column
    print(f"Sum of column {j + 1}: {col_sum}")

# Search for a key element in the matrix
key = int(input("\nEnter the key to search: "))
found = False   # Flag variable to track search result

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print(f"Key {key} found at position ({i + 1}, {j + 1})")
            found = True

# If the key was not found anywhere in the matrix
if not found:
    print(f"Key {key} not found in the matrix.")