import string
input_string = "Hello, world! This is an example string with punctuation."
translator = str.maketrans('', '', string.punctuation)
clean_string = input_string.translate(translator)
print(f"Original string: {input_string}")
print(f"String without punctuation: {clean_string}")
