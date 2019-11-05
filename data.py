users_count = 10
workflow_total_steps = 20
min_step_time_in_ms = 10
max_step_time_in_ms = 100
min_wait_time_in_ms = 500
max_wait_time_in_ms = 2000

workflow_name = "user_activity"

event_mapping = {
    0: "Philips Home Page",
    1: "Intranet",
    2: "HR Portal",
    3: "My Viewer",
    4: "My Profile",
    5: "Componsation Viewer",
    6: "Tax Viewer",
    7: "Work Day Home Page",
    8: "ADP Viewer",
    9: "Work Day Profile",
    10: "My Information",
    11: "View My Pay",
    12: "View My Benefits",
    13: "My Statements",
    14: "My Reimbursement Statements",
    15: "Advance Salary Viewer",
    16: "Tax Calculator",
    17: "Financial Year",
    18: "Notice Pay Reimbursement",
    19: "Payslips Viewer",
    20: "Payslips Download",
}

user_id_field_index = 2
current_step_field_index = 3
next_step_field_index = 4
step_time_field_index = 5
