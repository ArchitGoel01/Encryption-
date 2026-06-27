# 🔐 Random Substitution Cipher - Python

A simple Python project that demonstrates **encryption** and **decryption** using a **Random Substitution Cipher**. The program generates a random substitution key to encrypt user input and uses the same key to decrypt it back to the original message.

---

## 📖 About the Project

This project is designed to help beginners understand the fundamentals of encryption by implementing a basic substitution cipher in Python. It uses Python's built-in `random` and `string` modules to create a randomized character mapping for secure message transformation.

---

## ✨ Features

- 🔒 Encrypt plain text messages
- 🔓 Decrypt encrypted messages
- 🎲 Randomly generates a unique substitution key
- 🔤 Supports:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters
  - Spaces
- 🐍 Beginner-friendly Python code

---

## 🛠️ Technologies Used

- Python 3
- random
- string

---

## 📂 Project Structure

```
│── encryption.py
│── README.md
```

---

## ⚙️ How It Works

1. Creates a list of supported characters.
2. Copies the list to create a secret key.
3. Randomly shuffles the key.
4. Encrypts each character using the shuffled key.
5. Decrypts the encrypted message by reversing the mapping.

---

## ▶️ Example Output

```text
Enter a message to encrypt:
archit goel

Entered text : archit goel
Encrypted text : it>6N-Pzm=X

Enter a message to decrypt:
it>6N-Pzm=X

Entered text : it>6N-Pzm=X
Decrypted text : archit goel
```

---

### Run the Program

```bash
python encryption.py
```
### ⭐ If you found this project helpful, please consider giving it a Star on GitHub!
