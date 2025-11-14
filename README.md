# 🟢 Subscription Management & Analytics Tool

### About This Tool
A Python-based CRUD program designed as a case study simulating the management and analytics for a mock subscription-based service. This program replicates how administrators can manage user records and derive analysis from subscriber data.

Access the full source code [here!](https://github.com/ariq-ojan/subscription-analytics/blob/main/sporkify_subscriber_analytics_tool.py)

## 📍Project Overview
Provides a simplified demonstration of how subsciption-based businesses might manage & analyze their customer data and acquire insights.
- **CRUD Functionality:** Create, Read, Update, and delete users to and from the database
- **Subscription Management:** Track subscription history, manage plan, start/stop dates, and user data.
- **Insights & Reports:** Report key subscription metrics such as churn rate, CLV, MRR, and acquisition channels.

## 🎧 Case Study
<div align="center">
  <img src="https://github.com/ariq-ojan/subscription-analytics/blob/main/new_sporkify_banner.png">
</div>

Sporkify is a recently launched subscription-based music streaming platform catered to music enthusiasts. Unlike the competition, they promote sustainable business practices in the music industry, ensuring artists and musicians are paid faiarly.

Since their IT infrastructures aren't fully set up yet, **the customer and product team** requires a tool to manage all subscriptions and generate simple reports up until **January 1st, 2026**.

## ⚙️ Main Features
### 👥 User Management
- `show_user_database(users)` → Display a summary view of all users  
- `add_user(users)` → Add new user to database  
- `delete_user(users)` → Delete user from database  

### 📂 Subscription Management
- `view_subscription_history(user_id)` → Display full subscription history of a user  
- `start_subscription_function(user_id)` → Start a new subscription  
- `stop_subscription_function(user_id)` → Stop an active subscription  
- `update_plan(user_id)` → Change the plan of an active subscription  
- `change_name(user_id)` → Update user's name  

### 💰 Subscription Insights
- `churn_report(users)` → Calculate percentage of churned users / total users at end of year
- `mrr_calculator(users)` → Calculate recurring revenue each month, divided per plan 
- `clv_calculator(users)` → Calculate a user's lifetime value at end of year 
- `channel_percentage(users)` → Show percentage breakdown of acquisition channels

## 👤 User Data Structure
```python
  {
    "1": {                             # user_id and key of the dictionary
    "name": "Ali Susanto",             # Username
    "acq_channel": "Referral",         # Acquisition channel (Referral/Ads/Organic)
    "subscriptions": [                 # List of subs stored in a dictionary
        {"plan": "Basic",              # Available plans (Basic/Pro/Ultimate)
         "start_date": "2025-01-01",   # Subscription start date in string type
         "end_date": "2025-06-30",     # Subscription end date in string type 
         "status": "Inactive"},        # Status of subscription (Active/Inactive)
        {"plan": "Pro",               
         "start_date": "2025-07-01",
         "end_date": None,        
         "status": "Active"}
        ]
    }  
  ```
The program contains **10 hard-coded existing subscribers data**. New users can be added using the "Add New User" menu.

## ⚠️ Limitations
- Program is restricted to the year of 2025, current time is **frozen at December 31st, 2025.**
- As a mockup, this program does not have any memory, any changes made to the database **will be lost after exit.**

## ❓ How to Use

### Main Menu
```python
========================================
SPORKIFY SUBSCRIPTION ANALYTICS TOOL
========================================
1. Show user database
2. Add new users
3. Delete users
4. Manage subscriptions
5. Subscription Insights
6. Exit program

Select menu option (1-6):
```
Users can select their desired menu option by entering their menu numbers in the terminal. This will be the main way to navigate the menus throughout the program.

### Manage Subscription Menu

```python

Enter User ID:

==================================================
SUBSCRIPTION MANAGEMENT - User Name (ID: User ID)
==================================================
1. View Subscription History
2. Start New Subscription
3. Stop Current Subscription
4. Change Plan
5. Change Name
6. Back to Main Menu
==================================================
Input your selected menu (1-6):
```
Upon selecting this menu, users will be shown a list of User IDs and their respective names. They will next be asked to input user ID which will be used for all the sub-functions of this menu. 

### Subscription Insight Menu
```python

==================================================
SUBSCRIPTION INSIGHT
==================================================
1. Churn Report
2. Monthly Recurring Revenue (MRR)
3. Customer Lifetime Value (CLV)
4. Acquisition Channel Percentage
5. Return to main menu
==================================================
Input your selected menu (1-5):
```
Some options from this menu will ask users to enter a specific month (1-12) or a User ID.


## 💻 Installation

The tool provided in the download page is an executable (.exe) or in a python (.py) format, they **do not require any installation**. 

Requirements:
- [Python 3.10 or above](https://www.python.org/downloads/)
- [Tabulate Library](https://pypi.org/project/tabulate/)

## 🔮 Features Coming Soon!
1. Saving data to files (Program will remember changes after exit)
2. SQL database migration
3. CSV Import/Export
4. Graphical User Interface (GUI)
5. Advanced Analytics: Cohort Analysis, Custom Date Ranges for all functions

## ##
© 2025 Ariq Fauzan. All rights reserved
You’re free to use, modify, and distribute this project with proper attribution.

📧 Email: [mariqfauzan@gmail.com](mailto:mariqfauzan@gmail.com)  
💼 LinkedIn: [Ariq Fauzan](https://www.linkedin.com/in/ariq-fauzan/)
