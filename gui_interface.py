import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *
 
import random
def generate_otp(length):
    """
    Generates a One Time Password (OTP) of a specified length.
    
    Args:
    length (int): The length of the OTP to be generated.
    
    Returns:
    str: The generated OTP.
    """
    # Define the possible characters for the OTP
    characters = "0123456789"
    
    # Generate the OTP using random.choices which returns a list of randomly selected characters
    otp_list = random.choices(characters, k=length)
    
    # Join the list of characters into a single string to form the OTP
    otp = ''.join(otp_list)
    
    return otp

# Main program execution starts here
if __name__ == "__main__":
    # Get user input for the length of OTP
    length = int(input("Enter the length of the OTP: "))
    
    # Generate the OTP
    otp = generate_otp(length)
    
    # Print the generated OTP
    print("Generated OTP:", otp)


root = Tk() 
var = IntVar() 
var1 = IntVar() 
 
root.title("Random Password Generator") 

Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
 
c_label = Label(root, text="Length") 
c_label.grid(row=1) 
 

generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=2) 
copy_button = Button(root, text="Copy", command=copy) 
copy_button.grid(row=0, column=3)
combo = Combobox(root, textvariable=var1)
combo['values'] = (12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32,) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1)
 
 
root.mainloop()
