#!/usr/bin/env python3

import os
import sys
import time


ABOUT = r"""
======================================================================
                             ABOUT NERD
======================================================================

Tool Name : NERD
Author    : Bilal
Version   : 1.0

----------------------------------------------------------------------
Why was NERD created?
----------------------------------------------------------------------

NERD was developed as a personal Python learning project that gradually
evolved into a practical cybersecurity tool. The project also serves as
a way to improve Python programming skills, understand password creation
psychology, and build a useful tool for authorized security assessments.

----------------------------------------------------------------------
What does NERD do?
----------------------------------------------------------------------

• Collects user-related information
• Generates intelligent word variations
• Creates prefixes and common abbreviations
• Generates realistic password
• Prioritizes passwords using an internal scoring system
• Removes duplicate passwords automatically
• Separates results into High, Medium and Low priority wordlists
• Saves clean wordlists for further testing

----------------------------------------------------------------------
How powerful is NERD?
----------------------------------------------------------------------

NERD is designed around one simple idea:

    "People rarely create completely random passwords."

Instead, many users combine names, birthdays, favorite numbers,
locations, pets, movies, nicknames, years, symbols and memorable
information.

By combining these patterns intelligently, NERD attempts to generate
password candidates that are more realistic than generic dictionary
wordlists.

The effectiveness of NERD depends entirely on the quality and accuracy
of the information provided.

----------------------------------------------------------------------
Disclaimer
----------------------------------------------------------------------

NERD is intended ONLY for:

 • Educational Purposes
 • Authorized Penetration Testing
 • Capture The Flag (CTF) Competitions
 • Personal Security Assessments

Unauthorized use of this software against systems you do not own or
have explicit permission to test may violate laws and regulations.

The author assumes NO responsibility for misuse, illegal activities,
or any damage caused by this software.

Use NERD responsibly and ethically.

----------------------------------------------------------------------
Acknowledgements
----------------------------------------------------------------------

Thank you for using NERD.

This project started from curiosity, learning, and countless hours of
experimentation. Every feature has been built with the goal of making
password auditing smarter, cleaner, and more practical while keeping
the code simple enough for learners to understand.

NERD is still evolving, and future versions will continue to improve
its intelligence, performance, and usability.

Happy Learning.

- Bilal

======================================================================
"""

def user_input():

    user_details = {}
    
    print(f"{"="*3}> Please Provide Information.")
    input_details = {
                        "f_name" : "First Name",
                        "l_name" : "Last Name",
                        "n_name" : "Nick Name",
                        "d_o_b" : "Date of Birth (DD-MM-YYYY)",
                        "m_num" : "Mobile Number (+0123456789)",
                        "p_name" : "Other (Child, Pet, Partner) Name",
                        "country" : "Country",
                        "city" : "City",
                        "extra" : "Extra (ID No OR Favorite Movie OR Anything Else.)"
                    }

    for key in input_details:
        while True:
            get_input = input(f"Enter {input_details[key]}: ")
            if get_input == "":
                print(f"{input_details[key]} can't be empty.")
                continue

            user_details[key] = get_input
            break
    
    return user_details


TOTAL_STEPS = 6
def progress(step):

    percent = int((step / TOTAL_STEPS) * 100)

    filled = percent // 5          # 20 blocks

    bar = "█" * filled + "░" * (20 - filled)

    print(f"\r[ {bar} ] {percent}%", end="", flush=True)

    if step == TOTAL_STEPS:
        print()


def gen_variations(user_details):
    
    details = user_details

    u_details = {}

    variant_words = {}

    prefixes = []

    for key in details:

        if key == "d_o_b":
            u_details[key] = details[key]
            continue

        if key == "m_num":
            u_details[key] = details[key]
            continue

        lower = details[key].lower().replace(" ", "")
        upper = details[key].upper().replace(" ", "")
        capital = details[key].capitalize().replace(" ", "")
        variants = [lower, upper, capital]

        if key in ["f_name", "l_name", "n_name", "p_name"]:
            variant_words[key] = variants
        else:
            u_details[key] = variants

        if key in ["f_name", "l_name", "n_name", "p_name"]:
                for i in range(1, len(lower) + 1):
                    prefixes.append(lower[:i])
        
    return u_details, variant_words, prefixes

