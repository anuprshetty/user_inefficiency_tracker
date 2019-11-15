# User Inefficiency Tracker

This application is used to know the efficient and inefficient users for the given workflow.

## How to run?

- Run user_activity_generator.py file to generate user activity log in logs folder. To know the structure of log file, please see user_activity.log file on root directory.
- Run efficient_user_finder.py to know inefficent and efficient users for the Payslip download workflow.

## Output for the above log file --> **user_activity.log**

Inefficient Users:

User: user_2  
Total steps taken: 8  
Followed path:  
Philips Home Page --> Componsation Viewer --> View My Benefits --> Advance Salary Viewer --> Tax Calculator --> Financial Year --> Payslips Viewer --> Payslips Download

User: user_9  
Total steps taken: 8  
Followed path:  
Philips Home Page --> Tax Viewer --> ADP Viewer --> Advance Salary Viewer --> Tax Calculator --> Notice Pay Reimbursement --> Payslips Viewer --> Payslips Download

Efficient Users:

User: user_4  
Total steps taken: 4  
Followed path:  
Philips Home Page --> View My Pay --> Tax Calculator --> Payslips Download

User: user_7  
Total steps taken: 4  
Followed path:  
Philips Home Page --> Work Day Home Page --> Tax Calculator --> Payslips Download

User: user_8  
Total steps taken: 4  
Followed path:  
Philips Home Page --> Intranet --> Payslips Viewer --> Payslips Download
