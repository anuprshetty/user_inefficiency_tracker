import random
from log_generator import logger_obj
import data
import time

for user_id in range(1, data.users_count + 1):
    current_step = 0
    end_step = data.workflow_total_steps
    while current_step < end_step:
        next_step = random.randint(current_step + 1, end_step)
        step_time_in_ms = random.randint(
            data.min_step_time_in_ms, data.max_step_time_in_ms
        )

        log_message = f"user_{user_id},{data.event_mapping[current_step]},{data.event_mapping[next_step]},{step_time_in_ms}ms"
        logger_obj.info(log_message)

        wait_time_in_ms = random.randint(
            data.min_wait_time_in_ms, data.max_wait_time_in_ms
        )
        time.sleep(wait_time_in_ms // 1000)

        current_step = next_step
