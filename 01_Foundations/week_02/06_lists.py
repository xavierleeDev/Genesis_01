# --- Monday: List Mastery ---

# 1. Creating a list (Use square brackets[])
leads = ['john@leeauto.com', 'sarah@tech.io', 'mike@startup.net']

# 2. Accessing items (Python starts counting at 0!)
print(f"First lead in the system: {leads[0]}")
print(f"Most recent lead: {leads[-1]}") # -1 is a shortcut for the end

# 3. Modifying the list (The "Steward's Inventory" grows)
leads.append('agency@growth.org') # Adds to the end
leads.insert(0, 'priority@client.com') # Puts them at the front

print(f"Current Lead Count: {len(leads)}")
print(leads)