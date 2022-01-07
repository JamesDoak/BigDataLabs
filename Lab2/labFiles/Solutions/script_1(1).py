def power(value, power):
    result = 1
    for i in range(0, power):
        result = result * value
    return result

print(power(2,3))
print(power(10,4))

