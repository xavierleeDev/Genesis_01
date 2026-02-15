# ---Wednesday: Numbers & Math ---

# 1. Your Variables
hours_per_day = 1.5
days_per_week = 6
weeks_to_freedom = 12

# 2. The Calculations
total_hours_planned = hours_per_day * days_per_week * weeks_to_freedom
current_study_session = 45 # minutes
remaining_minutes_in_hour = 60 - current_study_session

# 3. The Result (Using f-string from Monday)
print(f"Goal: {total_hours_planned} total hours of coding in {weeks_to_freedom} weeks.")
print(f"I have {remaining_minutes_in_hour} minutes left in this hour's session.")

# 4. The "Stewardship" Bonus
# Python follows PEMDAS. Try this:
upwork_goal = (5000/4) # weekly goal for a $5k month
print(f"To hit my monthly goal. I need to earn ${upwork_goal} per week.")

# Integer Division (The Floor)
# Using // instead of / drops the decimal entirely
weekly_goal_int = 5000 // 4 
print(weekly_goal_int) # This will print 1250 (No .0!)