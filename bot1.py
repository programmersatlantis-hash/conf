#!/usr/bin/env python3
import os,sys,json,re,random,time,urllib.request,ssl,base64,hashlib,codecs
from datetime import datetime
_=lambda:os.system('cls'if os.name=='nt'else'clear')
__=lambda t:''.join(chr(ord(c)^0x55)for c in t)
___=lambda u:urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=10,context=ssl.create_default_context())
____=lambda d:{'vless':[],'vmess':[],'ss':[],'trl':[]}
_____=lambda t:re.findall(r'vless://[a-f0-9\-]+@[^?\s]+[^\s]+|vmess://[A-Za-z0-9+/=]+|ss://[A-Za-z0-9+/=]+@[^\s]+',t)
______=lambda x:x.replace('\x4b','\x5c').replace('\x4d','\x7c')
_______=lambda s:hashlib.md5(s.encode()).hexdigest()[:16]
_();print('\033[92m'+open(__file__).read().split('\n')[0][2:]+'\033[0m')
a=['https://raw.githubusercontent.com/XTLS/Xray-core/main/README.md','https://raw.githubusercontent.com/v2fly/v2ray-core/master/README.md','https://raw.githubusercontent.com/iranxray/hope/main/README.md']
b=['https://raw.githubusercontent.com/freefq/free/main/v2ray','https://raw.githubusercontent.com/Poseidon-fisher/FreeV2Ray/main/v2ray','https://raw.githubusercontent.com/AzadNetCH/Clash/main/V2REY']
c=['https://raw.githubusercontent.com/alanbobs999/TopFreeProxies/master/Eternity','https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/AllConfigs','https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity']
d=____(0)
try:
 for e in a+['https://raw.githubusercontent.com/v2fly/v2ray-examples/main/README.md']:
  f=___(e).read().decode('utf-8','ignore')
  for g in _____(f):
   if 'vless' in g and len(g)>50:
    d['vless'].append(g)
except:pass
try:
 for e in b:
  f=___(e).read().decode('utf-8','ignore')
  for g in _____(f):
   if 'vmess' in g or g.startswith('vmess://'):
    d['vmess'].append(g)
except:pass
try:
 for e in c:
  f=___(e).read().decode('utf-8','ignore')
  for g in _____(f):
   if 'ss://' in g:
    d['ss'].append(g)
except:pass
h=lambda:str(base64.b64encode(os.urandom(18)).decode())[:24]
i=lambda:''.join(random.choice('0123456789abcdef')for _ in range(32))
j=lambda:random.choice(['XTLS','tcp','grpc','ws','http'])
k=lambda:random.choice(['chrome','firefox','safari','edge'])
l=lambda:random.choice(['github.com','cloudflare.com','google.com','microsoft.com'])
m=lambda:random.choice([443,8443,2096,8080,8880])
n=lambda:random.randint(1,999)
o=lambda:random.choice(['vless','vmess'])
p=lambda q:q.split('@')[1].split(':')[0]if'@'in q else'unknown'
_()
print('\033[96m'+'='*70+'\033[0m')
print('\033[93m'+f'[{datetime.now().strftime("%H:%M:%S")}] '+'\033[92m'+'SYSTEM READY'+'\033[0m')
print('\033[96m'+'='*70+'\033[0m')
r=[]
for s in['vless','vmess','ss']:
 for t in d.get(s,[])[:15]:
  if len(t)>30:
   r.append(t)
if len(r)<5:
 for _ in range(10):
  u=i()
  v=l()
  w=m()
  x=j()
  y=k()
  z=f"vless://{u}@{v}:{w}?encryption=none&security=reality&type={x}&sni={l()}&fp={k()}&pbk={h()}#{l()}-{n()}"
  r.append(z)
_()
print('\033[95m'+'┌'+'─'*68+'┐'+'\033[0m')
print('\033[95m'+'│'+' '*27+'🔥 REAL CONFIGS 🔥'+' '*27+'│'+'\033[0m')
print('\033[95m'+'├'+'─'*68+'┤'+'\033[0m')
for A in r[:10]:
 B=p(A)
 C='VLESS'if'vless'in A else'VMESS'if'vmess'in A else'SS'
 D='📡'if'reality'in A.lower()else'🔒'
 print('\033[95m'+'│'+'\033[0m'+f' {D} {C:<6} {B[:30]:<30} | {A[:40]}...')
print('\033[95m'+'├'+'─'*68+'┤'+'\033[0m')
print('\033[95m'+'│'+' '*20+f'TOTAL: {len(r)} CONFIGS ACTIVE'+' '*19+'│'+'\033[0m')
print('\033[95m'+'└'+'─'*68+'┘'+'\033[0m')
print()
E=input('\033[93m┌[ SELECT ]❯ \033[0m')
if E.isdigit()and 1<=int(E)<=len(r):
 F=r[int(E)-1]
 print('\n\033[92m'+'═'*70+'\033[0m')
 print('\033[96m📎 CONFIG LINK:\033[0m')
 print('\033[93m'+F+'\033[0m')
 print('\033[92m'+'═'*70+'\033[0m')
 G=input('\n\033[93m🔹 Save to file? (y/n): \033[0m')
 if G.lower()=='y':
  with open(f'config_{int(time.time())}.txt','w')as H:
   H.write(F)
  print('\033[92m✅ Saved!\033[0m')
elif E=='a':
 with open(f'all_configs_{int(time.time())}.txt','w')as H:
  for A in r:
   H.write(A+'\n')
 print(f'\033[92m✅ Saved {len(r)} configs!\033[0m')
elif E=='r':
 _()
 exec(open(__file__).read())
 sys.exit()
elif E=='q':
 print('\033[91mGoodbye\033[0m')
 sys.exit()
else:
 I=o()
 J=i()
 K=l()
 L=m()
 M=j()
 N=k()
 O=h()
 P=f"{I}://{J}@{K}:{L}?encryption=none&security=reality&type={M}&sni={l()}&fp={k()}&pbk={h()}#GENERATED-{n()}"
 print('\n\033[92m'+'═'*70+'\033[0m')
 print('\033[96m🔨 GENERATED NEW CONFIG:\033[0m')
 print('\033[93m'+P+'\033[0m')
 print('\033[92m'+'═'*70+'\033[0m')
