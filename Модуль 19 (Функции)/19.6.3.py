# (вес, рост)
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]
print (sorted(data, key = lambda x: x[0] / (x[1]/100) ** 2))
print(min(data, key=lambda x: x[0] / x[1] ** 2))

a = ["asd", "bbd", "ddfa", "mcsa"]
print(list(map(len,a)))
