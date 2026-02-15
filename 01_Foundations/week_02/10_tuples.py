# --- Friday: Working with Tuples ---

# 1. Defining a Tuple (Immutable)
# These are coordinates for a scraping target that shouldn't move.
dimensions = (1920, 1080)
print(f"Original dimensions: {dimensions[0]}x{dimensions[1]}")

# 2. The "Immutable" Rule
# If you try to do: dimensions[0] = 2000, Python will throw a TypeError.
# Tuples protect your data from accidental changes.

# 3. Looping through a Tuple
print("\nSupported Resolutions:")
for dim in dimensions:
    print(dim)

# 4. Overwriting a Tuple
# You can't change a tuple, but you can redefine the whole variable.
dimensions = (3840, 2160)
print(f"\nNew dimensions: {dimensions}")