import src.encryption as enc
import os


def test_encryption():
    dir_list = os.listdir('test_data/video')
    original = []
    for file in dir_list:
        with open(f'test_data/video/{file}', 'rb') as test_file:
            original.append(test_file.read())

    test_enc = enc.Encryption()
    key = test_enc.new_key()
    test_out = []
    for file in original:
        enc_file = test_enc.encrypt(file)
        dec_file = test_enc.decrypt(key, enc_file)
        if dec_file == original:
            test_out.append(True)
        else:
            test_out.append(False)

    assert [True, True, True] == test_out


if __name__ == '__main__':
    test_encryption()
