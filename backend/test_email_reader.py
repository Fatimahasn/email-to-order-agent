import sys
sys.stdout.reconfigure(encoding="utf-8")
from app.services.email_reader import load_emails


emails = load_emails()

print(f"Total emails loaded: {len(emails)}")

for email in emails:
    print("\n------------------------------")
    print("Email ID:", email["email_id"])
    print("Sender:", email["sender"])
    print("Subject:", email["subject"])
    print("Body:")
    print(email["body"])
