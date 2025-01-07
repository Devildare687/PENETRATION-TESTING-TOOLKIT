import socket
import threading

def scan_port(target, port, open_ports):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)


        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)  
        s.close()
    except socket.error as e:
    
        pass

def scan_ports(target, start_port, end_port):
    print(f"Starting scan on {target} for ports {start_port}-{end_port}")
    threads = []
    open_ports = [] 

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()


    if open_ports:
        for port in open_ports:
            print(f"Port {port} is OPEN on {target}")
    else:
        print("No open ports found.")

    print(f"Port scan completed on {target}.")
