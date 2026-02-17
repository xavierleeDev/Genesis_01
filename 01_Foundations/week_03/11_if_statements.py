# --- Monday: Logic & If Statements ---

# 1. The Setup (Simulating a data check)
client_status = 'overdue'
order_total = 500

# 2. The Basic If Statement
# Note the double equals (==) for comparison!
if client_status == 'overdue':
    print("ALERT: Send payment reminder to client.")

# 3. If-Else (The Fork in the Road)
if order_total >= 1000:
    print("Priority: High Value Client.")
else:
    print("Priority: Standard Client.")

# 4. Checking for Errors (What your boss asked for)
# Checking if a value is empty or negative
data_point = -5 

if data_point < 0:
    print("ERROR: Negative value detected in database!")