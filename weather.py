monthly_average_temp = {'jan': 66, 'feb': 68,'mar': 73, 'apr': 79,
                'may': 88, 'jun': 91, 'july': 95, 'aug': 97,
                'sep': 91, 'oct': 84, 'nov': 77, 'dec': 70}

vals = monthly_average_temp.values()

top_range = 81

high = dict()


def ave_temp(year):
    total = 0
    for temp in year:
        total += year[temp]
    ave = total / len(monthly_average_temp)
    print("The average temperature in Dubi is " + str(ave))


def over(today):
    global top_range
    for temp in today:
        if today[temp] > top_range:
            high[temp] = (today[temp])
    print high

ave_temp(monthly_average_temp)
over(monthly_average_temp)


