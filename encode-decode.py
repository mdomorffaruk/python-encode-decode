import base64

# Task 1: Read the file
with open('my_input.txt', 'r') as file:
    content = file.read()

# Task 2: Convert all names to base64-encoded strings
# Assuming that names are separated by spaces
names = content.split()
encoded_names = [base64.b64encode(name.encode()).decode() for name in names]

# Task 3: Add "@protonmail.com" to all encoded names
encoded_names_with_email = [f"{name}@protonmail.com" for name in encoded_names]




# Task 4: Save it to output.txt file
with open('output.txt', 'w') as file:
    for encoded_name in encoded_names_with_email:
        file.write(encoded_name + '\n')

# Task 5: Reverse the process (decoding from output.txt)
# Assuming the encoded names in output.txt are separated by newline characters
with open('output.txt', 'r') as file:
    encoded_names_with_email = file.read().splitlines()

decoded_names = []
for encoded_name_with_email in encoded_names_with_email:
    # Remove "@protonmail.com" from the encoded name
    encoded_name = encoded_name_with_email.replace('@protonmail.com', '')
    
    # Decode the base64-encoded name
    decoded_name = base64.b64decode(encoded_name.encode()).decode()
    decoded_names.append(decoded_name)


print("Name from file\t\tEncode\t\t\tDecode")
for name, encoded_name_with_email, decoded_name in zip(names, encoded_names_with_email, decoded_names):
    print(f"{name}\t\t\t{encoded_name_with_email}\t{decoded_name}")