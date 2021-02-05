#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import datetime

# decoration
print(stylize("\n---- | Execution time of any code | ----\n", fg("red")))

# start time
start = datetime.datetime.now()

### Your code here ###
def fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(36)

### -------------- ###

# execution time
execution_time = str(datetime.datetime.now() - start)

# output
print(stylize("Your code has an execution time of:", fg("green")))
print(f"{execution_time[0]} - hours\n{execution_time[2:4]} - minute/s\n{execution_time[5:7]} - seconds\n{execution_time[8:]} - microseconds\n")
