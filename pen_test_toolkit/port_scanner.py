import socket
import threading

# Function to scan a single port on a target
def scan_port(target, port, open_ports):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 1 second for connection attempts
        s.settimeout(1)

        # Try connecting to the target and port
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)  # Add the open port to the list
        s.close()
    except socket.error as e:
        # If there's an error, we simply pass since we're scanning multiple ports
        pass

# Function to scan a range of ports on a target
def scan_ports(target, start_port, end_port):
    print(f"Starting scan on {target} for ports {start_port}-{end_port}")
    threads = []
    open_ports = []  # List to store open ports

    # Create a thread for each port in the specified range
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Check if any open ports were found and display the appropriate message
    if open_ports:
        for port in open_ports:
            print(f"Port {port} is OPEN on {target}")
    else:
        print("No open ports found.")

    print(f"Port scan completed on {target}.")
