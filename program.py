import pyautogui
import time
import pyperclip
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def is_last_message_from_sender(chat: str, sender_name="Tejesh Reddy") -> bool:
    lines = chat.strip().splitlines()
    for line in reversed(lines):
        if "]" in line and ":" in line:
            try:
                name_part = line.split("]")[1].strip()
                sender = name_part.split(":")[0].strip()
                return sender.lower() != sender_name.lower()
            except IndexError:
                continue
    return False

last_processed_message = ""  # memory to track last response
pyautogui.click(x=850, y=1046)
time.sleep(1) 

while True:
    pyautogui.click(x=685, y=226)
    pyautogui.moveTo(675, 196)
    pyautogui.mouseDown()
    pyautogui.moveTo(666, 1013, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    chat_history = pyperclip.paste()

    # Get last message only
    last_lines = chat_history.strip().splitlines()
    last_message = last_lines[-1] if last_lines else ""

    if last_message != last_processed_message and is_last_message_from_sender(chat_history):
        print("📨 New message detected, responding...")

        data = {
            "model": "llama3-70b-8192",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a person named Tejesh Reddy who speaks Telugu as well as English. "
                        "You are from India and you are a coder. You analyze chat history and respond like Tejesh Reddy. "
                        "Keep the reply human-like, friendly, fluent in English with a few Telugu words, use emojis when needed, and make it short but meaningful."
                    )
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            reply = result['choices'][0]['message']['content']
            print("🤖 Reply:", reply)

            pyperclip.copy(reply)
            time.sleep(1)

            pyautogui.click(x=1159, y=964)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pyautogui.press('enter')

            # Update memory so it won't resend
            last_processed_message = last_message
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    else:
        print("⏳ No new message or not from Vanga.")

    time.sleep(2)  # avoid hammering the system
