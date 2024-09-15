import requests
import json
from colorama import Fore, Style
import argparse


def decode_password(encoded_password, caesar_shift=-4):
    """Decodes the password (user and superuser)"""
    decoded_password = ""
    parts = encoded_password.split("&")
    for i in range(0, len(parts) - 1):
        decoded_char = chr(int(parts[i]))
        if decoded_char.isalpha():
            start = ord("a") if decoded_char.islower() else ord("A")
            shifted_char = chr((ord(decoded_char) - start + caesar_shift) % 26 + start)
        elif decoded_char.isdigit():
            # Directly convert ASCII code to number
            shifted_char = chr(int(parts[i]) - ord("0") + ord("0"))
        else:
            shifted_char = decoded_char
        decoded_password += shifted_char
    return decoded_password


def print_baseinfo(url):
    """Fetches and prints router base information"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        if "BASEINFOSET" in data:
            baseinfo = data["BASEINFOSET"]
            print(f"{Fore.CYAN}=== Router Base Information ==={Style.RESET_ALL}")
            for key, value in baseinfo.items():
                key_display = key.replace("baseinfoSet_", "")
                if key in ("baseinfoSet_TELECOMPASSWORD", "baseinfoSet_USERPASSWORD"):
                    value = decode_password(value)
                    value_display = f"{Fore.YELLOW}{value}{Style.RESET_ALL}"
                else:
                    value_display = value
                print(
                    f"{Fore.GREEN}{key_display:<25}{Style.RESET_ALL}: {value_display}"
                )
        else:
            print("No base information found in JSON.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch and decode router base information."
    )
    parser.add_argument(
        "-u",
        "--url",
        default="http://192.168.1.1:8080/cgi-bin/baseinfoSet.cgi",
        help="URL of the router's baseinfoSet.cgi",
    )
    args = parser.parse_args()
    print_baseinfo(args.url)
