# PENETRATION-TESTING-TOOLKIT

**COMPANY**: CODTECH IT SOLUTIONS PVT. LTD  
**NAME**: DEVANG AVINASH KENI  
**INTERN ID**: CT08FRA  
**DOMAIN**: Cyber Security & Ethical Hacking  
**BATCH DURATION**: December 25th, 2024 to January 25th, 2025  
**MENTOR NAME**: NEELA SANTOSH  

---

## DESCRIPTION

The Penetration Testing Toolkit is an all-in-one solution for ethical hackers and cybersecurity enthusiasts, aimed at identifying potential vulnerabilities in both simulated and real-world environments. Designed with simplicity and efficiency in mind, this toolkit is ideal for professionals and learners stepping into the domain of cybersecurity and ethical hacking. It equips users with the necessary tools to simulate attacks, analyze systems, and strengthen defenses against cyber threats. This toolkit emphasizes ethical practices and provides a controlled environment to test and refine penetration testing skills.

One of the primary goals of this toolkit is to offer a comprehensive yet beginner-friendly approach to penetration testing. By automating various processes, the toolkit ensures that even users with limited technical expertise can navigate its features and achieve meaningful results. It encompasses essential functionalities such as brute force attack simulations, port scanning, and easy-to-use batch file automation. These features are essential for ethical hackers to understand system vulnerabilities and enhance security measures.

The toolkit’s **Brute Force Module** allows users to simulate real-world attacks on login systems by testing a set of potential passwords against a target login page. This helps identify weak passwords and assess the overall robustness of authentication mechanisms. Additionally, the **Port Scanning Module** scans target systems to identify open ports and the services running on them. These insights are critical in evaluating potential entry points that attackers might exploit.

To streamline usability, the toolkit includes custom Windows batch files, eliminating the need to manually enter commands. With just a double-click, users can launch the server and toolkit interface, making it accessible even to those unfamiliar with command-line tools. This ease of use significantly reduces setup time and encourages broader adoption of penetration testing practices.

In summary, the Penetration Testing Toolkit is not just a tool but a learning platform. It enables users to simulate attacks in a safe, ethical manner and gain hands-on experience in identifying vulnerabilities. By focusing on usability, functionality, and ethical practices, this toolkit serves as a stepping stone toward a secure digital future.

---

### Features of the Toolkit:
1. **Brute Force Module**  
   Simulates brute force attacks on login forms using a list of potential passwords. The module logs successful and failed attempts, helping users analyze the security strength of login systems.

2. **Port Scanning**  
   Scans open ports on a target system to identify active services. This module provides insights into potential vulnerabilities that attackers might exploit.

3. **Batch File for Ease of Use**  
   Includes custom batch files for launching the toolkit and server with a simple double-click, streamlining the setup and operation process.

---

### Setup Instructions:

#### 1. Prerequisites
Before running the toolkit, ensure the following requirements are met:
- **Python 3.8+** installed on your system.
- **Required Libraries**: Install them using the following command:
  ```bash
  pip install flask requests
  ```

#### 2. Starting the Toolkit
- **Step 1**: Launch the Flask server using the provided `server.bat` file. This sets up a local test login page (http://127.0.0.1:5000/login) for brute force simulations.
- **Step 2**: Start the toolkit by running the `tool.bat` file. This automatically opens the toolkit interface, eliminating the need for manual commands.

#### 3. How to Test:
- **Brute Force Module**: Input the target login URL (http://127.0.0.1:5000/login) and specify the test credentials. The tool will simulate multiple login attempts and display the results.
- **Port Scanning Module**: Specify the target IP or URL (e.g., `scanme.nmap.org`). The tool will scan for open ports and provide a detailed report.

---

### Precautions:
- **Start the Server First**: Always launch the Flask server (`server.bat`) before using the toolkit. Ensure the test credentials match those in the server file (default: username `testuser`, password `securepassword123`).
- **Test Responsibly**: Use only authorized or test targets (e.g., `http://127.0.0.1:5000/login` and `scanme.nmap.org`). Unauthorized testing is strictly prohibited.
- **Simulated Environment**: Perform tests in a controlled environment to avoid legal or ethical violations.
- **Batch File Convenience**: Utilize the batch files to simplify the process. Double-click to run, no terminal commands needed.

---

## OUTPUT

#### On Opening the Tool...
![output1](https://github.com/user-attachments/assets/8880d8d1-607a-422c-97fc-c3e8bbddf969)

#### 1. **Port Scanner**
![output2](https://github.com/user-attachments/assets/18b69d6e-4d04-4c36-bd66-5b76bc9473d6)

#### 2. **Brute Forcer**
![output3](https://github.com/user-attachments/assets/c61455b7-8ec7-4de8-84ae-64667bd98f3d)
