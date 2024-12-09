# decriptionMovie.py

# Name: Ryan Dew, Luke Ransick, Connor MacFarland, Anthony Caggiano
# email: dewrm@mail.uc.edu, caggiaaj@mail.uc.edu, ransiclg@mail.uc.edu, macfarct@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment:  This is the final project for the class, we were given a task to decrypt a location on UC campas and a movie title. We were given 3 files to use, 2 json files with excrypted information and a txt file that was used as a index for the encrypted information. We were also given a key to decrypt the movie title.

# Brief Description of what this module does: This module has a function that decrypts the movie title using the Fernet key provided in the main module.
# Citations: Microsoft Copiolt, https://cryptography.io/en/latest/fernet/ --> fernet key information, https://pypi.org/project/pillow/ --> image display, https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/ --> fernet key information, understanding how it works, 
# Anything else that's relevant: None

import json
from cryptography.fernet import Fernet

def load_encrypted_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_encrypted_movie(encrypted_data, team_name):
    # Ensure the team_name exists in the encrypted data
    if team_name in encrypted_data:
        return encrypted_data[team_name][0]  # Access the first element in the list
    else:
        raise KeyError(f"Team name '{team_name}' not found in the encrypted data.")

def decrypt_movie_title(encrypted_title, key):
    fernet = Fernet(key)
    decrypted_title = fernet.decrypt(encrypted_title.encode()).decode()
    return decrypted_title
