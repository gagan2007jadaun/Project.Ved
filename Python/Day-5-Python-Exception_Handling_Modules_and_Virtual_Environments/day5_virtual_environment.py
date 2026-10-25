# VIRTUAL ENVIRONMENT
'''
Bhai, ye concept real-world Python development mein bahut important hai. Project VED mein jaise-jaise hum AI libraries install karenge, humein dependencies ko properly manage karna padega.

1. Virtual environment kya hai?
Virtual environment ek project-specific Python environment hota hai. Ismein project ke packages aur dependencies ko alag manage kar sakte hain.

Example: ek project ko library ka version 1 chahiye aur doosre ko version 2. Virtual environments unki dependencies ko isolate karne mein help karte hain.

2. WINDOWS SETUP

VS Code ka terminal kholo aur apne Day-5 folder mein ye commands run kar.

Step 1 — Environment create karo
python -m venv .venv


Step 2 — Activate karo

PowerShell terminal mein:
.\.venv\Scripts\Activate.ps1


Agar Command Prompt (CMD) use kar rahe ho:
.venv\Scripts\activate.bat


Activation ke baad terminal prompt mein (.venv) dikh sakta hai.

Step 3 — Pip update karo
python -m pip install --upgrade pip


Step 4 — Ek package install karo
python -m pip install requests


Step 5 — Installed packages dekho
python -m pip list


requests install karne ke liye internet access chahiye.

3. Dependencies save karna
Project mein installed packages ki list save karne ke liye:
python -m pip freeze > requirements.txt


Baad mein kisi compatible environment mein dependencies install kar sakte ho:
python -m pip install -r requirements.txt


Yaad rakh: .venv folder ko GitHub par upload mat karna. Use .gitignore mein add kar.
.venv/
__pycache__/
'''