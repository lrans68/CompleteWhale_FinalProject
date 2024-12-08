# main.py 

# Name: Ryan Dew, Luke Ransick, Connor MacFarland, Anthony Caggiano
# email: dewrm@mail.uc.edu, caggiaaj@mail.uc.edu, ransiclg@mail.uc.edu, macfarct@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This is the final project for the class, we were given a task to decrypt a location on UC campas and a movie title. We were given 3 files to use, 2 json files with excrypted information and a txt file that was used as a index for the encrypted information. We were also given a key to decrypt the movie title.

# Brief Description of what this module does: This module is the main module that invokes the functions from the decryptionGroup and decryptionMovie packages to decrypt the location and movie title respectively. It also loads and displays the images.
# Citations: Microsoft Copiolt, https://cryptography.io/en/latest/fernet/ --> fernet key information, https://pypi.org/project/pillow/ --> image display, https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/ --> fernet key information, understanding how it works, 
# Anything else that's relevant: We display two images in this module, just for clarity.

from decryptionGroupPackage.decryptionGroup import decrypt_location
from decryptionMoviePackage.decryptionMovie import decrypt_movie
from PIL import Image

def main():
    # Decrypt the location
    encrypted_group_file = 'data/EncryptedGroupHints Fall 2024 Section 001.json'
    english_file = 'data/UCEnglish.txt'
    team_name = 'Complete Whale'
    decrypted_location = decrypt_location(encrypted_group_file, english_file, team_name)
    print(f'CompleteWhale Decrypted Location: {decrypted_location}')
        
    # Decrypt the movie name
    encrypted_movie = "gAAAAABnJ6xXNfNlCIllzI4Wrsu7_yAgjjMeS7NstUWkMpyXn2z_j0hqav_M4lNcpwH-MIbcMoN30OB_0q8yPDyKNzZh1yDygBU5wvnS0wyx2Txa12WTwpQ="  # encrypted movie string
    key = "OYu19RxF9QJhFklueUCr4b4q8cgR5-1-qVJvLNXH9QA="  # Fernet key
    decrypted_movie = decrypt_movie(encrypted_movie, key)
    print(f'CompleteWhale Decrypted Movie: {decrypted_movie}')
   

    # Load and display the images
    image1_path = 'data/Photo1.jpg'  # Replace with file name
    image2_path = 'data/Photo2.jpg'  # Replace with file name
   
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
   
    image1.show()
    image2.show()


if __name__ == '__main__':
    main()
