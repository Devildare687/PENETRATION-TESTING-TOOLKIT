# PENETRATION-TESTING-TOOLKIT

**COMPANY**: CODTECH IT SOLUTIONS PVT. LTD  
**NAME**: DEVANG AVINASH KENI  
**INTERN ID**: CT08FRA  
**DOMAIN**: Cyber Security & Ethical Hacking  
**BATCH DURATION**: December 25th, 2024 to January 25th, 2025  
**MENTOR NAME**: NEELA SANTOSH  

---

## DESCRIPTION

This Penetration Testing Toolkit is designed to assist ethical hackers and cybersecurity professionals in identifying vulnerabilities in a simulated or real-world environment. It’s more than just a tool; it’s a stepping stone into the world of secure system analysis and penetration testing.

### Features of the Toolkit:
1. **Brute Force Module**  
   The brute force module enables you to test login forms with a set of potential passwords to simulate real-world penetration tests. It can test for both successful and failed login attempts.

2. **Port Scanning**  
   A port scanning tool is included to check for open ports, revealing services running on a target machine. This can help identify potential entry points.

3. **Batch File for Ease of Use**  
   To make life easier, I’ve added a custom Windows batch file. Instead of typing commands manually, you can just double-click the batch file to launch the toolkit as an app.

---

### Setup Instructions:

#### 1. Prerequisites
Before running the toolkit, make sure you have the following installed:
- **Python 3.8+**
- **Required Libraries**:  
  Install them using the command below:
  ```bash
  pip install flask requests time random

#### 2. Starting the Toolkit
-First, run the Flask server. Use the provided batch file server.bat to start the server. This ensures that the backend runs smoothly without needing to type in the terminal.
This will host a local test login page (http://127.0.0.1:5000/login) for brute force simulations.
-Next, launch the toolkit using the tool.bat file. It’s designed to start the tool directly, no manual commands required!

#### 3. How to Test:
-Input the target login URL (http://127.0.0.1:5000/login) and provide credentials for brute force testing. The tool will simulate login attempts and display results.
-Test port scanning by specifying the IP or URL of the target system. (When prompted for the target URL/IP, use the publicly available test target: scanme.nmap.org. The tool will scan open ports and display the results.)
________________________________________
### Precautions:
-**Run the server first**: Always start the Flask server (server.bat) before using the toolkit. 
Make sure you use inputs for username and password used in flask server file (in this case username is testuser and password is securepassword123, this can be changed later in flask sever file code to ensure it’s working)
Test responsibly: Use the provided test targets (http://127.0.0.1:5000/login for brute force and scanme.nmap.org for port scanning). Never target unauthorized systems.
-Simulated Environment: Ensure you test this tool in a controlled or authorized environment. Unauthorized use is strictly prohibited.
-Batch File Convenience: I’ve created batch files to make the entire process seamless—just double-click, and you’re good to go!

________________________________________
## OUTPUT
[Include links to screenshots of your toolkit in action.]
