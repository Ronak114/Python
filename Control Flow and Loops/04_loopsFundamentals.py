# break
for i in range(0, 21):
    print(i)
    if i == 11:
        break  # Cancel the execution of this loop now

# continue
for i in range(1, 20):
    if i == 10:
        continue  # continue the loop for the next iteration(skip the current iteration)
    print(i)

# pass
i = 3
if i == 32:
    pass  # do nothing
print("End of program")
