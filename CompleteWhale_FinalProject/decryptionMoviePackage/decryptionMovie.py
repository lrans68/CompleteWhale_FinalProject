# decriptionMovie.py

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


from cryptography.fernet import Fernet

def decrypt_movie(encrypted_movie, key):
    fernet = Fernet(key)
    decrypted_movie = fernet.decrypt(encrypted_movie.encode()).decode()
    return decrypted_movie

