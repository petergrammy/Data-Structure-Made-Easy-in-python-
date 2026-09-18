def daily_temperatures(temperatures: list[int]) -> list[int]:
    res=[0]*len(temperatures)
    stack=[]
    for current_day,current_temp in enumerate(temperatures):
        while(stack and
              current_temp>temperatures[stack[-1]]
              ):
            previous_day=stack.pop()
            res[previous_day]=current_day-previous_day
        stack.append(current_day)
    return res

print(daily_temperatures([67,68,98,22,66]))