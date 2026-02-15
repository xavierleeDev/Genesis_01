# --- Thursday: Working with Numerical Lists ---

# 1. Using range() to print numbers 1 to 5
# Note: range(1, 6) starts at 1 and stops BEFORE 6.
print("Counting to 5:")
for value in range(1, 6):
    print(f"\t{value}")

# 2. Making a massive list instantly
# We use the list() function around range()
numbers = list(range(1, 101))
print(f"\nGenerated a list of {len(numbers)} numbers.")

# 3. Simple Statistics (Very useful for Agency Reporting)
ages = [19, 25, 33, 45, 12, 60, 22]
print(f"\nMinimum age: {min(ages)}")
print(f"Maximum age: {max(ages)}")
print(f"Total Sum: {sum(ages)}")

# 4. List Comprehension (The "Pro" Shortcut)
# This creates a list of squared numbers in ONE line.
squares = [value**2 for value in range(1, 11)]
print(f"\nSquares from 1-10: {squares}")