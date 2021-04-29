# Made by Misspoken
# Don't remove credits or you'll have legal issues.
# Join my Discord server :)

import urllib.request, colorama, os, ctypes
from colorama import Fore

print(f'''{Fore.BLUE}

{Fore.RESET}
{Fore.BLUE}Made by Misspoken#1122.
{Fore.BLUE}╔═════════════════{Fore.RESET}Options{Fore.BLUE}═════════════════╗
{Fore.BLUE}║                                         {Fore.BLUE}║
{Fore.BLUE}║     {Fore.BLUE}[{Fore.RESET}HTTP{Fore.BLUE}]{Fore.RESET} - Scrapes HTTP Proxies        {Fore.BLUE}║
{Fore.BLUE}║     {Fore.BLUE}[{Fore.RESET}Socks4{Fore.BLUE}]{Fore.RESET} - Scrapes Socks4 Proxies    {Fore.BLUE}║
{Fore.BLUE}║     {Fore.BLUE}[{Fore.RESET}Socks5{Fore.BLUE}]{Fore.RESET} - Scrapes Socks5 Proxies    {Fore.BLUE}║
{Fore.BLUE}║                                         {Fore.BLUE}║
{Fore.BLUE}╚═════════════════════════════════════════╝
{Fore.RESET}''')

def scrape(type):
    print(f'{Fore.BLUE}> {Fore.RESET}Selected: {type}')
    urllib.request.urlretrieve(f'https://api.proxyscrape.com/?request=getproxies&proxytype={type.lower()}&timeout=10000&country=all&ssl=all&anonymity=all', f'{type}-proxies.txt')
    print(f'{Fore.GREEN}> {Fore.RESET}Successfully scraped {type} proxies! The file should be called {type}-proxies.txt!')
    input()
    exit()

choice = input(f'{Fore.BLUE}> {Fore.RESET}Which type do you want to scrape?: ')
if(choice == "HTTP".lower() or choice == "Socks4".lower() or choice == "Socks5".lower()):
    scrape(choice)
else:
    print(f'{Fore.RED}> {Fore.RESET}It seems like that proxy type doesn\'t exist.')
