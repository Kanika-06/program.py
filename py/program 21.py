numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
element_to_count = 5
count = 0
for item in numbers:
    if item == element_to_count:
        count += 1
print(f"Element {element_to_count} occurs {count} times in the list.")
