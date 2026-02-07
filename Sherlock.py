import requests
import os
import time

# Siber Güvenlik Renkleri
PURPLE = '\033[38;5;129m'
CYAN = '\033[38;5;51m'
GREEN = '\033[38;5;82m'
RED = '\033[38;5;196m'
WHITE = '\033[38;5;231m'
YELLOW = '\033[38;5;226m'
RESET = '\033[0m'

def banner():
    os.system('clear')
    print(f"{PURPLE}")
    print(r"  ____  _                      _            _     ")
    print(r" / ___|| |__   __ _  __| | _____      __  | |    ")
    print(r" \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /  | |    ")
    print(r"  ___) | | | | (_| | (_| | (_) \ V  V /   |_|    ")
    print(f"{WHITE} |____/|_| |_|\__,_|\__,_|\___/ \_/\_/    (_)    ")
    print(f"\n      {PURPLE}>> {WHITE}SHADOWNOVA SHERLOCK V3.0 {PURPLE}<<{RESET}")
    print(f"    {CYAN}Professional Cyber Security OSINT System{RESET}")
    print(f"       {RED}Deep Keyword Analysis Enabled (2026){RESET}\n")

def check_username():
    banner()
    user = input(f"{WHITE}Hedef Kullanıcı Adı (Target Username): {RESET}")
    print(f"\n{YELLOW}[!] {user} için dijital ayak izi taranıyor...{RESET}\n")
    
    # En güvenilir ve keyword analizi yapılmış platformlar
    targets = {
        "GitHub": [f"https://github.com/{user}", "Page not found"],
        "Reddit": [f"https://www.reddit.com/user/{user}", "nobody on Reddit goes by that name"],
        "Twitch": [f"https://www.twitch.tv/{user}", "time machine"],
        "Steam": [f"https://steamcommunity.com/id/{user}", "could not be found"],
        "Medium": [f"https://medium.com/@{user}", "404"],
        "SoundCloud": [f"https://soundcloud.com/{user}", "couldn't find that user"],
        "Patreon": [f"https://www.patreon.com/{user}", "isn't available"]
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    found_count = 0

    for name, data in targets.items():
        url = data[0]
        keyword = data[1]
        try:
            # Sitenin bizi bot sanmaması için 0.5 saniye bekleme
            time.sleep(0.5)
            response = requests.get(url, headers=headers, timeout=10)
            
            # 200 dönmesi ve sayfanın içinde "hata mesajı" olmaması lazım
            if response.status_code == 200 and keyword not in response.text:
                print(f"{GREEN}[+] {name:12}: FOUND! -> {url}{RESET}")
                found_count += 1
            else:
                print(f"{RED}[-] {name:12}: NOT FOUND{RESET}")
        except:
            print(f"{WHITE}[?] {name:12}: ERROR (Timeout/Proxy){RESET}")

    print(f"\n{CYAN}--- Tarama Bitti | Toplam {found_count} Hesap Bulundu ---{RESET}")

if __name__ == "__main__":
    check_username()
    input(f"\n{PURPLE}Çıkmak için Enter'a bas...{RESET}")

