# =============================================================================
# Program: 		Cutover_Verification_assistant.py
# Author: 		Aaron Carroll
# Created: 		2025-01-09
# Purpose: 		This program is meant to serve as an assistant cutting over a 
#               switch. It will connect to the switch and pull all active non 
#               trunking interfaces, there respective MAC address and then
#               connect to the cores and resolve the IP address of the MAC.
#               This data will be store as a CSV and YAML file for the name 
#               you choose. You will be able to also verify all connectins 
#               came back after by selecting the verify opion and giving 
#               the path to the previously create CSV or YAML file. 
# =============================================================================
import os
import netmiko

def get_users_objective() -> int:
    while True:
        # Display the prompt and capture the user input
        try:
            option = int(input(f"""
Select from the following: \n\n
{"Description":<45} | {"Option":<20}
-------------------------------------------------------
{"Verify endpoints are UP":<45} | {"1":<20}
{"Create CSV and YAML of connected endpoints":<45} | {"2":<20}
\nInput: """))
            # Check if the input is valid (either 1 or 2)
            if option == 1 or option == 2:
                return option
            else:
                print("\nInvalid option, please select 1 or 2.")
        except ValueError:
            # Handle case where input is not a valid integer
            print("Invalid input, please enter a number.")

def get_file_path() -> str:
    while True:
        try:
            file_path = input("Please enter the file path to the endpoints you wish to test (Can be a relative path): ")        
            if os.path.isfile(file_path):
                return file_path
            else:
                print("Invalid file path please try again")
        except ValueError:
            print("Ivalid input, Please enter an existing file path")


def main():
    user_input = get_users_objective()
    
    # If user selected to verify endpionts using ICMP after cutover
    if(user_input == 1):
        endpoint_file_path = get_file_path()
        print("finish this selection")
    else:
        
# Run the main function
if __name__ == "__main__":
    main()
