import random

def generate_otp(length):
    # Define the possible characters for the OTP
    characters = "0123456789"
    
    # Generate the OTP using random.choices
    otp = ''.join(random.choices(characters, k=length))
    
    return otp

# Get user input for the length of OTP
length = int(input("Enter the length of the OTP: "))

# Generate and print the OTP
otp = generate_otp(length)
print("Generated OTP:", otp)
