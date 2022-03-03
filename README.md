# One Time Pad
This program was built in Python 3.9. It functions by first taking in 2 required arguments: A Plaintext File location, and a Ciphertext file location. A third optional argument (the key) can also be provided if the user is needing to decrypt via XOR. 

This program functions as a One Time Pad. The user inputs a file containing plaintext. A cryptographically secure key is randomly generated via the 'sercets' module, that is the identical length of the plaintext itself. The plaintext is then XOR'd with the key to create the corresponding ciphertext. The ciphertext is then written to a file, and the key displayed to the user for decryption purposes

The user can then decrypt this file (or any file, so long as it was encrypted via XOR and the key is provided) by running this same program with the -k <key> option

## Compatability
Made in Python 3.9
Tested on Windows 10

## Options
* -h                 Displays Help Regarding how to run the cmd
* -c/--cipherfile    Required: Specify a textfile where the ciphertext will be written to (encryption) or read from (decryption)
* -p/--plainfile     Required: Specify a textfile where the plaintext will be written to (decryption) or read from (encryption)
* -k/--key           Optional: The key used for decryption
  
## Quickstart
1) Download the .ZIP File and extract to a directory of your choice
2) Run the program with appropriate options i.e.
```python3 main.py -c Ciphertext.txt -p Plaintext.txt -k 23523652615262623456236432```

# Purpose
This purpose of this program is to simulate the One Time Pad encryption technique. So long as the key is randomly generated, kept secure, and is at least as long as the plaintext, this encryption is unconditionally secure. 

# Example Output
![image](https://user-images.githubusercontent.com/77559638/156482554-ae546fca-5046-4508-a912-f218b6f76e13.png)
![image](https://user-images.githubusercontent.com/77559638/156482595-68d09ba7-8fe7-4f49-b4fa-dc816fa69f08.png)



