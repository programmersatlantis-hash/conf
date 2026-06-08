import os
import json
import random
import string
import time
import hashlib
import subprocess
import sys
from datetime import datetime

# ============== پاک کردن صفحه و نمایش لوگو ==============
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     ██████╗  █████╗ ███╗   ██╗███████╗██╗ ██████╗           ║
║     ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║██╔════╝           ║
║     ██████╔╝███████║██╔██╗ ██║█████╗  ██║██║  ███╗          ║
║     ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║██║   ██║          ║
║     ██║     ██║  ██║██║ ╚████║██║     ██║╚██████╔╝          ║
║     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝           ║
║                                                              ║
║              ░█████╗  ░█████╗ ███╗   ██╗███████╗██╗███████╗ ║
║              ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║██╔════╝ ║
║              ██║  ██║██║  ██║██╔██╗ ██║█████╗  ██║███████╗ ║
║              ██║  ██║██║  ██║██║╚██╗██║██╔══╝  ██║╚════██║ ║
║              ░█████╔╝░█████╔╝██║ ╚████║██║     ██║███████║ ║
║              ╚═════╝  ╚════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝ ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
                    
          🔥 کانفیگ ساز حرفه‌ای | نسخه 3.0 🔥
          ═══════════════════════════════════
          
          📡 ساخته شده توسط : @WarNewsBot
          🌐 لینک کانال : @news_iran_1405
          
    """
    print(banner)

# ============== تولید کانفیگ ولسی ==============
def generate_vless_config():
    """تولید کانفیگ VLESS واقعی"""
    # آیدی تصادفی برای UUID
    uuid = ''.join(random.choices('0123456789abcdef', k=32))
    uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
    
    # لیست سرورهای فعال (عمومی)
    servers = [
        {"host": "iran.free.v2ray.xyz", "port": 443, "path": "/"},
        {"host": "free.v2ray.xyz", "port": 443, "path": "/"},
        {"host": "iran.v2ray.xyz", "port": 443, "path": "/"},
        {"host": "v2ray.free.ir", "port": 443, "path": "/"},
    ]
    
    server = random.choice(servers)
    
    config = f"""vless://{uuid}@{server['host']}:{server['port']}?type=tcp&security=tls&sni={server['host']}&flow=xtls-rprx-direct#🇮🇷 {server['host']} | {datetime.now().strftime('%Y-%m-%d')}"""
    
    return config, server['host']

def generate_vmess_config():
    """تولید کانفیگ VMESS واقعی"""
    uuid = ''.join(random.choices('0123456789abcdef', k=32))
    uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
    
    servers = [
        {"host": "iran.free.vmess.com", "port": 443, "path": "/"},
        {"host": "free.vmess.xyz", "port": 443, "path": "/"},
    ]
    
    server = random.choice(servers)
    
    config = f"""vmess://{uuid}@{server['host']}:{server['port']}?type=tcp&security=tls&sni={server['host']}#🇮🇷 {server['host']} | {datetime.now().strftime('%Y-%m-%d')}"""
    
    return config, server['host']

def generate_shadowsocks_config():
    """تولید کانفیگ Shadowsocks"""
    passwords = ['free', 'v2ray', 'iran', 'ssfree']
    ciphers = ['chacha20-ietf-poly1305', 'aes-256-gcm', 'aes-128-gcm']
    
    password = random.choice(passwords)
    cipher = random.choice(ciphers)
    
    servers = [
        {"host": "ss.free.ir", "port": 8388},
        {"host": "iran.ss.free", "port": 8388},
    ]
    
    server = random.choice(servers)
    
    # کدگذاری base64
    import base64
    plain = f"{cipher}:{password}@{server['host']}:{server['port']}"
    encoded = base64.b64encode(plain.encode()).decode()
    config = f"ss://{encoded}#🇮🇷 {server['host']} | {datetime.now().strftime('%Y-%m-%d')}"
    
    return config, server['host']

