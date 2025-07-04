import os

INTERFACE_NAME = "Ethernet"

dns_servers = {
    "1. Radar DNS": ["10.202.10.10", "10.202.10.11"],
    "2. Electro DNS": ["78.157.42.100", "78.157.42.101"],
    "3. Shecan DNS": ["178.22.122.100", "185.51.200.2"],
    "4. Google DNS": ["8.8.8.8", "8.8.4.4"],
    "5. Cloudflare DNS": ["1.1.1.1", "1.0.0.1"],
    "6. Quad9 DNS": ["9.9.9.9", "149.112.112.112"],
    "7. OpenDNS": ["208.67.222.222", "208.67.220.220"]
}

def set_dns(primary, secondary):
    os.system(f'netsh interface ip set dns name="{INTERFACE_NAME}" static {primary}')
    os.system(f'netsh interface ip add dns name="{INTERFACE_NAME}" {secondary} index=2')
    print(f"DNS set to: {primary}, {secondary}")

def reset_dns():
    os.system(f'netsh interface ip set dns name="{INTERFACE_NAME}" dhcp')
    print("DNS reset to automatic (DHCP).")

def show_menu():
    print("\nselect DNS:")
    for key in dns_servers:
        print(key)
    print(f"{len(dns_servers)+1}. Reset DNS to automatic")
    print("0. exit")

def main():
    while True:
        show_menu()
        choice = input("enter your choice: ").strip()

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(dns_servers):
            dns = list(dns_servers.values())[int(choice) - 1]
            set_dns(dns[0], dns[1])
        elif choice == str(len(dns_servers)+1):
            reset_dns()
        else:
            print("invalid choice please try again.")

if __name__ == "__main__":
    main()
