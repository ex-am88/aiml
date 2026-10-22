
def f(x):
    return -(x - 5) ** 2 + 25

x = 0

while True:
    left = f(x - 1)
    right = f(x + 1)

    if left > f(x):
        x -= 1
    elif right > f(x):
        x += 1
    else:
        break

print("Maximum point:", x)
print("Maximum value:", f(x))
