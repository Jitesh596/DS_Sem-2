# ============================
# TOWER OF HANOI PROBLEM
# ============================

# Goal:
# Move n disks from Source rod to Target rod using an Auxiliary rod

# Rules:
# 1. Only one disk can be moved at a time
# 2. A larger disk cannot be placed on a smaller disk

# Base case: If there are no disks to move, stop the recursion    
# Step 1: Move (n-1) disks from Source to Auxiliary using Target as helper   
# Step 2: Move the largest (nth) disk directly from Source to Target 
# Step 3: Move the (n-1) disks from Auxiliary to Target using Source as helper

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 0:
        return

    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# ============================
# DRIVER CODE
# ============================
if __name__ == "__main__":
    n = 3  # number of disks
    tower_of_hanoi(n, 'A', 'C', 'B')
    # A = Source rod, C = Target rod, B = Auxiliary rod


# ============================
# THEORY & COMPLEXITY
# ============================

# Number of moves:
# Each additional disk requires moving all previous disks twice
# plus one move for the largest disk

# Recurrence Relation:
# T(n) = 2T(n-1) + 1

# Solution:
# T(n) = 2^n - 1

# Time Complexity: O(2^n)
# Space Complexity: O(n) due to recursion stack