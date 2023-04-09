"""
https://haveibeenpwned.com/API/v2#PwnedPasswords
"""

import requests
import hashlib

def check_password_security(password):
    """
    Check if password has been compromised in any known data breaches
    """

    # Pwned Passwords allows a password to be searched for by partial hash.
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    
    # Pass the first 5 characters of a SHA-1 password hash to the API.
    response = requests.get(f"https://api.pwnedpasswords.com/range/{sha1_password[:5]}")
    
    # When a password hash with the same first 5 characters is found 
    # the API will respond with an HTTP 200
    if response.status_code == 200:

        # Every hash beginning with the specified prefix, 
        # followed by a count of how many times it appears 
        # in the data set.
        for line in response.text.splitlines():
            if sha1_password[5:] == line.split(':')[0]:

                # Return the number of times the password was found
                # in the database.
                return int(line.split(':')[1])
            
        # The password does not exist in the data set.
        return 0
    
    else:

        # The password does not exist in the data set.
        return 0