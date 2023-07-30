from cryptography.fernet import Fernet


class Encryption:
    def __init__(self):
        self.key = None

    def new_key(self):
        self.key = Fernet.generate_key()
        return self.key

    def save_key(self):
        with open('file_key.key', 'wb') as file_key:
            file_key.write(self.key)

    def encrypt(self, file, key=None):
        if key is None:
            key = self.key
        encrypted = Fernet(key)
        return encrypted.encrypt(file)

    @staticmethod
    def decrypt(key, file):
        decrypted = Fernet(key)
        return decrypted.decrypt(file)


if __name__ == '__main__':

    with open('nba.csv', 'rb') as test_file:
        original = test_file.read()

    Test_Enc = Encryption()