def add_numbers(user_details):

    details = user_details

    c_numbers = [
                "123", "1234", "12345", "123456", "1234567", "12345678", "123456789",
                "321", "4321", "54321", "1122", "2520", "2552", "2580", "001",
                "999", "9999", "000", "0000", "111", "1111", "222", "2222",
                "333", "3333", "444", "4444", "555", "5555", "666", "6666",
                "777", "7777", "786", "7860", "888", "8888", "987", "9876",
                "2020", "2021", "2022", "2023", "2024", "2025", "2026",
                "1122", "1212", "1010", "007", "786786"
                ]

    for key in details:
        if key == "d_o_b":
            dob = details[key].replace("-", "")
            day = dob[:2]
            month = dob[2:4]
            year = dob[4:]
            day_month = dob[:4]
            month_year = dob[2:]

            c_numbers.extend([dob, day, month, year, day_month, month_year])

        if key == "m_num":
            mnum = details[key].replace("+", "")
            f_num = mnum[:3]
            s_num = mnum[3:6]
            l_num = mnum[6:]

            c_numbers.extend([mnum, f_num, s_num, l_num])

        if key == "extra":

            value = details[key].strip().replace(" ", "").replace("-", "")

            if value.isdigit():

                c_numbers.append(value)

                for i in range(len(value) - 2):
                    c_numbers.append(value[i:i+3])

    return c_numbers

def com_word_number(variant_words, numbers, symbols):

    result = {}

    for word_list in variant_words.values():

        for word in word_list:

            for num in numbers:

                save_password(result, word + num, 95)

                for sym in symbols:

                    save_password(result, word + sym + num, 90)

                    save_password(result, word + num + sym, 88)

                    save_password(result, num + word, 75)

                    save_password(result, num + word + sym, 65)

                    save_password(result, num + sym + word, 60)

    return result

def com_word_word(variant_words):

    result = {}

    fields = list(variant_words.keys())

    for i in fields:

        for j in fields:

            if i == j:
                continue

            for a in variant_words[i]:

                for b in variant_words[j]:

                    save_password(result, a+b, 85)

    return result

def com_word_word_number(variant_words, numbers):

    result = {}

    fields = list(variant_words.keys())

    for i in fields:

        for j in fields:

            if i == j:
                continue

            for a in variant_words[i]:

                for b in variant_words[j]:

                    for num in numbers:

                        save_password(result, a+b+num, 82)

                        save_password(result, num+a+b, 70)

    return result

def com_word_word_symbol(variant_words, numbers, symbols):

    result = {}

    fields = list(variant_words.keys())

    for i in fields:

        for j in fields:

            if i == j:
                continue

            for a in variant_words[i]:

                for b in variant_words[j]:

                    for num in numbers:

                        for sym in symbols:

                            save_password(result, a+b+num+sym, 80)

                            save_password(result, a+b+sym+num, 78)

                            save_password(result, num+a+b+sym, 72)

                            save_password(result, sym+a+b+num, 65)

    return result

def com_details(u_details, numbers, symbols):

    result = {}

    for key in ["country", "city", "extra"]:

        if key not in u_details:
            continue

        for value in u_details[key]:

            value = value.strip()

            if value.replace(" ", "").isalpha():

                words = value.split()

                # Single word
                if len(words) == 1:
                    candidates = [words[0]]

                # Multi-word
                else:
                    candidates = words
                    candidates = list(set(words + ["".join(words)]))

                for clean in candidates:

                    for num in numbers:

                        save_password(result, clean + num, 75)

                        for sym in symbols:

                            save_password(result, clean + sym + num, 68)
                            save_password(result, clean + num + sym, 68)
                            save_password(result, num + clean, 60)
                            save_password(result, num + sym + clean, 55)
                            save_password(result, num + clean + sym, 55)


    return result


def com_prefix(prefixes, numbers, symbols):

    result = {}

    for pre in prefixes:

        for num in numbers:

            save_password(result, pre+num, 65)

            for sym in symbols:

                save_password(result, pre+num+sym, 60)

                save_password(result, pre+sym+num, 60)

    return result


