# --- Friday: The Steward's Inventory ---

# 1. Your Upwork Identity
developer_name = "Xavier"  # Use your name here!
agency_name = "Lee Automation"

# 2. The Skills (The Inventory)
skill_1 = "Python Web Scraping"
skill_2 = "Automated Data Cleaning"
skill_3 = "Custom API Integrations"

# 3. The Pricing (Using what we learned Wednesday/Thursday)
hourly_rate = 45.0
daily_rate = hourly_rate * 8

# 4. The Professional Output
print(f"AGENCY: {agency_name.upper()}")
print(f"LEAD DEVELOPER: {developer_name}")
print(f"\nRETAIL SERVICES:")
print(f"\t- {skill_1.title()}")
print(f"\t- {skill_2.title()}")
print(f"\t- {skill_3.title()}")

print(f"\nFINANCIALS:")
print(f"\tBase Rate: ${hourly_rate:,.2f}/hr")
print(f"\tDay Rate:  ${daily_rate:,.2f} (Stewardship Discount)")