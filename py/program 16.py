input_string = "hello, world!"
frequency_dict = {}
for char in input_string:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1
print(f"Character frequency in '{input_string}':")
for char, freq in frequency_dict.items():
    print(f"'{char}': {freq}")