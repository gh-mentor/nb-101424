"""
This module contains a Python function that simulates a workload. It uses a loop to iterate through a given number of steps, where each step involves a random sleep time between 0.5 and 1.5 seconds. The function prints a message indicating the completion of each step.
"""


import random
import time

"""
Create a Python function named 'simulate_load' that simulates a workload.
Arguments:
- 'workload': an integer representing the number of steps in the workload
Returns: NONE
Details:
- Use a 'loop' to simulate a workload by iterating from the given workload value down to 1. 
- For each iteration, it performs the following steps:
    1) Generates a random sleep time between 0.5 and 1.5 seconds.
    2) Pauses the execution for the generated sleep time.
    3) Prints a message indicating the completion of the current step.
Usage:
simulate_load(10); # Simulates a workload with 10 steps
"""

def simulate_load(workload):
    for i in range(workload, 0, -1):
        sleep_time = random.uniform(0.5, 1.5)
        time.sleep(sleep_time)
        print(f"Step {i} completed.")

