# ---Thursday: F-String Masterclass ---

# 1. Data Points
project_name = "Genesis_01"
progress_percent = 65.5 
weekly_earnings = 1250.0
days_left = 2

# 2. The Power of the F-String
# we can do math AND formatting right inside the curly braces!

# Formatting a percentage to 0 decimal places
summary = f"Project: {project_name.title()}"

# .1f means "Floating point with 1 decimal place"
status = f"Progress: {progress_percent:.1f}% Complete"

# Formatting currency with a comma and 2 decimal places
finance = f"Weekly Target: ${weekly_earnings:,.2f}"

# 3. Putting it all together
print("-" * 30) # A clean separator line
print(f"STARTDATE REPORT: {project_name.upper()}")
print(f"{summary}")
print(f"{status}")
print(f"{finance}")
print(f"Deadline: {days_left} days remaining")
print("-" * 30)