# decriptionGroup.py

# Name: Ryan Dew, Luke Ransick, Connor MacFarland, Anthony Caggiano
# email: dewrm@mail.uc.edu, caggiaaj@mail.uc.edu, ransiclg@mail.uc.edu, macfarct@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This is the final project for the class, we were given a task to decrypt a location on UC campus and a movie title. We were given 3 files to use, 2 json files with excrypted information and a txt file that was used as a index for the encrypted information. We were also given a key to decrypt the movie title.

# Brief Description of what this module does: This module decrypts the location of the specified team using the indices in the encrypted data and the English words from the text file.
# Citations: Microsoft Copiolt, https://cryptography.io/en/latest/fernet/ --> fernet key information, https://pypi.org/project/pillow/ --> image display, https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/ --> fernet key information, understanding how it works, 
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