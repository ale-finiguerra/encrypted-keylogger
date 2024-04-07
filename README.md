# Keylogger with Encrypted Keystrokes 🔒

This project is a keylogger that captures keystrokes from all active windows and encrypts them using the FERNET algorithm to ensure the security and privacy of the captured data.

## Features

- Captures keystrokes from all active windows
- Encrypts captured keystrokes using the FERNET algorithm
- Stores encrypted keystrokes in a text file named `keystrokes.txt`
- Uses a secure decryption key to decrypt the captured data
- Provides a secure and private way to record keystrokes

## Installation

1. Clone the repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Run the `keylogger.py` script to start the keylogger

## Usage

1. The keylogger will start capturing keystrokes from all active windows
2. The captured keystrokes will be encrypted using the FERNET algorithm
3. The encrypted keystrokes will be stored in a text file named `keystrokes.txt`
4. To decrypt the captured data, you will need to use the decryption key that is provided in the `decryption_key.txt` file

## Security

The captured keystrokes are encrypted using the FERNET algorithm, which is a symmetric encryption algorithm that uses a secure key to encrypt and decrypt data. The decryption key is stored in a separate file named `decryption_key.txt` to prevent unauthorized access to the captured data.

It is important to note that the use of this project may be illegal in certain jurisdictions. Please ensure that you are in compliance with all applicable laws and regulations before using this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file
