# 🟢 Subscription Analytics Tool
A Python-based CRUD program designed as a case study simulating the management and analytics for a mock subscription-based service. This program replicates how administrators can manage user records and derive analysis from subscriber data.

## Project Overview
Provides a simplified demonstration of how subsciption-based businesses might manage and analyze their customer data and acquire insights.
- **CRUD Functionality:** Create, Read, Update, and delete users to and from the database
- **Subscription Management:** Track subscription history, manage plan, start/stop dates, and user data.
- **Insights & Reports:** Report key subscription metrics such as churn rate, CLV, MRR, and acquisition channels.

## Case Study

<div align="center">
  <img src="https://github.com/ariq-ojan/subscription-analytics/blob/main/sporkify_banner.png" width='640'>
</div>

Sporkify is a recently launched subscription-based music streaming platform catered to music enthusiasts. They promotes sustainable business practices in the music industry, ensuring artists and musicians are paid faiarly. They have also been found to run anti-authoritarian ads.

Since their IT infrastructures aren't fully set up yet, **the customer and product team** requires a tool to manage all subscriptions and generate reports up until **January 1st, 2026**.

## Functions
### User Management
- `show_user_database(users)` → Display a summary view of all users  
- `add_user(users)` → Add new user to database  
- `delete_user(users)` → Delete user from database  

### Subscription Management
- `view_subscription_history(user_id)` → Display full subscription history of a user  
- `start_subscription_function(user_id)` → Start a new subscription  
- `stop_subscription_function(user_id)` → Stop an active subscription  
- `update_plan(user_id)` → Change the plan of an active subscription  
- `change_name(user_id)` → Update user's name  

### Subscription Insights
- `churn_report(users)` → Generate churn report and churn rate  
- `mrr_calculator(users)` → Calculate monthly recurring revenue (MRR)  
- `clv_calculator(users)` → Calculate customer lifetime value (CLV)  
- `channel_percentage(users)` → Show percentage breakdown of acquisition channels

## Database Structure
```python
  {
    "1": {                             # user_id and key of the dictionary
    "name": "Ali Susanto",             # Username
    "acq_channel": "Referral",         # Acquisition channel (Referral/Ads/Organic)
    "subscriptions": [                 # List of subs stored in a dictionary
        {"plan": "Basic",              # Available plans (Basic/Pro/Ultimate)
         "start_date": "2025-01-01",
         "end_date": "2025-06-30",
         "status": "Inactive"},        # Status of subscription (Active/Inactive)
        {"plan": "Pro",               
         "start_date": "2025-07-01",
         "end_date": None,        
         "status": "Active"}
        ]
    }  
  ```






