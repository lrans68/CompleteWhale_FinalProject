# main.py 

# Name: Ryan Dew, Luke Ransick, Connor MacFarland, Anthony Caggiano
# email: dewrm@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment:
# Brief Description of what this module does:
# Citations: 
# Anything else that's relevant: None

from decryptionGroupPackage.decryptionGroup import decrypt_location
from decryptionMoviePackage.decryptionMovie import decrypt_movie


def main():
    # Decrypt the location
    encrypted_group_file = 'data/EncryptedGroupHints Fall 2024 Section 001.json'
    english_file = 'data/UCEnglish.txt'
    team_name = 'Complete Whale'  # Replace with the actual team name
    decrypted_location = decrypt_location(encrypted_group_file, english_file, team_name)
    print(f'CompleteWhale Decrypted Location: {decrypted_location}')
        
    # Decrypt the movie name
    encrypted_movie = "gAAAAABnJ6xXNfNlCIllzI4Wrsu7_yAgjjMeS7NstUWkMpyXn2z_j0hqav_M4lNcpwH-MIbcMoN30OB_0q8yPDyKNzZh1yDygBU5wvnS0wyx2Txa12WTwpQ="  # Replace with actual encrypted movie string
    key = "OYu19RxF9QJhFklueUCr4b4q8cgR5-1-qVJvLNXH9QA="  # Replace with actual Fernet key
    decrypted_movie = decrypt_movie(encrypted_movie, key)
    print(f'CompleteWhale Decrypted Movie: {decrypted_movie}')

   
if __name__ == '__main__':
    main()