**Authors:** Paula Meneses y Santiago Tavera

# Text encryption and decryption system
This program is a text encryption and decryption system, which uses the AES algorithm to encrypt and decrypt a text.

### Preconditions
1. First of all, make sure you have Python installed on your computer.
2. Make sure you have the pycryptodome library installed. If you don't have it, you can install it by running the following command in the terminal:

```pip install pycryptodome```

3. Make sure ypu have Crypto installed. If you don't have it, you can install it by running the following command in the terminal:

```pip install Crypto```

- You can check if everything is installed correctly by running this command:

```pip list```

## How to use:
First you should clone the repository to your computer.

**To run the program outside the development environment:**
1. Navigate to the folder where the repository was cloned

```src/Console/Console.py```


2. Run the main file:

```python src/Console/Console.py```

## How does the program work:
For now the program only works by the console.
When you run the program, you will see a menu with the following options:
```
1. Encrypt text
2. Decrypt text
3. Exit
```
The program will ask you to enter the number of the option you want to select.
4. If you select option 1, the program will ask you to enter the text you want to _encrypt_.
5. If you select option 2, the program will ask you to enter the text you want to _decrypt_.

- If you select option 1 or 2, the program will ask you to enter the key you want to use to encrypt or decrypt the text.
- The key **must** be 16 characters long.


- After entering the text and the key, the program will show you the encrypted or decrypted text.

6. If you select option 3, the program will end.


## Take into account:
- The project includes a set of unit tests that are used to verify compliance with requirements. 
To run the tests, you must install the Unittest dependency.
You can install it by running the following command in the terminal:

```pip install unittest```
