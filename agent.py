# agent.py

import sys
import time
import os
from datetime import datetime
from tools import send_whatsapp_message, ToolError


def wait_until(target_hour: int, target_minute: int) -> None:
    while True:
        now = datetime.now()
        if (now.hour, now.minute) >= (target_hour, target_minute):
            return
        time.sleep(30)


def read_message_from_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Message file not found: {file_path}")

    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue          # skip empty lines
            if stripped.startswith("#"):
                continue          # skip comments
            lines.append(stripped)

    if not lines:
        raise ValueError("Message file has no sendable content")

    return " ".join(lines)   # single-line, reliable


def run_agent(contact_name: str, message_file: str, hour: int, minute: int) -> None:
    print(f"[AGENT] Reading message from file: {message_file}")
    message = read_message_from_file(message_file)

    print(f"[AGENT] Waiting until {hour:02d}:{minute:02d}...")
    wait_until(hour, minute)

    print("[AGENT] Time reached. Sending message.")

    try:
        result = send_whatsapp_message(contact_name, message)
        print(f"[AGENT] SUCCESS: {result}")
    except ToolError as e:
        print(f"[AGENT] FAILED: {e}")
        return

    print("[AGENT] Shutting down system.")
    #os.system("shutdown /s /t 0")              use only when it is required 


if __name__ == "__main__":
    """
    Usage:
    python agent.py <contact_name> <message_file> <hour> <minute>

    Example:
    python agent.py alice message.txt 9 0
    """

    if len(sys.argv) != 5:
        print("Usage: python agent.py <contact_name> <message_file> <hour> <minute>")
        sys.exit(1)

    contact_name = sys.argv[1]
    message_file = sys.argv[2]

    try:
        hour = int(sys.argv[3])
        minute = int(sys.argv[4])
    except ValueError:
        print("Hour and minute must be integers.")
        sys.exit(1)

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        print("Invalid time.")
        sys.exit(1)

    run_agent(contact_name, message_file, hour, minute)
