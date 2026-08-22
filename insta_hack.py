import requests
from colorama import Fore, Style

def login(username, password):
    print(f"{Fore.GREEN}[+] Trying to login as {username}...{Style.RESET_ALL}")
    
    # Instagram API endpoint (Example)
    url = "https://www.instagram.com/accounts/login/ajax/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"{Fore.CYAN}[-] Status Code: {response.status_code}{Style.RESET_ALL}")
        
        # Agar login successful ho (example logic)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] Success! Credentials Valid.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Failed. Check credentials.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    user = input("Enter Username: ")
    passw = input("Enter Password: ")
    login(user, passw)