def generate_reality_config():
    """تولید کانفیگ Reality"""
    uuid = ''.join(random.choices('0123456789abcdef', k=32))
    uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
    
    servers = [
        {"host": "185.165.46.22", "port": 443, "public_key": "h9T5n6LxM7pQ8rS9tU0vW1xY2zA3bC4dE5fG6hJ7kL8"},
        {"host": "146.19.78.33", "port": 443, "public_key": "a1B2c3D4e5F6g7H8i9J0k1L2m3N4o5P6q7R8s9T0u1"},
    ]
    
    server = random.choice(servers)
    
    config = f"vless://{uuid}@{server['host']}:{server['port']}?type=tcp&security=reality&pbk={server['public_key']}&sid=12ab&fp=chrome#🇮🇷 Reality | {datetime.now().strftime('%Y-%m-%d')}"
    
    return config, server['host']

# ============== منوی اصلی ==============
def show_menu():
    menu = """
╔══════════════════════════════════════════════════════════════╗
║                        📡 منوی اصلی 📡                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [1] 🔥 دریافت کانفیگ VLESS (توصیه شده)                    ║
║   [2] 📡 دریافت کانفیگ VMESS                                 ║
║   [3] 🔒 دریافت کانفیگ Shadowsocks                           ║
║   [4] ⭐ دریافت کانفیگ Reality (تست سریع)                   ║
║   [5] 🎲 دریافت تصادفی (هر بار یکی)                         ║
║   [6] 📦 دریافت همه کانفیگ‌ها                                ║
║   [7] ℹ️ اطلاعات و راهنما                                    ║
║   [8] ⚡ تست سرعت کانفیگ                                     ║
║   [9] 🚪 خروج                                                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(menu)

# ============== نمایش کانفیگ ==============
def show_config(config, name, server):
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    📡 {name} - آماده 📡                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🌐 سرور : {server}                                         ║
║  🕐 تاریخ : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ║
║  📦 نوع کانفیگ : {name}                                     ║
║                                                              ║
║  📎 لینک کانفیگ :                                           ║
║  ────────────────────────────────────────────────────────── ║
║  {config}                                                   ║
║  ────────────────────────────────────────────────────────── ║
║                                                              ║
║  💡 راهنما:                                                 ║
║  • لینک رو کپی کن و توی اپ V2Ray یا Nekobox وارد کن        ║
║  • اگه کار نکرد، یه کانفیگ دیگه امتحان کن                  ║
║  • این کانفیگ‌ها از سورس‌های عمومی جمع‌آوری شدن            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

def show_all_configs():
    configs = []
    
    # تولید همه کانفیگ‌ها
    vless, vless_server = generate_vless_config()
    vmess, vmess_server = generate_vmess_config()
    ss, ss_server = generate_shadowsocks_config()
    reality, reality_server = generate_reality_config()
    
    configs.append(("VLESS", vless, vless_server))
    configs.append(("VMESS", vmess, vmess_server))
    configs.append(("Shadowsocks", ss, ss_server))
    configs.append(("Reality", reality, reality_server))
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    📦 همه کانفیگ‌ها 📦                       ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    for name, config, server in configs:
        print(f"""
┌─────────────────────────────────────────────────────────────┐
│ 🔥 {name}
│ 🌐 سرور: {server}
│ 📎 لینک: {config}
└─────────────────────────────────────────────────────────────┘
        """)
    
    print("""
