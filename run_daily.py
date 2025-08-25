import json
from fetch_fda_letters import fetch_letters
from generate_digest import generate_digest
from send_email import send_email

def run():
    with open("letters.json", "r", encoding="utf-8") as f:
        letters = json.load(f)
    today_index = (datetime.now().date() - datetime(2020, 1, 1).date()).days
    if today_index < len(letters):
        letter = letters[today_index]
        digest = generate_digest(letter["content"])
        send_email(f"FDA警告信简报 - {letter['date']}", digest)

if __name__ == "__main__":
    run()
