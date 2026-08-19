# String formatting
template = "Dear {}, Good morning. Take this {} Rupee bag"
a = "Ronak"
a1 = 10000
b = "Teja"
b1 = 1000
c = "Rahi"
c1 = 300

# Template string formatting.
s1 = template.format(a, a1)
print(s1)

# f-string formatting.
print(f"{c} you are awesome and take this {c1} Rs bag")