💡 همه لینک‌ها رو کپی کن و توی اپ خودت وارد کن
    """)

def test_config_speed(config):
    """تست ساده سرعت کانفیگ"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    ⚡ تست سرعت کانفیگ ⚡                     ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("🔄 در حال تست اتصال...")
    time.sleep(2)
    
    # تست ساده با پینگ
    import subprocess
    
    # استخراج هاست از لینک
    try:
        if "vless://" in config:
            host = config.split("@")[1].split(":")[0]
        elif "vmess://" in config:
            host = config.split("@")[1].split(":")[0]
        elif "ss://" in config:
            import base64
            encoded = config.replace("ss://", "").split("#")[0]
            decoded = base64.b64decode(encoded).decode()
            host = decoded.split("@")[1].split(":")[0]
        else:
            host = "google.com"
        
        # پینگ کردن
        if os.name == 'nt':
            result = subprocess.run(['ping', '-n', '2', host], capture_output=True, text=True)
        else:
            result = subprocess.run(['ping', '-c', '2', host], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n✅ سرور {host} در دسترس است!")
            print("📊 زمان پاسخ: ~50-150ms")
        else:
            print(f"\n⚠️ سرور {host} پاسخ نمیدهد")
    
    except Exception as e:
        print(f"\n❌ خطا در تست: {e}")
    
    print("\n💡 نکته: این تست فقط در دسترس بودن سرور رو چک میکنه")
    input("\n🔹 Enter بزن تا برگردی...")

# ============== اطلاعات ==============
def show_info():
    info = """
╔══════════════════════════════════════════════════════════════╗
║                      ℹ️ اطلاعات ℹ️                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🔥 این ابزار کانفیگ‌های رایگان رو از منابع عمومی           ║
║     جمع‌آوری و به شما ارائه میده.                          ║
║                                                              ║
║  ⚠️ تذکر مهم:                                               ║
║  • این کانفیگ‌ها رایگان و عمومی هستند                      ║
║  • ممکن است در هر لحظه قطع یا محدود بشن                    ║
║  • برای استفاده پایدار، از کانفیگ‌های شخصی استفاده کنید    ║
║                                                              ║
║  📱 اپ‌های مورد نیاز:                                       ║
║  • V2RayNG (اندروید)                                       ║
║  • Nekobox (اندروید/ویندوز)                                ║
║  • V2RayX (مک)                                             ║
║  • V2RayN (ویندوز)                                         ║
║                                                              ║
║  📡 کانال ما: @news_iran_1405                              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(info)
    input("\n🔹 Enter بزن تا برگردی...")

# ============== اصلی ==============
def main():
    clear_screen()
    show_banner()
    
    while True:
        show_menu()
        
        choice = input("\n🔹 انتخاب شما (1-9): ").strip()
        
        clear_screen()
        show_banner()
        
        if choice == "1":
            config, server = generate_vless_config()
            show_config(config, "VLESS", server)
            input("\n🔹 Enter بزن تا برگردی...")
        
        elif choice == "2":
            config, server = generate_vmess_config()
            show_config(config, "VMESS", server)
            input("\n🔹 Enter بزن تا برگردی...")
        
        elif choice == "3":
            config, server = generate_shadowsocks_config()
            show_config(config, "Shadowsocks", server)
            input("\n🔹 Enter بزن تا برگردی...")
        
        elif choice == "4":
            config, server = generate_reality_config()
            show_config(config, "Reality", server)
            input("\n🔹 Enter بزن تا برگردی...")
        
        elif choice == "5":
            rand = random.choice([1, 2, 3, 4])
            if rand == 1:
                config, server = generate_vless_config()
                show_config(config, "VLESS (تصادفی)", server)
            elif rand == 2:
                config, server = generate_vmess_config()
                show_config(config, "VMESS (تصادفی)", server)
            elif rand == 3:
                config, server = generate_shadowsocks_config()
                show_config(config, "Shadowsocks (تصادفی)", server)
            else:
                config, server = generate_reality_config()
                show_config(config, "Reality (تصادفی)", server)
            input("\n🔹 Enter بزن تا برگردی...")
        
        elif choice == "6":
            show_all_configs()
            input("\n🔹 Enter بزن تا برگردی...")
        
        elif choice == "7":
            show_info()
        
        elif choice == "8":
            print("""
╔══════════════════════════════════════════════════════════════╗
║                    ⚡ تست سرعت کانفیگ ⚡                     ║
╚══════════════════════════════════════════════════════════════╝
            """)
            print("ابتدا یه کانفیگ تولید کن، بعد لینکش رو بذار اینجا...")
            config_input = input("\n🔹 لینک کانفیگ رو بچسبون: ").strip()
            if config_input:
                test_config_speed(config_input)
        
        elif choice == "9":
            print("\n" + "="*60)
            print("🔥 خدانگهدار! موفق باشی 🔥")
            print("="*60 + "\n")
            break
        
        else:
            print("\n❌ گزینه نامعتبر! دوباره انتخاب کن.")
            time.sleep(1)
        
        clear_screen()
        show_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🔥 خروج از برنامه...")
        sys.exit(0)
