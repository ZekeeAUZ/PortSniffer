import socket

def scan_port(target, port):
   
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            return True   # ONLY when port is open


    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    print("=== Simple Port Scanner ===\n")

    target = input("Enter target IP or hostname: ")

    print(f"\nScanning {target} (ports 1–1024)...\n")

    open_port_count = 0
    for port in range(1, 1025):
        scan_port(target, port)
        open_port_count += 1 

    print("\nScan complete.")


if __name__ == "__main__":
    main()
