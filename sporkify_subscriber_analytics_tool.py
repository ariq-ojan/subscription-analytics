### IMPORTING REQUIRED LIBRARIES
from tabulate import tabulate
from datetime import datetime, date, timedelta

### DATE AND TIME FORMATTING
current_date = "2025-12-31"
DATE_FMT = "%Y-%m-%d"

### SPORKIFY USER DATABASE
users = {
    "1": {                            # user_id and key of the dictionary
    "name": "Ali Susanto",            # Username
    "acq_channel": "Referral",        # Acquisition channel (Referral/Ads/Organic)
    "subscriptions": [                # List of subscriptions stored in a dictionary
        {"plan": "Basic", 
         "start_date": "2025-01-01",
         "end_date": "2025-06-30",
         "status": "Inactive"},
        {"plan": "Pro", 
         "start_date": "2025-07-01",
         "end_date": None,
         "status": "Active"}
        ]
    },

    "2": {
    "name": "Brian Goransson",
    "acq_channel": "Ads",
    "subscriptions": [
        {"plan": "Ultimate", 
         "start_date": "2025-02-14",
         "end_date": "2025-09-27",
         "status": "Inactive"}
        ]
    },
    
    "3": {
    "name": "Cokil Rastafarian",
    "acq_channel": "Organic",
    "subscriptions": [
        {"plan": "Pro", 
         "start_date": "2025-03-10",
         "end_date": None,
         "status": "Active"}
        ]
    },

    "4": {
    "name": "Dewi Kirana",
    "acq_channel": "Referral",
    "subscriptions": [
        {"plan": "Pro", 
         "start_date": "2025-01-15",
         "end_date": "2025-05-31",
         "status": "Inactive"},
        {"plan": "Ultimate", 
         "start_date": "2025-06-01",
         "end_date": "2025-12-17",
         "status": "Active"}
        ]
    },

    "5": {
    "name": "Eggy Sidabutar",
    "acq_channel": "Ads",
    "subscriptions": [
        {"plan": "Basic", 
         "start_date": "2025-01-20",
         "end_date": "2025-04-27",
         "status": "Inactive"},
        {"plan": "Pro", 
         "start_date": "2025-09-01",
         "end_date": None,
         "status": "Active"}
        ]
    },

    "6": {
    "name": "Fang Xiu Xiu",
    "acq_channel": "Referral",
    "subscriptions": [
        {"plan": "Ultimate", 
         "start_date": "2025-07-01",
         "end_date": None,
         "status": "Active"}
        ]
    },

    "7": {
    "name": "Geebran Dungeau",
    "acq_channel": "Ads",
    "subscriptions": [
        {"plan": "Basic", 
         "start_date": "2025-01-11",
         "end_date": "2025-03-20",
         "status": "Inactive"},
        {"plan": "Pro", 
         "start_date": "2025-05-01",
         "end_date": "2025-08-20",
         "status": "Inactive"},
        {"plan": "Basic", 
         "start_date": "2025-11-01",
         "end_date": None,
         "status": "Active"}
        ]
    },

    "8": {
    "name": "Hirohashi Takoyaki",
    "acq_channel": "Referral",
    "subscriptions": [
        {"plan": "Basic", 
         "start_date": "2025-03-12",
         "end_date": None,
         "status": "Active"}
        ]
    },

    "9": {
    "name": "Indah Gobleaux",
    "acq_channel": "Organic",
    "subscriptions": [
        {"plan": "Ultimate", 
         "start_date": "2025-06-10",
         "end_date": "2025-11-27",
         "status": "Inactive"}
        ]
    },

    "10": {
    "name": "Jacky Yusuf",
    "acq_channel": "Ads",
    "subscriptions": [
        {"plan": "Pro", 
         "start_date": "2025-02-20",
         "end_date": "2025-04-14",
         "status": "Inactive"},
        {"plan": "Pro", 
         "start_date": "2025-08-04",
         "end_date": "2025-09-27",
         "status": "Inactive"}
        ]
    },
}

### SPORKIFY SUBSCRIPTION PLANS
sporkify_plans = {
        "basic": 35000,
        "pro": 50000,
        "ultimate": 100000
    }

