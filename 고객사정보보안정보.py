from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='encryption_key.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='encryption_key.key'):
    return open(filename, 'rb').read()

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

# 암호화 키 생성 및 저장
encryption_key = generate_key()
save_key(encryption_key)

# 사용자의 개인정보
user_data = "고객사의 중요한 정보"

# 데이터 암호화
encrypted_data = encrypt_data(user_data, encryption_key)

# 암호화된 데이터 출력
print("암호화된 데이터:", encrypted_data)

# 데이터 복호화
decrypted_data = decrypt_data(encrypted_data, encryption_key)

# 복호화된 데이터 출력
print("복호화된 데이터:", decrypted_data)
