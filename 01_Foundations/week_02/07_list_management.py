# --- Tuesday: Organizing & Processing Lists ---

# 1. The Backlog (Our initial list of tasks)
tasks = ['email_client', 'clean_data', 'push_to_github', 'bill_client']

# 2. "Popping" a task (The Automation Workflow)
# .pop() removes the LAST item and lets you work with it.
current_task = tasks.pop() 

print(f"Processing Task: {current_task}")
print(f"Remaining Tasks: {tasks}")

# 3. Deleting by Position (The 'del' statement)
# Let's say the first task is spam/garbage.
del tasks[0]
print(f"\nRemoved Spam. Current List: {tasks}")

# 4. Removing by Value (When you know WHAT, but not WHERE)
# We finished cleaning data, so let's remove it by name.
tasks.remove('clean_data')
print(f"Data Cleaned. Final List: {tasks}")

# 5. Sorting (Organizing for Clarity)
# Let's add some new random tasks to sort.
new_tasks = ['zebra_setup', 'alpha_protocol', 'beta_test']
new_tasks.sort() # Sorts A-Z permanently
print(f"\nSorted Tasks: {new_tasks}")

# --- Sorting in Reverse ---

clients = ['Zebra_Corp', 'Apple_Inc', 'Micro_Systems', 'Best_Buy']

# 1. Normal Sort (A-Z)
clients.sort()
print(f"Alphabetical: {clients}")
# Output: ['Apple_Inc', 'Best_Buy', 'Micro_Systems', 'Zebra_Corp']

# 2. Reverse Sort (Z-A)
# We use the 'reverse=True' argument inside the parentheses
clients.sort(reverse=True)
print(f"Reverse Order: {clients}")
# Output: ['Zebra_Corp', 'Micro_Systems', 'Best_Buy', 'Apple_Inc']