# encrypted-keylogger
Keylogger with Encrypted Keystrokes
This project is a simple keylogger that encrypts the captured keystrokes using the FERNET algorithm and stores them in a text file. The purpose of this project is to secure the captured data by making it unreadable without the decryption key.
Features
Captures keystrokes from all active windows
Encrypts captured keystrokes using the FERNET algorithm
Stores encrypted keystrokes in a text file
Uses a secure decryption key to decrypt the captured data
Installation
Clone the repository to your local machine
Install the required dependencies by running pip install -r requirements.txt
Run the keylogger.py script to start the keylogger
Usage
The keylogger will start capturing keystrokes from all active windows
The captured keystrokes will be encrypted using the FERNET algorithm
The encrypted keystrokes will be stored in a text file named keystrokes.txt
To decrypt the captured data, you will need to use the decryption key that is provided in the decryption_key.txt file
Security
The captured keystrokes are encrypted using the FERNET algorithm, which is a symmetric encryption algorithm that uses a secure key to encrypt and decrypt data. The decryption key is stored in a separate file named decryption_key.txt to prevent unauthorized access to the captured data.
It is important to note that the use of this project may be illegal in certain jurisdictions. Please ensure that you are in compliance with all applicable laws and regulations before using this project.
