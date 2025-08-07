#!/usr/bin/env python3


# region swithc_config_export
# sript start

# checks to see if ssh is installed
import shutil
if shutil.which("ssh"):
    print("SSH is installed...continuing...")
else:
    raise Exception("SSH is not installed...ending script...")


# tries to ping the device before trying to ssh into it.
import subprocess
import platform

ip = "10.23.1.1"

# Determine ping parameters based on OS
param = "-n" if platform.system().lower() == "windows" else "-c"

# Build ping command
ping_cmd = ["ping", param, "1", ip]

# Run ping command
result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check return code: 0 means success
if result.returncode == 0:
    print(f"Ping to {ip} successful...proceeding with SSH...")
else:
    raise Exception("Ping to {ip} failed, ending script...")



# Checks if paramiko is installed, else installs it based on OS.

import sys
import subprocess
import importlib.util
import platform

def is_paramiko_installed():
    return importlib.util.find_spec("paramiko") is not None

def install_paramiko():
    # Determine correct pip command
    os_name = platform.system().lower()

    if os_name == "windows":
        pip_cmd = [sys.executable, "-m", "pip", "install", "paramiko"]
    elif os_name in ["linux", "darwin"]:  # darwin = macOS
        pip_cmd = [sys.executable, "-m", "pip", "install", "paramiko"]
    else:
        raise Exception(f"Unsupported OS: {os_name}")

    print(f"Installing paramiko using: {' '.join(pip_cmd)}")
    subprocess.check_call(pip_cmd)

def main():
    print(f"Running on: {platform.system()}")

    if is_paramiko_installed():
        print("paramiko is already installed.")
    else:
        print("paramiko is not installed. Installing now...")
        try:
            install_paramiko()
            print("paramiko installed successfully.")
        except Exception as e:
            print(f"Failed to install paramiko: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()




# tries to export the config to a file locally.
import paramiko
import time
from datetime import datetime
import os
import re  # for cleaning ANSI escape sequences


# make sure to plug in the vars.
switch_name = "My-Device-Name-Here"
ip = "X.X.X.X"
user = "username"
password = "passwd"

# Set this to where you want to save the config
save_path = os.path.expanduser(r"C:\Ninja-Transfer")

# Create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Ensure the directory exists
os.makedirs(save_path, exist_ok=True)

# Build the filename with switch name and timestamp
filename = f"{switch_name}_{timestamp}_config.txt"
filepath = os.path.join(save_path, filename)

# Start SSH session
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=user, password=password)

# Open interactive shell
shell = client.invoke_shell()
time.sleep(2)

# Clear initial banner
if shell.recv_ready():
    shell.recv(65535)

# Disable paging, note must add a space before the cmd or the first letter gets cut off.
shell.send(" no page\n")
time.sleep(1)
if shell.recv_ready():
    shell.recv(65535)

# Send command to show config, note must add a space before the cmd or the first letter gets cut off.
shell.send(" show running-config\n")
time.sleep(3)

# Receive all data
output = ""
while shell.recv_ready():
    output += shell.recv(65535).decode()
    time.sleep(1)

# Clean up ANSI escape sequences
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
clean_output = ansi_escape.sub('', output)

# Write to file
with open(filepath, "w") as f:
    f.write(clean_output)

print(f"Configuration from '{switch_name}' saved to:\n{filepath}")

client.close()


# script end
# endregion
