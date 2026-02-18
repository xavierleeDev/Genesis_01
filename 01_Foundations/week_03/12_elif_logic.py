# --- Tuesday: Complex Decision Making ---

order_value = 750

if order_value >= 1000:
    print("Status: Platinum Priority")
elif order_value >= 500:
    print("Status: Gold Standard")
elif order_value >= 100:
    print("Status: Silver Tier")
else:
    print("Status: Basic Tier")

# Pro Tip: Order matters! 
# If you put 'order_value >= 100' at the top, 
# a $750 order would stop there and never reach the 'Gold' check.

age = 25
has_license = True

# Using 'and' for strict requirements
if age >= 18 and has_license:
    print("You can operate the company vehicle.")

# Using 'or' for flexible requirements
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("The office automation is in 'Off-Hours' mode.")


# Ask the user for the temperature
temp = int(input("Enter the current temperature: "))

if temp > 90:
    print("It's scorching! Stay hydrated.")
elif 70 <= temp <= 90:
    print("Perfect weather for coding.")
elif 50 <= temp <= 69:
    print("A bit chilly, grab a jacket.")
else:
    print("It's freezing! Stay inside.")

try:
    temp = int(input("Enter the current temperature: "))
    # ... your logic here ...
except ValueError:
    print("Please enter a valid number next time!")
