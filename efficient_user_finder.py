import csv
import data


filename = "logs/" + data.workflow_name + ".log"
log_fields = []
log_rows = []

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    log_fields = next(csvreader)
    for csv_row in csvreader:
        log_rows.append(csv_row)

user_activity_mapping = {}
current_step_key = log_fields[data.current_step_field_index]
next_step_key = log_fields[data.next_step_field_index]
step_time_key = log_fields[data.step_time_field_index]
steps_info_key = "STEPS INFO"
total_time_key = "TOTAL TIME"

for log_row in log_rows:
    user_id = log_row[data.user_id_field_index]
    if user_id not in user_activity_mapping:
        current_step = log_row[data.current_step_field_index]
        step_time = "0ms"
        step_info = {current_step_key: current_step, step_time_key: step_time}
        user_activity_mapping[user_id] = {}
        user_activity_mapping[user_id][steps_info_key] = [step_info]
        user_activity_mapping[user_id][total_time_key] = int(step_time[:-2])

    next_step = log_row[data.next_step_field_index]
    step_time = log_row[data.step_time_field_index]
    step_info = {current_step_key: next_step, step_time_key: step_time}
    user_activity_mapping[user_id][steps_info_key].append(step_info)
    user_activity_mapping[user_id][total_time_key] += int(step_time[:-2])

all_total_steps = [
    len(user_info[steps_info_key]) for user_info in user_activity_mapping.values()
]
min_total_steps = min(all_total_steps)
max_total_steps = max(all_total_steps)

efficient_user_ids = [
    user_id
    for user_id, user_info in user_activity_mapping.items()
    if len(user_info[steps_info_key]) == min_total_steps
]

inefficient_user_ids = [
    user_id
    for user_id, user_info in user_activity_mapping.items()
    if len(user_info[steps_info_key]) == max_total_steps
]


def display_user_info(user_id):
    print(f"User: {user_id}")
    print(f"Total steps taken: {len(user_activity_mapping[user_id][steps_info_key])}")
    print("Followed path:")
    steps_info = user_activity_mapping[user_id][steps_info_key]
    for index, step_info in enumerate(steps_info):
        if index < len(steps_info) - 1:
            print(f"{step_info[current_step_key]} --> ", end="")
        else:
            print(f"{step_info[current_step_key]}")
    print()


print("\n\nInefficient Users:\n\n")
for user_id in inefficient_user_ids:
    display_user_info(user_id)

print("\n\nEfficient Users:\n\n")
for user_id in efficient_user_ids:
    display_user_info(user_id)
