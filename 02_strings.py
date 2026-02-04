# 1. The Raw Motto
motto = "automation is stewardship"

# 2. String Methods (The Polish)
print(motto.upper()) # ALL CAPS for urgency
print(motto.title()) # Capitalize Each word  for branding

# 3. Whitespace is Formatting (The Layout)
# /n creates a new line | \t adds a tab (indent)
formatted_motto = f"Daily Mission:\n\t{motto.title()}"

print(formatted_motto)