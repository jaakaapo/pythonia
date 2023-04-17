import statistics

data = [1.3, 2.7, 0,8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

values_below_avg = list(filter(lambda x: x < avg, data))
values_above_avg = list(filter(lambda x: x > avg, data))

print(values_below_avg)
print(values_above_avg)

countries = ["", "Brazil", "", "Chile"]

filteret_list = list(filter(None, countries))
print(filteret_list)