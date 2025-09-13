# Global variable to store the detected operating system
# Will be set to 'win' for Windows or 'linux' for Linux during initialization
OS = None

# Global variable to store the primary network interface name (Windows only)
# Example: 'Ethernet', 'Wi-Fi', etc. Used for applying DNS settings via netsh
INTERFACE = None