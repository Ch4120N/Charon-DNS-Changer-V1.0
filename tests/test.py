"""
Test script for Charon DNS Changer.
Provides utilities to:
- Map menu numbers to DNS entries
- Retrieve DNS IP addresses
- Execute system commands
- Check current system DNS servers
"""

import sys
import subprocess
import platform
import re
from datetime import datetime

# -----------------------
# DNS Configuration Data
# -----------------------

# Dictionary of predefined DNS servers
# Each entry has a primary (index1) and secondary (index2) IP address
DNS_DICTIONARY = {
    "Ch4120N DNS": {"index1": "78.157.42.100", "index2": "10.202.10.11"},
    "Charon Security Agency DNS1": {"index1": "178.22.122.100", "index2": "1.1.1.1"},
    "Charon Security Agency DNS2": {"index1": "78.157.42.101", "index2": "1.1.1.1"},
    "Shecan DNS": {"index1": "185.51.200.2", "index2": "178.22.122.100"},
    "Electro DNS": {"index1": "78.157.42.100", "index2": "78.157.42.101"},
    "403.online": {"index1": "10.202.10.202", "index2": "10.202.10.102"},
    "Google Public DNS": {"index1": "8.8.8.8", "index2": "8.8.4.4"},
    "Quad9": {"index1": "9.9.9.9", "index2": "149.112.112.112"},
    "OpenDNS Home": {"index1": "208.67.222.222", "index2": "208.67.220.220"},
    "Cloudflare DNS": {"index1": "1.1.1.1", "index2": "1.0.0.1"},
    "Comodo Secure DNS": {"index1": "8.26.56.26", "index2": "8.20.247.20"},
    "CleanBrowsing": {"index1": "185.225.168.168", "index2": "185.228.169.168"},
    "Alternate DNS": {"index1": "76.76.19.19", "index2": "76.223.122.150"},
    "AdGuard DNS": {"index1": "176.103.130.130", "index2": "176.103.130.131"},
    "Verisign": {"index1": "64.6.64.6", "index2": "64.6.65.6"},
    "OpenNIC": {"index1": "216.87.84.211", "index2": "23.90.4.6"},
    "Yandex DNS": {"index1": "77.88.8.8", "index2": "77.88.8.1"},
    "DNS.Watch": {"index1": "84.200.69.80", "index2": "84.200.70.40"},
    "Level 3": {"index1": "209.244.0.3", "index2": "209.244.0.4"},
    "Oracle Dyn": {"index1": "216.146.35.35", "index2": "216.146.36.36"},
    "UncensoredDNS": {"index1": "91.239.100.100", "index2": "89.233.43.71"},
    "Neustar Security Services": {"index1": "156.154.70.5", "index2": "156.157.71.5"},
    "GreenTeamDNS": {"index1": "81.218.119.11", "index2": "209.88.198.133"},
    "SafeDNS": {"index1": "195.46.39.39", "index2": "195.46.39.40"},
}

# Mapping of numeric menu options to DNS dictionary keys
OPTIONS = {str(i+1): name for i, name in enumerate(DNS_DICTIONARY.keys())}

# -----------------------
# DNS Utility Functions
# -----------------------

def get_dns_choice(user_input: str) -> str:
    """
    Normalize user input and return corresponding DNS dictionary key.
    E.g., "01" → "1" → "Ch4120N DNS"
    """
    normalized = str(int(user_input))  # convert to integer string
    return OPTIONS.get(normalized)


def getDNSs(name: str) -> list:
    """
    Retrieve primary and secondary DNS IP addresses for a given DNS name.
    Returns an empty list if DNS name is not found.
    """
    indexes = DNS_DICTIONARY.get(name)
    try:
        return [indexes.get('index1'), indexes.get('index2')]
    except AttributeError:
        return []


def execute(command: str) -> bool:
    """
    Execute a system command and return True if it succeeded.
    Uses subprocess.run with shell access and captures output.
    Suppresses console window on Windows.
    """
    try:
        kwargs = {
            "shell": True,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "text": True
        }

        if sys.platform.lower() == 'win32':
            kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW

        result = subprocess.run(command, **kwargs)
        return result.returncode == 0

    except Exception:
        return False


def escape_newlines_block(text: str) -> str:
    """
    Escape newline characters in a multi-line string for safe insertion
    into shell commands or files.
    """
    text = text.replace("\r\n", "\n")
    core = text.strip("\n")
    escaped = core.replace("\n", r"\n")
    return r"\n" + escaped + r"\n"


def get_current_dns() -> str:
    """
    Retrieve current DNS IPs configured on the system.
    Works on both Windows and Linux.
    Returns a comma-separated string of DNS addresses.
    """
    dns_list = []

    system = platform.system().lower()

    if system == "windows":
        try:
            netsh_output = subprocess.getoutput("netsh interface ip show dns").splitlines()
            for line in netsh_output:
                match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", line)
                if match:
                    ip = match.group(1)
                    if ip not in dns_list:
                        dns_list.append(ip)
        except Exception as e:
            print(f"Error getting DNS on Windows: {e}")

    elif system == "linux":
        try:
            with open("/etc/resolv.conf", "r") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("nameserver"):
                        parts = line.split()
                        if len(parts) >= 2 and parts[1] not in dns_list:
                            dns_list.append(parts[1])
        except Exception as e:
            print(f"Error reading /etc/resolv.conf: {e}")

    else:
        print("Unsupported OS")
        return ""

    return ", ".join(dns_list)


# -----------------------
# Example Usage
# -----------------------

if __name__ == "__main__":
    # Display current DNS servers
    dns_str = get_current_dns()
    print(f"Current DNS: {dns_str}")

    # Example of normalizing user input and retrieving DNS addresses
    # Uncomment below for interactive testing:
    # user_input = input("Please enter DNS option number [1-24]: ")
    # dns_name = get_dns_choice(user_input)
    # print(getDNSs(dns_name))
