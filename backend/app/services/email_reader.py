
from pathlib import Path
from email.parser import Parser
from email.policy import default


# Locate backend/data/emails
EMAIL_DIR = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "emails"
)


def read_email(file_path: Path) -> dict:
    """
    Read an email text file and extract its headers and body.
    """

    raw_email = file_path.read_text(encoding="utf-8-sig")

    message = Parser(policy=default).parsestr(raw_email)

    return {
        "email_id": file_path.stem,
        "sender": message.get("From", ""),
        "subject": message.get("Subject", ""),
        "body": message.get_payload().strip(),
    }


def load_emails() -> list[dict]:
    """
    Load all .txt email files from the emails directory.
    """

    email_files = sorted(EMAIL_DIR.glob("*.txt"))

    return [
        read_email(file_path)
        for file_path in email_files
    ]
