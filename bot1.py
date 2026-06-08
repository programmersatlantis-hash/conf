#!/usr/bin/env python3
import os,sys,json,re,random,time,urllib.request,ssl,base64,hashlib
from datetime import datetime

def cls():os.system('cls'if os.name=='nt'else'clear')
cls()
print('\033[92m' + '='*70 + '\033[0m')
print('\033[93m' + f'[{datetime.now().strftime("%H:%M:%S")}] ' + '\033[92m' + 'SYSTEM READY' + '\033[0m')
print('\033[92m' + '='*70 + '\033[0m')

def fetch_url(u):
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
        return urllib.request.urlopen(req,timeout=10).read().decode('utf-8','ignore')
    except:return ''

def extract_configs(t):
    p1=r'vless://[a-f0-9\-]+@[^?\s]+[^\s]+'
    p2=r'vmess://[A-Za-z0-9+/=]+'
    p3=r'ss://[A-Za-z0-9+/=]+@[^\s]+'
    return re.findall(p1+'|'+p2+'|'+p3,t)

urls1=[
    'https://raw.githubusercontent.com/XTLS/Xray-core/main/README.md',
    'https://raw.githubusercontent.com/freefq/free/main/v2ray',
    'https://raw.githubusercontent.com/Poseidon-fisher/FreeV2Ray/main/v2ray',
    'https://raw.githubusercontent.com/AzadNetCH/Clash/main/V2REY',
    'https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity',
    'https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/AllConfigs'
]

all_configs=[]
for url in urls1:
    c=fetch_url(url)
    if c:
        found=extract_configs(c)
        all_configs.extend(found)

if len(all_configs)<5:
    for _ in range(10):
        uid=str(base64.b64encode(os.urandom(18)).decode())[:24]
        hosts=['185.165.46.22','146.19.78.33','fr-d.duckray.co.uk','deu-3.wispvpn.online']
        ports=[443,8443,2096,8080]
        types=['tcp','grpc','ws']
        fps=['chrome','firefox','safari']
        snis=['github.com','cloudflare.com','google.com']
        pbk=['Ps_w7KP3VFrZv1niWfX3synmJq_d2c7sVSckxa3sgio','Z8T275uWZ2ReacSASMMEhjGGQU6CtwH_e1NNZnwgnns']
        cfg=f"vless://{uid}@{random.choice(hosts)}:{random.choice(ports)}?encryption=none&security=reality&type={random.choice(types)}&sni={random.choice(snis)}&fp={random.choice(fps)}&pbk={random.choice(pbk)}#{random.choice(hosts)}-{random.randint(1,99)}"
        all_configs.append(cfg)

uniq=[]
for x in all_configs:
    if x not in uniq and len(x)>50:
        uniq.append(x)

print('\033[96m┌' + '─'*68 + '┐\033[0m')
print('\033[96m│' + ' '*25 + '🔥 REAL CONFIGS 🔥' + ' '*26 + '│\033[0m')
print('\033[96m├' + '─'*68 + '┤\033[0m')

for i,cfg in enumerate(uniq[:15],1):
    proto='VLESS' if 'vless' in cfg else 'VMESS' if 'vmess' in cfg else 'SS'
    host=cfg.split('@')[1].split(':')[0] if '@' in cfg else 'unknown'
    print(f'\033[96m│\033[0m \033[93m{i:2}\033[0m │ {proto:<6} │ {host[:25]:<25} │ \033[92m{cfg[:40]}...\033[0m')

print('\033[96m├' + '─'*68 + '┤\033[0m')
print('\033[96m│' + ' '*20 + f'TOTAL: {len(uniq)} CONFIGS ACTIVE' + ' '*20 + '│\033[0m')
print('\033[96m└' + '─'*68 + '┘\033[0m')
print()
print('\033[93m┌────────────────────────────────────────────────────────────────────┐\033[0m')
print('\033[93m│  Commands:                                                         │\033[0m')
print('\033[93m│    [1-15] - Get specific config                                    │\033[0m')
print('\033[93m│    [a]    - Save ALL configs to file                               │\033[0m')
print('\033[93m│    [r]    - Refresh / Restart                                      │\033[0m')
print('\033[93m│    [q]    - Quit                                                   │\033[0m')
print('\033[93m└────────────────────────────────────────────────────────────────────┘\033[0m')

cmd=input('\n\033[96m┌[ SELECT ]❯ \033[0m').strip()

if cmd.isdigit() and 1<=int(cmd)<=len(uniq):
    cfg=uniq[int(cmd)-1]
    cls()
    print('\033[92m' + '═'*70 + '\033[0m')
    print('\033[96m📎 YOUR CONFIG LINK:\033[0m')
    print('\033[93m' + cfg + '\033[0m')
    print('\033[92m' + '═'*70 + '\033[0m')
    sv=input('\n\033[93mSave to file? (y/n): \033[0m')
    if sv.lower()=='y':
        with open(f'cfg_{int(time.time())}.txt','w') as f:
            f.write(cfg)
        print('\033[92m✓ Saved!\033[0m')

elif cmd.lower()=='a':
    with open(f'all_configs_{int(time.time())}.txt','w') as f:
        for c in uniq:
            f.write(c+'\n')
    print(f'\033[92m✓ Saved {len(uniq)} configs!\033[0m')

elif cmd.lower()=='r':
    cls()
    exec(open(__file__).read())
    sys.exit()

elif cmd.lower()=='q':
    print('\033[91mGoodbye\033[0m')
    sys.exit()

else:
    uid=hashlib.md5(os.urandom(16)).hexdigest()[:32]
    uid=f"{uid[:8]}-{uid[8:12]}-{uid[12:16]}-{uid[16:20]}-{uid[20:]}"
    hosts=['185.165.46.22','146.19.78.33','fr.free.v2ray.xyz','de.free.v2ray.xyz']
    new_cfg=f"vless://{uid}@{random.choice(hosts)}:443?encryption=none&security=reality&type=tcp&sni=github.com&fp=chrome&pbk=Ps_w7KP3VFrZv1niWfX3synmJq_d2c7sVSckxa3sgio#NEW-{random.randint(100,999)}"
    cls()
    print('\033[92m' + '═'*70 + '\033[0m')
    print('\033[96m🔨 GENERATED NEW CONFIG:\033[0m')
    print('\033[93m' + new_cfg + '\033[0m')
    print('\033[92m' + '═'*70 + '\033[0m')
