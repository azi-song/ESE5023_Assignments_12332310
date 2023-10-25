import numpy as np
def Find_expression(target, expression="", current_num=0, next_num=1):
    if next_num == 10:  
        if current_num == target:
            print(expression)
        return
    
    Find_expression(target, expression + "+" + str(next_num), current_num + next_num, next_num + 1)
    Find_expression(target, expression + "-" + str(next_num), current_num - next_num, next_num + 1)
    Find_expression(target, expression + str(next_num), int(str(current_num) + str(next_num)), next_num + 1)


for i in range(1, 101):
    print("Target:", i)
    Find_expression(i)
    print()
    
from collections import Counter
Total_solutions = []
for i in range(1, 101):
    c = Counter(Find_expression(i),1)
    Total_solutions.append(c)
    print()

print("Total_solutions:", Total_solutions)

max_count = max(Total_solutions)
min_count = min(Total_solutions)
max_index = Total_solutions.index(max_count) + 1
min_index = Total_solutions.index(min_count) + 1

print("The maximum number of solutions is {max_count}, which occurs for the number {max_index}.")
print("The minimum number of solutions is {min_count}, which occurs for the number {min_index}.")