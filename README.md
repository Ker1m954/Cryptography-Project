<div align="center">
  <img src="https://img.shields.io/github/languages/count/Ker1m954/Cryptography-Project?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/Ker1m954/Cryptography-Project?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/Ker1m954/Cryptography-Project?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/Ker1m954/Cryptography-Project?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# ENCRYPTION AND DECRYIPTION TOOL FOR PYTHON

*A simple but well written code for Pyhton that you can use for both encryiption and decryption*

---

## Features

- **Feature 1:** Simple, but very useful.

- **Feature 2:** Our code is specially modificated for user-friendly-command-line interface. Allowing non-programmers to interact with the code at easily.


---

## Our Team

- **232****033**-
  *Mehmet Kerim SAİN: Main Contributer - Lead*
  
- **222******040*-
  *Gürkan Plevnelioğlu: Main Contributer*
  
- **232****042**- 
  *Muhammed Yunus Elçi: Main Contributer*

---

## Check Our Roadmap

See our plans in [ROADMAP.md](ROADMAP.md).  


---

## Researches*

| Topic      | Link                                    | Description                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Python based Decryption and Encryption codes      | [researchs/deepsearch.01.md](researchs/deepsearch.01.md) | In-depth analysis of python based decryption and encryption codes 
| Digital Signatures in Python.  | [researchs/deepsearch02.md](researchs/deepsearch02.md) | Brief overview of Digital Signatures in Python..  |
| Cryptographic Applications in Python.       | [researchs/deepsearch03.md](researchs/deepsearch03.md)    | A deatiled search about Cryptographic Applications in Python.                  |

---

## Installation 

1. **Clone Our Repository  
   ```bash
   git clone https://github.com/Ker1m954/Cryptography.git
   cd Ker1m954/Cryptography
   ```

