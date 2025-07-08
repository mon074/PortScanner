🔍 Port Scanner (Multithreaded)

A simple and educational **port scanner** written in **Python**, designed to scan a **range of ports** quickly using **multithreading**. Ideal for learning how network scanning works.


🚀 Features

- 📶 Scans a **range of ports** specified by the user
- ⚡ Uses **multithreading** to improve speed
- 🎯 Target any IP address or domain (e.g., `scanme.nmap.org`)
- 🐍 Built entirely with **Python standard libraries**


🧰 Libraries Used

| Library       | Purpose                                      |
|---------------|----------------------------------------------|
| `socket`      | To create connections and check open ports   |
| `threading`   | To run multiple scans in parallel (faster)   |



## 💻 How to Use

1. Run the script

2. Enter the following when prompted:

✅ Target IP or domain (e.g., scanme.nmap.org or 192.168.1.1)

✅ Start port (e.g., 20)

✅ End port (e.g., 100)

The program will scan ports from 20 to 100 and show which ones are open.


bash:
python port_scanner.py

⚠️ Disclaimer
This tool is for educational purposes only.
Do not scan any system you don’t own or don’t have permission to test. Unauthorized scanning can be illegal.

👩‍💻 Author
Made by Divyanka Raghuvanshi (mon074)




