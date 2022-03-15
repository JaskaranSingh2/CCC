# Person 1
# a steps forward, b steps backward

# Person 2
# c steps forward, d steps backward

# a >= b
# c >= d
# Same total number of steps, not same distance
# Nicky and Byron both step forward on their first steps at the same time

"""
what I need to do:
The position from start for one sequence is a-b/c-d
The total number of steps is a+b/c+d while it does not equal S
The total number of steps must not exceed S
If a+b/c+d adds to make the total number of steps greater than S, then we will add S - total number of steps
"""