2. **Set Up Virtual Environment(Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Caesar Cipher**
What It Is
The Caesar Cipher is a basic substitution cipher where each letter in your message (plaintext) is shifted by a fixed number of positions in the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on. It’s a simple way to obscure text.

**How It Works**
Encryption: Shifts each letter forward by the specified number (the "shift" or key).
Decryption: Shifts each letter backward by the same number.
Non-alphabetic characters (like spaces or punctuation) stay unchanged.
It only affects letters (A-Z), preserving case (uppercase/lowercase).
Why It’s Important
It’s one of the earliest encryption methods, dating back to Julius Caesar. While not secure today, it introduces the core idea of transforming plaintext into ciphertext using a key.

**How to Use It in the Code**
Start the Program:
Run the script (e.g., python crypto_toolkit.py).
Select Caesar Cipher:
From the main menu, enter 1 and press Enter.
Choose an Action:
You’ll see a sub-menu:
1. Encrypt a message
2. Decrypt a message
3. Back to main menu
Type 1 to encrypt or 2 to decrypt, then press Enter.
Enter Inputs:
Message: Type your text (e.g., "HELLO WORLD") and press Enter.
Shift: Enter an integer (e.g., 3) and press Enter.
View Output:
The program displays the result (e.g., "KHOOR ZRUOG" for encryption with shift 3).
Return:
Choose 3 to go back to the main menu.
Example
Encrypt:
Input: Message = "HELLO WORLD", Shift = 3
Output: "KHOOR ZRUOG"
Decrypt:
Input: Message = "KHOOR ZRUOG", Shift = 3
Output: "HELLO WORLD"


2. **Vigenère Cipher**
What It Is
The Vigenère Cipher is a more advanced substitution cipher that uses a keyword to shift each letter in the message. Unlike the Caesar Cipher’s single shift, it applies different shifts based on the keyword, making it harder to crack.

**How It Works**
The keyword is repeated to match the message’s length (e.g., "KEY" for "HELLO WORLD" becomes "KEYKEYKEYK").
Each letter in the message is shifted by the value of the corresponding keyword letter ('A' = 0, 'B' = 1, ..., 'Z' = 25).
Encryption: Add the shift to each letter.
Decryption: Subtract the shift from each letter.
Like the Caesar Cipher, it preserves non-alphabetic characters and case.
Why It’s Important
It’s a step up from the Caesar Cipher, showing how multiple shifts (polyalphabetic substitution) improve security. It was considered unbreakable for centuries until frequency analysis cracked it.

How to Use It in the Code
Select Vigenère Cipher:
From the main menu, enter 2 and press Enter.
Choose an Action:
Sub-menu options:
1. Encrypt a message
2. Decrypt a message
3. Back to main menu
Type 1 or 2 and press Enter.
Enter Inputs:
Message: Type your text (e.g., "HELLO WORLD").
Keyword: Enter a word with at least one letter (e.g., "KEY").
View Output:
The program shows the result (e.g., "RIJVS UYVJN" for encryption).
Return:
Choose 3 to go back.
Example
Encrypt:
Input: Message = "HELLO WORLD", Keyword = "KEY"
Output: "RIJVS UYVJN"
Decrypt:
Input: Message = "RIJVS UYVJN", Keyword = "KEY"
Output: "HELLO WORLD"


**3. AES Encryption**
What It Is
AES (Advanced Encryption Standard) is a modern symmetric encryption algorithm that uses the same key for both encryption and decryption. It’s fast, secure, and widely used in applications like VPNs and disk encryption.

**How It Works**
Encryption:
The program generates a random 16-byte key and an initialization vector (IV).
It pads the message to a multiple of 16 bytes, then encrypts it using AES in CBC (Cipher Block Chaining) mode.
Outputs are in hexadecimal format.
Decryption:
You provide the ciphertext, key, and IV (all in hex) to reverse the process.
Why It’s Important
AES is a cornerstone of modern cryptography, trusted by governments and industries for protecting sensitive data.

How to Use It in the Code
Select AES Encryption:
From the main menu, enter 3 and press Enter.
Choose an Action:
Sub-menu options:
1. Encrypt a message
2. Decrypt a message
3. Back to main menu
Type 1 or 2 and press Enter.
For Encryption:
Enter your message (e.g., "Secret Message").
The program outputs:
Ciphertext (hex)
Key (hex)
IV (hex)
Save these values for decryption.
For Decryption:
Enter the ciphertext, key, and IV (in hex) when prompted.
The program displays the original message.
Return:
Choose 3 to go back.
Example
Encrypt:
Input: "Secret Message"
Output:
Ciphertext: (e.g., "e2a1...")
Key: (e.g., "1f2b...")
IV: (e.g., "9c3d...")
Decrypt:
Input: Ciphertext, Key, IV (from above)
Output: "Secret Message"


**5. SHA-256 Hashing**
What It Is
SHA-256 is a cryptographic hash function that takes any input and produces a fixed 256-bit (64-character) hash. It’s one-way—you can’t reverse it to find the original data.

How It Works
The program uses Python’s hashlib to compute the hash.
The input message is converted to bytes, hashed, and displayed as a hexadecimal string.
Why It’s Important
Hashing ensures data integrity (e.g., verifying downloads) and is key to password storage and blockchain technology.

How to Use It in the Code
Select SHA-256 Hashing:
From the main menu, enter 4 and press Enter.
Enter Input:
Type your message (e.g., "Hello World").
View Output:
The program shows the hash (e.g., "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e").
Return:
You’re automatically returned to the main menu.
Example
Input: "Hello World"
Output: "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"


**5. RSA Digital Signatures**
What It Is
RSA (Rivest-Shamir-Adleman) is an asymmetric algorithm using a private key to sign messages and a public key to verify them. Digital signatures prove a message’s authenticity and integrity.

**How It Works**
Key Generation: Creates a private-public key pair.
Signing: Hashes the message with SHA-256, then signs it with the private key.
Verification: Uses the public key to check the signature against the message.
Why It’s Important
Digital signatures are vital for secure communications, software updates, and legal agreements.

How to Use It in the Code
Select RSA Digital Signatures:
From the main menu, enter 5 and press Enter.
Choose an Action:
Sub-menu options:
1. Generate RSA key pair
2. Sign a message
3. Verify a signature
4. Back to main menu
Generate Keys:
Select 1 to create a key pair (displayed in hex).
Save these for signing/verification.
Sign:
Select 2, enter your message (e.g., "Sign me!").
Output: Signature (hex).
Verify:
Select 3, enter the message and signature (hex).
Output: "Signature is valid!" or "Signature is invalid".
Return:
Choose 4 to go back.
Example
Generate Keys: Private and public keys (hex).
Sign:
Input: "Sign me!"
Output: Signature (hex)
Verify:
Input: "Sign me!", Signature
Output: "Signature is valid!"

---

## Contribution

We welcome anyone who is willing to help!:  
1. Please first fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  


---

## License*

Licensed under the [MIT License](LICENSE.md).  

---

## Our Acknowledgements

Special thanks to:  
- Awesome Template!: Thanks to our amazing teacher Keyvan for giving us this amazing template! Keyvan Arasteh (https://github.com/keyvanarasteh)

---

## You Can Contact Us Via;

Project Maintainer: [Mehmet Kerim SAİN] - [mehmetkerimsain@gmail.com]  
Found any bug or missing lines? Please open an issue.  

---
