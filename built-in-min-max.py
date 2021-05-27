def minimum(value1, value2, value3, value4):
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    return min_value
# print(" minimum value is: " + str(minimum(15, 9, 27, 14)))


def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value
# print(maximum(12, 27, 36))

min_value = min(15, 9, 27, 14)
# print(min_value)

max_value = max(12, 27, 36)
# print(max_value)

# print(" minimum value is: {}\n maximum value is: {}".format(minimum(15, 9, 27, 14), maximum(12, 27, 36)))

# print("\n\n\n minimum value is: {}\n maximum value is: {}\n minimum value is: {}\n maximum value is: {}".format(minimum(15, 9, 27, 14), maximum(12, 27, 36), min_value, max_value))

print("\n\n\n minimum value is: {}\n \
maximum value is: {}\n \
minimum value is: {}\n \
maximum value is: {}".format(
    minimum(15, 9, 27, 14),
    maximum(12, 27, 36),
    min_value,
    max_value))
