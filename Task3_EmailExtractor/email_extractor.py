import re

# Open the input text file
with open("input.txt", "r") as file:
    text = file.read()

# Find all email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save email addresses to another file
with open("emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Email addresses found:\n")

for email in emails:
    print(email)

print("\nAll email addresses have been saved to emails.txt")
