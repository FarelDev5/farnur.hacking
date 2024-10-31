import os
import requests
import subprocess
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from datetime import datetime
import pyfiglet
import re
import socket

console = Console()

# Author Information
def author_info():
    print(Panel(
        "[bold green]Author: Farel Alfareza[/bold green]\n"
        "[bold cyan]Instagram/TikTok: @farel.project_5[/bold cyan]",
        title="[bold magenta]About[/bold magenta]", expand=False
    ))

# Function to display FARNUR logo with gradient effect
def show_logo():
    logo_text = pyfiglet.figlet_format("FARNUR", font="standard")
    gradient_logo = ""
    colors = ["#8A2BE2", "#9370DB", "#BA55D3", "#DA70D6", "#FF69B4"]

    # Apply colors per line
    for line in logo_text.splitlines():
        color = colors[0]
        colors = colors[1:] + [colors[0]]  # Rotate colors
        gradient_logo += f"[{color}]{line}[/]\n"

    console.print(Panel(gradient_logo, title="[bold magenta]FARNUR[/bold magenta]", expand=False))

# Function to display device information with a modern table
def device_info():
    device_name = os.popen("getprop ro.product.model").read().strip() or "Unknown Device"
    os_version = os.popen("getprop ro.build.version.release").read().strip() or "Unknown OS"
    termux_version = os.popen("pkg list-installed | grep termux").read().strip() or "Unknown Termux Version"

    # Creating a modern table layout
    table = Table(title="Device Information", title_style="bold magenta")
    table.add_column("Property", style="bold cyan")
    table.add_column("Details", style="bold yellow")

    # Adding rows with device information
    table.add_row("Device Model", device_name)
    table.add_row("OS Version", os_version)
    table.add_row("Termux Version", termux_version)

    console.print(table)

# Function to ping a website
def ping_website():
    website = input("$farnur/input/website: ")
    
    try:
        result = subprocess.run(["ping", "-c", "4", website], capture_output=True, text=True, check=True)
        print(Panel(
            f"[bold cyan]Ping Output:[/bold cyan]\n{result.stdout}",
            title="[bold magenta]Ping Website[/bold magenta]", expand=False
        ))
    except subprocess.CalledProcessError as e:
        print(f"[bold red]Error pinging website: {e.stderr}[/bold red]")

# Function to open location in Google Maps
def open_in_maps(lat, lon):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    os.system(f"termux-open-url '{maps_url}'")
    print(f"[bold green]Opening location in Google Maps: {maps_url}[/bold green]")

# Function to track IP and open location in Google Maps
def track_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(Panel(
                f"[bold cyan]IP: {ip}[/bold cyan]\n"
                f"[bold green]Location: {data['city']}, {data['regionName']}, {data['country']}[/bold green]\n"
                f"[bold yellow]ISP: {data['isp']}[/bold yellow]\n"
                f"[bold red]Latitude: {data['lat']} | Longitude: {data['lon']}[/bold red]",
                title="[bold magenta]IP Tracker[/bold magenta]", expand=False
            ))
            open_in_maps(data['lat'], data['lon'])
            geoip_lookup(ip)
        else:
            print("[bold red]IP tracking failed. Please check the IP address.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error: {e}[/bold red]")

