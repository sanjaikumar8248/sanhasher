#!/usr/bin/env python3
"""

Menu:
1. Password Hash Generator
2. File Hash Generator
3. Password Hash Checker/Decrypter
0. Exit


"""
import hashlib
import base64
import os
import sys
import time
import zipfile

HASH_ALGOS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
    "sha3_224": hashlib.sha3_224,
    "sha3_256": hashlib.sha3_256,
    "sha3_384": hashlib.sha3_384,
    "sha3_512": hashlib.sha3_512,
    "blake2b": hashlib.blake2b,
    "blake2s": hashlib.blake2s,
}

def banner():
    print("\n==============================")
    print("             SanHasher                    ")
    print("==============================")

def pause():
    print("\nPress 0 to return to main menu | Ctrl+C to exit")

def password_hash_generator():
    while True:
        banner()
        print("[ Password Hash Generator ]\n")
        text = input("Enter password/text: ")
        print("\n--- Cryptographic Hashes ---")
        for name, func in HASH_ALGOS.items():
            print(f"{name.upper():10}: {func(text.encode()).hexdigest()}")
        print("\n--- Encoding (Not a Hash) ---")
        print("BASE64     :", base64.b64encode(text.encode()).decode())
        pause()
        if input(">> ") == "0": return

def file_hash_generator():
    while True:
        banner()
        print("[ File Hash Generator ]\n")
        path = input("Enter file path: ").strip()
        if not os.path.isfile(path):
            print("File not found.")
            pause()
            if input(">> ") == "0": return
            continue
        print("\nComputing file hashes...")
        for name, func in HASH_ALGOS.items():
            h = func()
            with open(path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    h.update(chunk)
            print(f"{name.upper():10}: {h.hexdigest()}" )
        pause()
        if input(">> ") == "0": return

def password_hash_checker():
    while True:
        banner()
        print("[ Password Hash Checker/Decrypter ]\n")
        print("Supported hash types:\n" + ", ".join(HASH_ALGOS.keys()))
        hval = input("Enter hash: ").strip().lower()
        htype = input("Hash type: ").strip().lower()
        wpath = input("Wordlist file: ").strip()

        if htype not in HASH_ALGOS:
            print("Unsupported hash type.")
            pause()
            if input(">> ") == "0": return
            continue

        found = False
        try:
            with open(wpath, 'r', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if HASH_ALGOS[htype](word.encode()).hexdigest() == hval:
                        print("\nPASSWORD FOUND!")
                        print("Password:", word)
                        print("Strength: WEAK (dictionary-based)")
                        found = True
                        break
        except FileNotFoundError:
            print("Wordlist not found.")
            pause()
            if input(">> ") == "0": return
            continue

        if not found:
            print("\nPassword NOT found in dictionary")
            print("Strength: STRONG (dictionary-resistant)")

        pause()
        if input(">> ") == "0": return

def main():
    while True:
        try:
            banner()
            print("1. Password Hash Generator")
            print("2. File Hash Generator")
            print("3. Password Hash Decrypter")
            print("0. Exit")
            print("------------------------------")
            ch = input("Enter your choice: ").strip()
            if ch == '1':
                password_hash_generator()
            elif ch == '2':
                file_hash_generator()
            elif ch == '3':
                password_hash_checker()
            elif ch == '0':
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid option")
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nCtrl+C detected. Exiting safely.")
            sys.exit()

if __name__ == '__main__':
    main()
