import sys

# adding Folder_2 to the system path
sys.path.insert(0, 'C:/Users/david/Documents/GitHub/FileTransfer/FileTransfer')
import src.encryption as enc
import os


def test_encryption_folder():
    test_enc = enc.Encryption()
    key = test_enc.new_key()
    dir_list = os.listdir('test_data/video')
    original = []
    for file in dir_list:
        with open(f'test_data/video/{file}', 'rb') as test_file:
            original.append(test_file.read())

    test_out = []
    for file in original:
        enc_file = test_enc.encrypt(file)
        with open('video_enc.mkv', 'wb') as encrypted_file:
            encrypted_file.write(enc_file)
        dec_file = test_enc.decrypt(key, enc_file)
        with open('video_dec.mkv', 'wb') as decrypt_file:
            decrypt_file.write(dec_file)

    assert original[0] == dec_file


def test_encryption_file():
    with open('test_data/bled-zima-jezero-grad-cerkev.jpg', 'rb') as test_file:
        original = test_file.read()

    test_enc = enc.Encryption()
    key = test_enc.new_key()
    enc_file = test_enc.encrypt(original)
    dec_file = test_enc.decrypt(key, enc_file)

    assert dec_file == enc_file

if __name__ == '__main__':
    test_encryption_folder()
