import requests
import os

def load_wordlist(path):
    if not os.path.exists(path):
        print("[!] Wordlist bulunamadı.")
        return []

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().splitlines()

def scan_target(target_ip, wordlist):
    base_url = f"http://{target_ip}"

    print(f"\n[+] Hedef taranıyor: {base_url}\n")

    for path in wordlist:
        url = f"{base_url}/{path}"

        try:
            response = requests.get(url, timeout=3)

            if response.status_code == 200:
                print(f"[FOUND] {url}")

        except requests.RequestException:
            pass

def main():
    while True:
        print("\n--- DirBusterLite ---")
        print("Çıkmak için 'x' yazın.")

        target_ip = input("Hedef IP: ").strip()
        if target_ip.lower() == "x":
            break

        wordlist_path = input("Wordlist yolu: ").strip()
        if wordlist_path.lower() == "x":
            break

        wordlist = load_wordlist(wordlist_path)
        if not wordlist:
            continue

        scan_target(target_ip, wordlist)

if __name__ == "__main__":
    main()
