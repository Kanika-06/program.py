def find_min_max(numbers):
    if not numbers:
        return None, None

    min_val = numbers[0]
    max_val = numbers[0]

    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val
