import argparse
import os
import secrets
import sys


def main():
    args = _build_parser()
    if args.key:
        return decrypt(args.cipherfile, args.plainfile, int(args.key))
    return encrypt(args.cipherfile, args.plainfile)


def encrypt(cipher_file_path, plain_file_path):
    with open(plain_file_path, 'r', encoding='utf8') as plaintext_file:
        plaintext = plaintext_file.read()

    key = key_generator(plaintext)
    plaintext_int = [ord(x) for x in plaintext]
    ciphertext_xor = [bit1 ^ bit2 for bit1, bit2 in zip(plaintext_int, key[0])]
    ciphertext = ''.join(chr(byte) for byte in ciphertext_xor)

    with open(cipher_file_path, 'w', encoding='utf-8') as ciphertextfile:
        ciphertextfile.write(ciphertext)
    print(f"Ciphertext: {ciphertext} | Written to file: {cipher_file_path} | Key: {key[1]}")


def decrypt(cipher_file_path, plain_file_path, key_int):
    with open(cipher_file_path, 'r', encoding='utf-8') as file:
        ciphertext = file.read()

    key = key_int.to_bytes(1024, byteorder=sys.byteorder)
    ciphertext_int = [ord(x) for x in ciphertext]
    plaintext_xor = [bit1 ^ bit2 for bit1, bit2 in zip(ciphertext_int, key)]
    plaintext = ''.join(chr(byte) for byte in plaintext_xor)

    with open(plain_file_path, 'w', encoding='utf-8') as file:
        file.write(plaintext)
    print(f"Plaintext: {plaintext} | Written to: {plain_file_path}")


def key_generator(plaintext):
    key_bytes = secrets.token_bytes(len(plaintext))
    key_integ = int.from_bytes(key_bytes, sys.byteorder)
    return key_bytes, key_integ


def _build_parser():
    """ Build Parser to accept user-defined argument """
    parser = argparse.ArgumentParser(description="One Time Pad")
    required_args = parser.add_argument_group('Required Arguments')
    required_args.add_argument('-c', '--cipherfile', required=True, type=_check_file, help="Please enter the relative "
                                                                                           "or absolute path of the "
                                                                                           "ciphertext file that will "
                                                                                           "be written to")
    required_args.add_argument('-p', '--plainfile', required=True, type=_check_file, help="Please enter the relative or"
                                                                                          " absolute path of the "
                                                                                          "plaintext file that will be"
                                                                                          " written to")
    parser.add_argument('-k', '--key', required=False, default=False, help="Optional. Specify the Key. Only required"
                                                                           "if you are decrypting a file")
    args = parser.parse_args()
    print(f"Parameters Inputted: Plaintext = {args.plainfile} | Ciphertext = {args.cipherfile} | Key = {args.key}")
    return args


def _check_file(file):
    if not os.path.isfile(file):
        raise argparse.ArgumentTypeError(f"File path of {file} cannot be found, or is not a file. "
                                         f"Please check the file path")
    try:
        with open(file, 'r', encoding='utf8') as test_file:
            test_file.read()
            return file
    except IOError:
        raise argparse.ArgumentTypeError(f"{file} was found, but the file is not readable. Check permissions")
    except UnicodeDecodeError:
        raise argparse.ArgumentTypeError(f"{file} was found but some characters could not be decoded with UTF8. Check"
                                         f"file type/extension.")


if __name__ == '__main__':
    main()
