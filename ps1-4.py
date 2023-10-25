def Least_moves(x):
    current_amount = 1 
    steps = 0  # 步数

    while current_amount < x:
        if current_amount * 2 <= x:
            current_amount *= 2 
        else:
            current_amount += 1 
        steps += 1  # 步数加一

    return steps