# New Feature: GeoIP Lookup
def geoip_lookup(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(Panel(
            f"[bold cyan]IP: {data.get('ip', 'N/A')}[/bold cyan]\n"
            f"[bold green]City: {data.get('city', 'N/A')}[/bold green]\n"
            f"[bold green]Region: {data.get('region', 'N/A')}[/bold green]\n"
            f"[bold green]Country: {data.get('country', 'N/A')}[/bold green]\n"
            f"[bold yellow]Organization: {data.get('org', 'N/A')}[/bold yellow]\n"
            f"[bold red]Location: {data.get('loc', 'N/A')}[/bold red]",
            title="[bold magenta]GeoIP Information[/bold magenta]", expand=False
        ))
    except Exception as e:
        print(f"[bold red]Error retrieving GeoIP data: {e}[/bold red]")

# New Feature: Port Scanner
def port_scanner(ip):
    print(f"[bold green]Scanning open ports on {ip}...[/bold green]")
    open_ports = []
    try:
        for port in range(1, 1025):  # Scanning first 1024 ports
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            sock.close()
        
        if open_ports:
            print(Panel(
                f"[bold cyan]Open Ports:[/bold cyan] {', '.join(map(str, open_ports))}",
                title="[bold magenta]Port Scanner[/bold magenta]", expand=False
            ))
        else:
            print("[bold red]No open ports found.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error: {e}[/bold red]")

# Function to display current date and time
def date_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(Panel(
        f"[bold cyan]Current Date and Time: {current_time}[/bold cyan]",
        title="[bold magenta]Date & Time[/bold magenta]", expand=False
    ))

# Function to run shell commands with loop
def run_command():
    os.system('clear')
    show_logo()
    author_info()
    device_info()
    while True:
        print(Panel(
            "[bold magenta]Command Menu[/bold magenta]\n"
            "1. Enter a shell command to execute\n"
            "Type 'clear' to clear the screen\n"
            "Type 'exit' to return to the main menu",
            title="[bold green]RUN COMMAND[/bold green]", expand=False
        ))

        command = input("$farnur/input/command: ")
        
        if command.strip().lower() == 'clear':
            os.system('clear')
            show_logo()
            author_info()
            device_info()
            continue
        
        if command.strip().lower() == 'exit':
            os.system('clear')
            show_logo()
            author_info()
            device_info()
            return  # Return to the main menu
        
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(Panel(
                f"[bold cyan]Command Output:[/bold cyan]\n{result.stdout}",
                title="[bold magenta]Command Execution Result[/bold magenta]", expand=False
            ))
        except subprocess.CalledProcessError as e:
            print(f"[bold red]Error executing command: {e.stderr}[/bold red]")

# Function to validate IP address
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

# Function to convert text to ASCII codes
def text_to_ascii():
    text = input("$farnur/input/text: ")
    ascii_codes = [(char, ord(char)) for char in text]
    
    result = "\n".join([f"[bold yellow]'{char}': {code}[/bold yellow]" for char, code in ascii_codes])
    
    print(Panel(
        f"[bold cyan]ASCII Codes and Interpretations:[/bold cyan]\n{result}",
        title="[bold magenta]ASCII Conversion[/bold magenta]", expand=False
    ))

# Main function to display menu
def main_menu():
    while True:
        print(Panel(
            "[bold magenta]Choose a Feature:[/bold magenta]\n"
            "1. IP Tracking\n"
            "2. Date & Time\n"
            "3. Run Command\n"
            "4. GeoIP Lookup\n"
            "5. Port Scanner\n"
            "6. ASCII Converter\n"
            "7. Ping Website\n"
            "8. Exit",
            title="[bold green]FARNUR MENU[/bold green]", expand=False
        ))

        choice = input("$farnur/input: ")
        
        if choice == '1':
            ip = input("$farnur/input/ip: ")
            if is_valid_ip(ip):
                track_ip(ip)
            else:
                print("[bold red]Invalid IP address format.[/bold red]")
        elif choice == '2':
            date_time()
        elif choice == '3':
            run_command()
        elif choice == '4':
            ip = input("$farnur/input/geoip/ip: ")
            if is_valid_ip(ip):
                geoip_lookup(ip)
            else:
                print("[bold red]Invalid IP address format.[/bold red]")
        elif choice == '5':
            ip = input("$farnur/input/port/ip: ")
            if is_valid_ip(ip):
                port_scanner(ip)
            else:
                print("[bold red]Invalid IP address format.[/bold red]")
        elif choice == '6':
            text_to_ascii()
        elif choice == '7':
            ping_website()
        elif choice == '8':
            print("[bold red]Exiting program...[/bold red]")
            break
        else:
            print("[bold red]Invalid choice. Please try again.[/bold red]")

if __name__ == "__main__":
    os.system('clear')
    show_logo()
    author_info()
    device_info()
    main_menu()
