import os
import sys
import time
import msvcrt
import pyotp
from colorama import init, Fore, Style

init()

def clear():
    os.system("cls")

def get_secret():
    while True:
        clear()
        print(f"{Fore.CYAN}=== 2FA Code Generator ==={Style.RESET_ALL}\n")
        secret = input("Enter 2FA secret key: ").strip().replace(" ", "").upper()
        if not secret:
            continue
        try:
            pyotp.TOTP(secret).now()
            return secret
        except Exception:
            print(f"\n{Fore.RED}Invalid secret key. Try again.{Style.RESET_ALL}")
            time.sleep(1.5)

def display_code(secret):
    totp = pyotp.TOTP(secret)
    prev_remaining = -1

    while True:
        remaining = 30 - (int(time.time()) % 30)

        if prev_remaining != -1 and remaining > prev_remaining:
            clear()
            print(f"\n  {Fore.RED}{Style.BRIGHT}Code expired!{Style.RESET_ALL}\n")
            time.sleep(1)
            prev_remaining = -1
            continue

        code = totp.now()

        if remaining != prev_remaining:
            clear()
            print(f"{Fore.CYAN}=== 2FA Code Generator ==={Style.RESET_ALL}\n")
            print(f"  Code:  {Fore.GREEN}{Style.BRIGHT}{code}{Style.RESET_ALL}\n")

            if remaining <= 5:
                color = Fore.RED
            elif remaining <= 10:
                color = Fore.YELLOW
            else:
                color = Fore.WHITE

            bar_len = 20
            filled = int((remaining / 30) * bar_len)
            bar = "█" * filled + "░" * (bar_len - filled)
            print(f"  Time:  {color}{bar} {remaining}s{Style.RESET_ALL}\n")
            print(f"{Fore.LIGHTBLACK_EX}  [Backspace] New key{Style.RESET_ALL}")
            prev_remaining = remaining

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"\x08" or key == b"\x7f":
                return

        time.sleep(0.1)

def main():
    try:
        while True:
            secret = get_secret()
            display_code(secret)
    except KeyboardInterrupt:
        clear()
        print(f"\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