os.makedirs("nerd_output", exist_ok=True)


def save_password(result, password, score):

    if password not in result:

        result[password] = score

    elif score > result[password]:

        result[password] = score

def merge_passwords(main_result, new_result):

    for password, score in new_result.items():

        if password not in main_result:

            main_result[password] = score

        elif score > main_result[password]:

            main_result[password] = score


def gen_combination(u_details, variant_words, prefixes, numbers):

    passwords = {}

    progress(0)

    symbols = [
        "!", '"', "#", "$", "%", "&", "'", "(", ")", "*",
        "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
        "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"
    ]

    # Word + Number
    merge_passwords(
        passwords,
        com_word_number(variant_words, numbers, symbols)
    )
    progress(1)

    # Word + Word
    merge_passwords(
        passwords,
        com_word_word(variant_words)
    )
    progress(2)

    # Word + Word + Number
    merge_passwords(
        passwords,
        com_word_word_number(variant_words, numbers)
    )
    progress(3)

    # Word + Word + Symbol + Number
    merge_passwords(
        passwords,
        com_word_word_symbol(
            variant_words,
            numbers,
            symbols
        )
    )
    progress(4)

    # Country / City / Extra
    merge_passwords(
        passwords,
        com_details(
            u_details,
            numbers,
            symbols
        )
    )
    progress(5)

    # Prefixes
    merge_passwords(
        passwords,
        com_prefix(
            prefixes,
            numbers,
            symbols
        )
    )
    progress(6)

    return passwords

def save_passwords(passwords, f_name):

    high = []
    medium = []
    low = []
    for password, score in passwords.items():
        if score >= 90:
            high.append(password)
        elif score >= 70:
            medium.append(password)
        else:
            low.append(password)

    # High Priority
    with open(f"nerd_output/{f_name.lower()}_high.txt", "w", encoding="utf-8") as file:
        for password in sorted(high):
            file.write(password + "\n")

    # Medium Priority
    with open(f"nerd_output/{f_name.lower()}_medium.txt", "w", encoding="utf-8") as file:
        for password in sorted(medium):
            file.write(password + "\n")

    # Low Priority
    with open(f"nerd_output/{f_name.lower()}_low.txt", "w", encoding="utf-8") as file:
        for password in sorted(low):
            file.write(password + "\n")

    print("\n==================================")
    print("        Generation Report")
    print("==================================")
    print("Wordlists saved successfully.\n")
    print(f"Generated : {len(passwords):,}")
    print(f"High      : {len(high):,}")
    print(f"Medium    : {len(medium):,}")
    print(f"Low       : {len(low):,}")
    print("Output Folder : nerd_output")
    print("==================================")


def banner():

    os.system("clear")
    os.system("cls")

    logo = [
        " ███╗   ██╗ ███████╗ ██████╗  ██████╗",
        " ████╗  ██║ ██╔════╝ ██╔══██╗ ██╔══██╗",
        " ██╔██╗ ██║ █████╗   ██████╔╝ ██║  ██║",
        " ██║╚██╗██║ ██╔══╝   ██╔══██╗ ██║  ██║",
        " ██║ ╚████║ ███████╗ ██║  ██║ ██████╔╝",
        " ╚═╝  ╚═══╝ ╚══════╝ ╚═╝  ╚═╝ ╚═════╝"
    ]

    for line in logo:
        print(line)
        time.sleep(0.4)

    print("=" * 40)
    print(" Version : 1.0")
    print(" Author  : Bilal")
    print("=" * 40)

    time.sleep(0.5)


def menu():

    while True:
        print("\n[1] Generate Password List")
        print("[2] About")
        print("[3] Exit")

        choice = input("\nSelect > ").strip()

        if choice == "1":
            return

        elif choice == "2":
            print(ABOUT)

        elif choice == "3":
            print("\nThanks for using NERD.")
            exit()

        else:
            print("Invalid option.")


def main():

    banner()

    menu()
    
    details = user_input()

    u_details, variant_words, prefixes = gen_variations(details)

    numbers = add_numbers(details)

    passwords = gen_combination(
        u_details,
        variant_words,
        prefixes,
        numbers
    )

    save_passwords(
        passwords,
        details["f_name"]
    )


main()
