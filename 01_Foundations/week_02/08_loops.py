# --- Wednesday: Looping Through Lists ---

# 1. The List (The "Fuel" for our loop)
websites = ['upwork.com', 'freelancer.com', 'fiverr.com', 'linkedin.com']

# 2. The Loop (The "Engine")
# Translation: "For every single 'site' inside the 'websites' list..."
for site in websites:
    # EVERYTHING indented here happens 4 times!
    print(f"Logging into: {site}")
    print(f"\t- Scraping data from {site}...")
    print(f"\t- Data saved for {site}.\n")

# 3. The Exit (Outside the loop)
# This line is NOT indented, so it only runs once at the very end.
print("--- Job Complete: All sites processed ---")