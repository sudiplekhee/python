import pyfiglet
import nmap

scanner = nmap.PortScanner()
  
name = pyfiglet.figlet_format("S U D I P")
print(name)

print("Welcome to the basic nmap scanner ")
ip = input("Enter the target ip: ")
port_range = input("Enter port range (e.g. 20-80): ")

print(f"Scanning the target {ip} from {port_range}....")

scanner.scan(ip,port_range)

for port in scanner[ip]['tcp']:
    state = scanner[ip]['tcp'][port]['state']
    print(f"Port {port} is {state}")