### MENU OPTION 1: SHOW USERS (WORKS)
def show_user_database(users):
    table = []
    for user_id, user in users.items(): 
        subs = user.get("subscriptions", []) 

        if subs:
            latest = subs[-1] #Takes the last subscription in the list
            row = [
                user_id,
                user["name"].title(), # .title() For better name formatting
                latest["plan"].title(),
                latest["start_date"],
                latest["end_date"] if latest["end_date"] else "Active",
                user["acq_channel"],   
                latest["status"]
            ]
        else: #If user never have any subscription
             row = [
                user_id,
                user["name"],
                "-", "-", "-",  # no plan/dates
                user["acq_channel"],
                "Not Subscribed"
            ]
             
        table.append(row)

    headers = ["ID", "Name", "Plan", "Start", "End", "Channel", "Status"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid")) #Print table using tabulate

### MENU OPTION 2: ADD NEW USERS (WORKS)
def add_user (users):

    ##Generated incremental user id number.
    if not users:
        user_id = 1  # If users dict is empty, set user_id = 1
    else:
        user_id = max(int(uid) for uid in users.keys()) + 1  # Loops, looks for the highest uid value and +1

    ## Header
    print(f"\n{'='*40}")
    print(f"ADD NEW USER")
    print(f"{'='*40}")

    new_name = input("Insert new user name: ").strip().title()

    ##Ask for valid acquisition channel:
    while True:
        new_acq_channel = input("Insert acquisition channel (Referral/Ads/Organic): ").strip().lower()
        if new_acq_channel in ["referral", "ads", "organic"]:
           break 
        else:
            print("Acquisition channel invalid! Only input Referral/Ads/Organic. ")
    
    ##Save new user to users database
    users[str(user_id)] = {
        "name": new_name,
        "acq_channel": new_acq_channel.capitalize(),
        "subscriptions": []
    }

    print(f"User {user_id} ({new_name}) has been added successfully! ")

### MENU OPTION 3: DELETE USERS (WORKS)
def delete_user(users):

    ## Header
    print(f"\n{'='*40}")
    print(f"DELETE USER")
    print(f"{'='*40}")

    show_user_database(users)
    while True:
        delete_uid = input("Insert user ID to delete: ").strip()
        if delete_uid in users:
            confirm = input(f"Are you sure you want to delete User {delete_uid}? (Y/N)") # Extra layer of confirmation
            if confirm.lower() == "y":
                del users[delete_uid]
                print(f"User {delete_uid} deleted successfully.")
            else:
                print("Input invalid! User delete cancelled.") # Automatically cancel delete function for safety
            break
        else:
            print(f"Input invalid! User ID {delete_uid} doesn't exist.")

### MENU OPTION 4: MANAGE SUBSCRIPTIONS
## HELPER FUNCTIONS
def convert_str_to_date(date_string): # Takes a date string and converts it into a 'datetime' object

    if date_string is None or date_string == "": # Validation: If input is none or empty, return none.
        return None
    
    if not isinstance(date_string, str): # Validation: if input is not a string, return none.
        return None
    
    try:
        return datetime.strptime(date_string, DATE_FMT).date()
    except (ValueError, TypeError):  # If results error, just return nothing bruh
        return None    
def is_valid_date_format(date_string): # Returns date data that passes the validation
    return convert_str_to_date(date_string) is not None
def validate_date_input(date_string): # Returns a boolean and the converted date data
    if not is_valid_date_format(date_string):
        return False, "Invalid date format! Please use YYYY-MM-DD"
    
    input_date = convert_str_to_date(date_string)
    current_date_obj = convert_str_to_date(current_date)
    
    # Cannot be in the future (after current frozen date)
    if input_date > current_date_obj:
        return False, f"Date cannot be after current date ({current_date_obj})"
    
    return True, input_date
def get_latest_subscription(user_id): # Returns a dict of latest subscription
    if user_id not in users: # Validation: user_id must exist in users dict
        return None
    
    subscriptions = users[user_id]["subscriptions"]

    if not subscriptions: # Validation: If the specific user have no subscriptions, return None
        return None
    
    latest_sub = subscriptions[0] 

    # Loops through each subscription and compares each values with itself to find the latest subscription
    for subscription in subscriptions: 
        if convert_str_to_date(subscription["start_date"]) > convert_str_to_date(latest_sub["start_date"]):
            latest_sub = subscription
    
    return latest_sub
def get_current_active_subscription(user_id): # Returns the latest active subscription
    if user_id not in users:
        return None
    
    subscriptions = users[user_id]["subscriptions"]
    
    for subscription in subscriptions:
        if subscription["end_date"] == None and subscription["status"].lower() == "active":
            return subscription
        
    return None

## SUB-MENU 1: VIEW SUBSCRIPTION HISTORY
def view_subscription_history(user_id):
    if user_id not in users: #Check if user id exists
        print(f"User ID {user_id} not found.")
        return
    user = users[user_id]
    user_name = user["name"]
    acq_channel = user["acq_channel"]
    subscriptions = user.get("subscriptions", [])

    # Getting the subscription status of the latest sub
    current_sub = get_latest_subscription(user_id)
    if current_sub is None: 
        current_status = None
    elif current_sub["status"].lower() == "active":
        current_status = "Active"
    else:
        current_status = "Inactive"
    
    # Print header with user info
    print(f"\nID: {user_id} | Name: {user_name} | Acquisition: {acq_channel}")
    
    # Print subscription history
    print("\nHistory:")
    
    if not subscriptions:
        print("No subscription history found.")
        return
    
    # Sort subscriptions by start_date to show chronological order
    sorted_subs = sorted(subscriptions, key=lambda x: x["start_date"])
    
    for sub in sorted_subs:
        plan = sub["plan"].capitalize()
        start_date = sub["start_date"]
        end_date = sub["end_date"]
        
        # Format the end date - show "Active" if None, otherwise show the date
        if end_date is None:
            end_display = "Active"
        else:
            end_display = end_date
        
        # Print in the requested format with proper spacing
        print(f"  - {plan:<8} | {start_date} → {end_display}")

    print(f"\nSubscription Status: {current_status}")

## SUB-MENU 2: START SUBSCRIPTION
def start_subscription(user_id):
    print(f"\n{'='*40}")
    print(f"START NEW SUBSCRIPTION")
    print(f"{'='*40}")
    
    latest_sub = get_latest_subscription(user_id)
    
    # Check if user can start a new subscription
    if latest_sub is not None and latest_sub["status"] == "Active":
        print(f"User has an active {latest_sub['plan'].capitalize()} subscription!")
        print("Please stop the current subscription first.")
        return False
    
    # Show available plans
    print(f"{'Plan':<10} {'Price (Rp)':>12}")
    print("-" * 25)

    for plan, price in sporkify_plans.items():
        print(f"{plan.capitalize():<10} {price:>12,}")
        
    plan = input("Input selected plan (Basic/Pro/Ultimate): ").strip()
    
    # Validate plan
    if plan.lower() not in sporkify_plans:
        print(f"'{plan}' is not a valid plan!")
        return False
    
    # Get start date
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    
    # Validate start date
    is_valid, result = validate_date_input(start_date)
    if not is_valid:
        print(f"ERROR: {result}")
        return False
    
    # Additional validation: start date should be after latest subscription end date
    if latest_sub is not None and latest_sub["end_date"] is not None:
        latest_end = convert_str_to_date(latest_sub["end_date"])
        start_date_obj = convert_str_to_date(start_date)
        
        if start_date_obj <= latest_end:
            print(f"Start date must be after your last subscription ended ({latest_sub['end_date']})")
            return False
    
    # Create new subscription
    new_subscription = {
        "plan": plan,
        "start_date": start_date,
        "end_date": None,  # Means still going
        "status": "Active"
    }
    
    users[user_id]["subscriptions"].append(new_subscription)
    
    print(f"Started {plan.capitalize()} subscription on {start_date}")
    return True

## SUB-MENU 3: STOP SUBSCRIPTION
def stop_subscription(user_id):
    print(f"\n{'='*40}")
    print(f"STOP SUBSCRIPTION")
    print(f"{'='*40}")

    latest_sub = get_latest_subscription(user_id)

    if latest_sub is None or latest_sub["status"] != "Active":
        print("User has no active subscription to stop.")
        print("Please start a subscription first.")
        return False
    
    print(f"Current active subscription: {latest_sub["plan"].capitalize()}, started on {latest_sub["start_date"]}")

    stop_date = input("Enter stop date (YYYY-MM-DD): ").strip()

    is_valid, result = validate_date_input(stop_date)
    if not is_valid:
        print(f"Error: {result}")
        return False
    
    # Update the subscription
    latest_sub["end_date"] = stop_date
    latest_sub["status"] = "Inactive"
    
    print(f"Stopped {latest_sub['plan'].capitalize()} subscription on {stop_date}")
    return True

## SUB-MENU 4: UPDATE PLAN 
def update_plan(user_id):
    print(f"\n{'='*40}")
    print(f"UPDATE PLAN")
    print(f"{'='*40}")
   
    latest_sub = get_latest_subscription(user_id) # Validation: must have a subscription.
    if latest_sub is None:
        print(f"User has no active subscription.")
        return False
    
    if latest_sub["status"].lower() == "inactive": # Validation: latest subscription must be active.
        print("User must have an active subscription to update.")
        return False

    print(f"Current active subscription: {latest_sub["plan"]}, started on {latest_sub["start_date"]}")
    
    # Show available plan and pricelist
    print(f"{'Plan':<10} {'Price (Rp)':>12}")
    print("-" * 25)

    for plan, price in sporkify_plans.items():
        print(f"{plan.capitalize():<10} {price:>12,}")

    new_plan = input("Input updated plan (Basic/Pro/Ultimate): ").lower()
    
    if new_plan not in sporkify_plans: # Validation: selected plan must exist in list of plans.
        print(f"Input invalid! Plan '{new_plan}' is not available.")
        return False
    
    if latest_sub["plan"].lower() == new_plan: # Validation: selected plan cant be the same as the old one.
        print(f"User {user_id} is already on {new_plan} plan!")
        return False
    
    # Get start date for new plan
    start_date = input("Enter start date for new plan (YYYY-MM-DD): ").strip()
    is_valid, result = validate_date_input(start_date) # Validation: using previous function.
    if not is_valid:
        print(f"Error: {result}")
        return False
    
    start_date_obj = convert_str_to_date(start_date)
   
    # Ends previous subscription the day before the new subscription starts.
    latest_sub["end_date"] = (start_date_obj - timedelta(days=1)).strftime("%Y-%m-%d")

    if latest_sub is not None and latest_sub["end_date"] is not None:
        latest_end = convert_str_to_date(latest_sub["end_date"])
        start_date_obj = convert_str_to_date(start_date)
        
        if start_date_obj <= latest_end:
            print(f"Start date must be after your last subscription ended ({latest_sub['end_date']})")
            return False
    
    # Create new subscription
    new_subscription = {
        "plan": new_plan,
        "start_date": start_date,
        "end_date": None,  # Means still going
        "status": "Active"
    }
    
    users[user_id]["subscriptions"].append(new_subscription)

    print(f"User {user_id} changed from {latest_sub["plan"].capitalize()} to {new_plan.capitalize()}")
    return True

## SUB-MENU 5: CHANGE NAME
def change_name(user_id):
    print(f"\n{'='*40}")
    print(f"CHANGE NAME")
    print(f"{'='*40}")

    new_name = input(f"Insert new name for {user_id}: ").strip().title()

    if new_name == "" or new_name == None: # Validation: new name cant be empty or the same as previous name
        print("New name can't be empty or identical with previous name.")
        return
    
    users[user_id]["name"] = new_name
    print(f"User {user_id}'s name has been updated to {new_name}.")
    return True
     
## MENU OPTION 4 MAIN MENU
def manage_subscription_menu():
    print(f"\n{'='*40}")
    print("MANAGE SUBSCRIPTION")
    print(f"{'='*40}")
    
    # Show all users first so they can see available IDs
    print("Available Users:")
    if not users:
        print("No users found.")
        return
    
    for user_id, user_data in users.items():
        print(f"  ID: {user_id} | Name: {user_data['name']}")

    user_id = input("\nEnter User ID: ").strip()    
    if user_id not in users:
        print(f"Input invalid! User {user_id} not found")
        return
    
    user_name = users[user_id]["name"]

    while True:
        current_name = users[user_id]["name"]

        print(f"\n{'='*50}")
        print(f"SUBSCRIPTION MANAGEMENT - {current_name} (ID: {user_id})")
        print(f"{'='*50}")
        print("1. View Subscription History")
        print("2. Start New Subscription")
        print("3. Stop Current Subscription")
        print("4. Change Plan")
        print("5. Change Name")
        print("6. Back to Main Menu")
        print(f"{'='*50}")
        
        choice = input("Input your selected menu (1-6): ").strip()
        
        if choice == "1":
            view_subscription_history(user_id)
        elif choice == "2":
            start_subscription(user_id)
        elif choice == "3":
            stop_subscription(user_id)
        elif choice == "4":
            update_plan(user_id)
        elif choice == "5":
            change_name(user_id)
        elif choice == "6":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

### MENU OPTION 5: SUBSCRIPTION INSIGHTS
## SUB-MENU 1: CHURN REPORT
def churn_report(users):

    # Header
    print(f"\n{'='*40}")
    print("CHURN REPORT")
    print(f"{'='*40}")

    #Placeholder variables
    churned = 0
    active = 0
    no_subscription = 0

    for user in users.values():
        subs = user.get("subscriptions", [])
        if not subs:
            no_subscription += 1
            continue

        latest = subs[-1]
        if latest["status"].lower() == "inactive":
            churned += 1
        else:
            active += 1

    total_ever_subscribed = churned + active
    churn_rate = (churned / total_ever_subscribed * 100) if total_ever_subscribed else 0

    # Print report
    summary_data = [
        ["Total Users", len(users)],
        ["Ever Subscribed", total_ever_subscribed],
        ["Currently Active", active],
        ["Churned Users", churned],
        ["Never Subscribed", no_subscription],
        ["Churn Rate", f"{round(churn_rate, 2)}%"]
    ]
    
    print(tabulate(summary_data, headers=["Metric", "Count"], tablefmt="fancy_grid"))

## SUB-MENU 2: MONTHLY RECURRING REVENUE (MRR) CALCULATOR
def mrr_calculator(users):

    #Header
    print(f"\n{'='*30}")
    print("MRR CALCULATOR")
    print(f"{'='*30}")
    
    try: # Use 'try/except' conditional statement
        month = int(input("Enter month number (1-12): ").strip()) # Input which month user wants to calculate
        if month < 1 or month > 12: # Validation
            print("Invalid month!")
            return

        # Month boundaries
        start = date(2025, month, 1) 
        end = (date(2025, month+1, 1) if month < 12 else date(2026, 1, 1)) - timedelta(days=1) # End is the next month of the selected month minus 1 days.
        month_name = start.strftime("%B") # Converts the int month value into month names (January, September, etc.)

        total_rev = 0 # Variable to accumulate revenue
        active_subs = [] # List to track active subscriber User ID
        plan_breakdown = {} # Dictionary to map plan count/revenue

        for uid, udata in users.items(): #
            for sub in udata.get("subscriptions", []):
                start_obj = convert_str_to_date(sub["start_date"])
                end_obj = convert_str_to_date(sub["end_date"])

                if (start_obj and start_obj <= end) and (end_obj is None or end_obj >= start):  # Validates if start object is active at any point in the month
                    plan = sub["plan"].lower()
                    price = sporkify_plans.get(plan, 0)
                    total_rev += price # Add price to the revenue variable
                    active_subs.append(uid) # Appends uid to active sub

                    # Update plan breeakdown
                    bd = plan_breakdown.setdefault(plan, {"count": 0, "revenue": 0})
                    bd["count"] += 1
                    bd["revenue"] += price

        # Header
        print(f"\n{'='*50}")
        print(f"MRR REPORT - {month_name.upper()} 2025")
        print(f"{'='*50}")

        print(f" TOTAL MRR: Rp{total_rev:,.2f}")
        print(f" TOTAL ACTIVE SUBSCRIBERS: {len(active_subs)}")

        if active_subs:
            print(f" AVERAGE REVENUE PER USER: Rp{total_rev/len(active_subs):.2f}")

        if plan_breakdown:
            table = [[p.capitalize(), d["count"], f"Rp{d["revenue"]:,.2f}", f"Rp{d["revenue"]/d["count"]:.2f}"] # Shows revenue and avg revenue per person
                     for p, d in plan_breakdown.items()]
            print("\n BREAKDOWN BY PLAN:")
            print(tabulate(table, headers=["Plan","Subs","Revenue","Avg/User"], tablefmt="fancy_grid"))

    except Exception as e:
        print(f"Error: {e}")

## SUB-MENU 3: CUSTOMER LIFETIME VALUE (CLV) CALCULATOR
def clv_calculator(users):
    def calculate_months_subscribed(start_date_str, end_date_str):
        try:
            start_date = datetime.strptime(start_date_str, DATE_FMT).date()
            
            if end_date_str is None:
                end_date = datetime.strptime(current_date, DATE_FMT).date() # Ongoing subscription - fixed "today"
            else:
                end_date = datetime.strptime(end_date_str, DATE_FMT).date()
            
            # Count months from start month to end month (inclusive)
            months = 0
            current = start_date.replace(day=1)
            end_month = end_date.replace(day=1)
            
            while current <= end_month: # Validates if not end of month yet
                months += 1
                if current.month == 12: # If month is December, will use Jan 1st, 2026
                    current = current.replace(year=current.year + 1, month=1)
                else:
                    current = current.replace(month=current.month + 1)
            
            return months
        except ValueError:
            return 0

    #Header
    print(f"\n{'='*30}")
    print("CLV CALCULATOR")
    print(f"{'='*30}")

    user_id = input("Enter User ID: ").strip()
    
    if user_id not in users:
        print(f"User {user_id} not found.")

    user = users[user_id]
    user_name = user["name"]
    subscriptions = user.get("subscriptions", [])

    total_revenue = 0 # Variable to accumulate revenue
    total_months = 0 # Variable to accumulate amount of months
    breakdown = []

    for sub in subscriptions:
        plan = sub["plan"]
        start = sub["start_date"]
        end = sub["end_date"]
        
        price = sporkify_plans.get(plan.strip().lower(), 0)
        months = calculate_months_subscribed(start, end)
        revenue = months * price
        
        total_months += months
        total_revenue += revenue

        breakdown.append([plan.capitalize(), months, f"Rp{revenue:,}"])

    # Print report
    print(f"\n{'='*40}")
    print(f"CLV REPORT - USER {user_id}")
    print(f"{'='*40}")
    print(f"Name: {user_name}")
    print(f"Total CLV: Rp{total_revenue:,}")
    print(f"Total Months Subscribed: {total_months} months")

    if breakdown:
        print("\nSubscription Breakdown:")
        print(tabulate(breakdown, headers=["Plan", "Months", "Revenue"], tablefmt="fancy_grid"))
    else:
        print("\nNo subscriptions found.")

## SUB-MENU 4: ACQUISITION CHANNEL PERCENTAGE
def channel_percentage(users):

    # Header
    print(f"\n{'='*40}")
    print(f"ACQUISITION CHANNEL PERCENTAGE")
    print(f"{'='*40}")
    
    #Placeholder count variable
    ads = 0
    organic = 0
    referral = 0

    # Add count into variable
    for user in users.values():
        if user["acq_channel"].lower() == "ads":
            ads += 1
        elif user["acq_channel"].lower() == "organic":
            organic += 1
        elif user["acq_channel"].lower() == "referral":
            referral += 1

    # Calculate percentage
    total = len(users)
    ads_percent = round((ads / total) * 100, 1)
    organic_percent = round((organic / total) * 100, 1)
    referral_percent = round((referral / total) * 100, 1)

    channel_table = [
        ["Ads", ads, f"{ads_percent}%"],
        ["Organic", organic, f"{organic_percent}%"],
        ["Referral", referral, f"{referral_percent}%"]
    ]
    print(tabulate(channel_table, headers=["Channel", "Users", "Percentage"], tablefmt="fancy_grid"))

### MENU OPTION 5 MAIN MENU
def subscription_insights(users):
    while True:
        print(f"\n{'='*50}")
        print("SUBSCRIPTION INSIGHT")
        print(f"{'='*50}")
        print("1. Churn Report")
        print("2. Monthly Recurring Revenue (MRR)")
        print("3. Customer Lifetime Value (CLV)")
        print("4. Acquisition Channel Percentage")
        print("5. Return to main menu")
        print(f"{'='*50}")

        choice = input("Input your selected menu (1-5): ").strip()
            
        if choice == "1":
            churn_report(users)
        elif choice == "2":
            mrr_calculator(users)
        elif choice == "3":
            clv_calculator(users)
        elif choice == "4":
            channel_percentage(users)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

### MAIN MENU
def main_menu(users):
    while True:
        print("\n" + "="*40)
        print("SPORKIFY SUBSCRIPTION ANALYSIS SYSTEM")
        print("="*40)
        print("1. Show user database")
        print("2. Add new users")
        print("3. Delete users")
        print("4. Manage subscriptions")
        print("5. Subscription Insights")
        print("6. Exit program")

        try:
            menu_input = int(input("\nSelect menu option (1-6): ").strip())
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if menu_input == 1: 
            show_user_database(users)
        elif menu_input == 2:
            add_user(users)
        elif menu_input == 3:
            delete_user(users)
        elif menu_input == 4:
            manage_subscription_menu()
        elif menu_input == 5:
            subscription_insights(users)
        elif menu_input == 6:
            print("Exiting program. Thank you!")
            return
        else:
            print(f"Invalid input! Please select 1–6.")

###### RUN PROGRAM #######
main_menu(users)