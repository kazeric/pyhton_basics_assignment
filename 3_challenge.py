user_inputs = []

for i in range(5):
    user_in = input(f'Enter a value {i}')
    user_inputs.append(user_in)
    print(user_inputs)

unique_inputs = set(user_inputs)
print(f"unique_inputs are: {unique_inputs}")