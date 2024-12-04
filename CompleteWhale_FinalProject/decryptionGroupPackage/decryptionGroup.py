# decriptionGroup.py

# Name: Ryan Dew, Luke Ransick, Connor MacFarland, Anthony Caggiano
# email: dewrm@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: 

# Brief Description of what this module does.
# Citations: 
# Anything else that's relevant: None

import json

def load_english_words(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def decrypt_location(encrypted_file, english_file, team_name):
    # Load the encrypted data from the JSON file
    with open(encrypted_file, 'r') as ef:
        encrypted_data = json.load(ef)
    
    # Load the English words from the text file
    english_words = load_english_words(english_file)
    
    # Decrypt the location using the indices in the encrypted data for the specified team
    decrypted_message = []
    for index in encrypted_data['CompleteWhale']:
        word = english_words[int(index)].strip()
        decrypted_message.append(word)
    
    return ' '.join(decrypted_message)