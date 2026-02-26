#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import random

# Color codes for Termux
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
    "\033[91m",  # Red again
    "\033[92m",  # Green again
]
reset = "\033[0m"
bold = "\033[1m"

def clear():
    os.system("clear")

def typing(text, delay=0.03):
    """Typing animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def center_text(text):
    """Center text on screen"""
    terminal_width = 60
    padding = (terminal_width - len(text)) // 2
    return " " * padding + text

def hacker_loading(duration=2):
    """Professional loading animation"""
    symbols = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(duration * 10):
        for symbol in symbols:
            sys.stdout.write(f"\r{colors[1]}{bold}[ {symbol} ] Hacking in progress...{reset}")
            sys.stdout.flush()
            time.sleep(0.05)

# Professional Hacker Logo
hacker_logo = f"""
{colors[2]}{bold}
    ╔══════════════════════════════════════════════╗
    ║  ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗ ██████╗  ║
    ║  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔════╝  ║
    ║  ███████║███████║██║     █████╔╝ █████╗  ██║       ║
    ║  ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║       ║
    ║  ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗╚██████╗  ║
    ║  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ║
    ╚══════════════════════════════════════════════╝
{reset}"""

# Skull ASCII Art
skull_art = f"""
{colors[1]}{bold}
    ╔══════════════════════════════╗
    ║      ░░░░░░░░░░░░░░░░░░░     ║
    ║     ░░░▄▀▀▀▄░░░░▄▀▀▀▄░░░     ║
    ║     ░░▐░▄▄░▌░░░░▐░▄▄░▌░░     ║
    ║     ░░▐▀▀▀▀▀▄▄▄▄▀▀▀▀▀▌░░     ║
    ║     ░░█▀▄▄▄█░▀░█▄▄▄█░▀▄░░     ║
    ║     ░░░░░░░░░░░░░░░░░░░░░     ║
    ╚══════════════════════════════╝
{reset}"""

# Cool Matrix Rain Effect
def matrix_rain():
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    for _ in range(25):
        line = ""
        for _ in range(70):
            line += random.choice(chars)
        color = random.choice(colors[:2])  # Green shades only
        print(color + line + reset)
        time.sleep(0.03)

# Glitch Effect
def glitch_effect(text, repeat=3):
    for _ in range(repeat):
        clear()
        for _ in range(5):
            glitched = ""
            for char in text:
                if random.random() < 0.3:
                    glitched += random.choice("@#$%&*")
                else:
                    glitched += char
            print(random.choice(colors) + glitched + reset)
            time.sleep(0.1)
        time.sleep(0.2)

# Floating Name Animation
def floating_name(name, duration=5):
    positions = list(range(0, 40, 2)) + list(range(38, 0, -2))
    start_time = time.time()
    while time.time() - start_time < duration:
        for pos in positions:
            clear()
            print("\n" * 5)
            print(" " * pos + colors[3] + bold + "╔══════════════════════════╗")
            print(" " * pos + colors[3] + bold + f"║     {colors[5]}{name}{colors[3]}     ║")
            print(" " * pos + colors[3] + bold + "╚══════════════════════════╝")
            
            # Status bar
            print(f"\n\n{colors[2]}[+] System Status: {colors[1]}ACTIVE{reset}")
            print(f"{colors[2]}[+] User: {colors[5]}{name}{reset}")
            print(f"{colors[2]}[+] Connection: {colors[1]}SECURE 🔒{reset}")
            time.sleep(0.03)

# Name Typing Animation
def name_typing(name):
    clear()
    print("\n" * 3)
    typing(colors[4] + bold + "╔══════════════════════════════════════╗", 0.02)
    
    for i in range(len(name) + 1):
        sys.stdout.write(f"\r{colors[4]}{bold}║           {colors[5]}{name[:i]}{colors[4]}{'█' if i < len(name) else ''}            ║")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print(f"\n{colors[4]}{bold}╚══════════════════════════════════════╝{reset}")
    time.sleep(1)

# Main Animation Sequence
def main():
    try:
        name = "NAFIZ SHEIKH"
        
        # Opening Sequence
        clear()
        print(colors[1] + bold + center_text("INITIALIZING HACKER TERMINAL...") + reset)
        time.sleep(1)
        
        # Matrix Rain
        clear()
        print(colors[1] + bold + ">> ENTERING THE MATRIX <<" + reset)
        time.sleep(1)
        matrix_rain()
        
        # Show Hacker Logo
        clear()
        print(hacker_logo)
        time.sleep(2)
        
        # Glitch Effect with Name
        glitch_effect(name, 2)
        
        # Name Typing Animation
        name_typing(name)
        
        # Floating Name Animation
        floating_name(name, 4)
        
        # Show Skull with Animation
        clear()
        for color in colors:
            print(color + skull_art + reset)
            time.sleep(0.2)
        
        # Loading Animation
        clear()
        hacker_loading(3)
        print("\n")
        
        # Professional Info Display
        clear()
        print(colors[2] + bold + "╔══════════════════════════════════════╗")
        print(colors[2] + bold + f"║     {colors[5]}🔥 HACKER PROFILE 🔥{colors[2]}       ║")
        print(colors[2] + bold + "╠══════════════════════════════════════╣")
        print(colors[2] + bold + f"║  {colors[3]}► Name:{colors[5]} {name:<25}{colors[2]}  ║")
        print(colors[2] + bold + f"║  {colors[3]}► Status:{colors[1]} ETHICAL HACKER{colors[2]}     ║")
        print(colors[2] + bold + f"║  {colors[3]}► Level:{colors[4]} LEGENDARY{colors[2]}            ║")
        print(colors[2] + bold + f"║  {colors[3]}► Country:{colors[6]} BANGLADESH{colors[2]}         ║")
        print(colors[2] + bold + "╚══════════════════════════════════════╝" + reset)
        time.sleep(3)
        
        # Hacking Animation
        clear()
        print(colors[5] + bold + center_text(">> HACKING SEQUENCE INITIATED <<") + reset)
        time.sleep(1)
        
        # Progress Bars
        tasks = ["Bypassing Firewall", "Cracking Password", "Accessing Database", "Downloading Data", "Covering Tracks"]
        for task in tasks:
            sys.stdout.write(f"\r{colors[1]}[•] {task}: ")
            for i in range(0, 101, 10):
                bar = "█" * (i // 2) + "░" * (50 - (i // 2))
                sys.stdout.write(f"\r{colors[1]}[•] {task}: {colors[2]}[{bar}] {i}%")
                sys.stdout.flush()
                time.sleep(0.05)
            print(f" {colors[3]}✓ DONE")
            time.sleep(0.3)
        
        # Final Show
        clear()
        print("\n" * 3)
        typing(colors[4] + bold + center_text("🔥 HACKING BY NAFIZ SHEIKH 🔥"), 0.03)
        time.sleep(1)
        
        print("\n" + colors[2] + bold + center_text("⚡ SYSTEM HACKED SUCCESSFULLY! ⚡") + reset)
        time.sleep(1)
        
        # Animated Name Loop (This will keep running)
        print("\n" + colors[6] + center_text("Press CTRL+C to exit") + reset)
        
        # Infinite animation loop with your name
        animation_chars = ["◢", "◣", "◤", "◥"]
        i = 0
        while True:
            i = (i + 1) % 4
            sys.stdout.write(f"\r{colors[random.randint(0,6)]}{bold}>> {name} || HACKER MODE ACTIVE {animation_chars[i]} <<{reset}")
            sys.stdout.flush()
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        clear()
        print(colors[5] + bold + "\n╔══════════════════════════════════════╗")
        print(colors[5] + bold + "║     THANK YOU FOR WATCHING!         ║")
        print(colors[5] + bold + f"║     {colors[3]}{name}{colors[5]}                    ║")
        print(colors[5] + bold + "║     🔴 HACKING SHOW ENDED 🔴         ║")
        print(colors[5] + bold + "╚══════════════════════════════════════╝" + reset)
        print("\n" + colors[2] + "Subscribe: Hacking By Nafiz Sheikh" + reset)
        sys.exit(0)

if __name__ == "__main__":
    main()