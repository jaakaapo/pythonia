temps = [("Helsinki", 1), ("Berlin", 10), ("Cairo", 36)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)


print(list(map(c_to_f, temps)))