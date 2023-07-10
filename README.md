## 😸 DM discord bot `@Bot DM#6773`
[![discord](https://img.shields.io/badge/discord-v2.2.3-blue)](https://pypi.org/project/discord/)
[![python-decouple](https://img.shields.io/badge/python_decouple-v3.8-orange)](https://pypi.org/project/python-decouple/)
### A discord bot for DM-ing users 😼

![Profile](https://raw.githubusercontent.com/DynoW/botfordms/main/DM_bot_profile.png)

### Commands:
- !msg [user] [message]<br>
> Send someone a message. example: !msg @DynoW You are the best!<br>
- !msg all [message]<br>
> (Admin only) Announce everyone on the server about something. example: !msg all Ntza<br>
- !msg block [message]<br>
> (Admin only) Block a user. example: !msg block @BotDM<br>
- !report [user] [message]<br>
> Send a report for an user. example: !report @BotDM scam<br>

### How to install:
Requirements: python3<br>
Dependencies: discord, python-decouple<br>

\> Clone repo: `git clone https://github.com/DynoW/botfordms.git`<br>

\> Change directory: `cd botfordms`

\> Intall dependencies: `pip install -r requirements.txt`<br>

\> Create a .env file (example file: .env_sample): `echo "DM_BOT_TOKEN=YOUR_TOKEN_HERE" > .env`<br>

\> (Optional) Additionally create a venv: `python3 -m venv venv` and activate: `. venv/bin/activate` (Linux) or `. venv/bin/Activate.ps1` (Windows)

\> Run! `python3 Bot.py` or `nohup python3 Bot.py >> log.txt 2>&1 &` for background use<br>

### For help contact: DynoW#9056. Enjoy! 🐱
