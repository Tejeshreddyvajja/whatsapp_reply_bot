# WhatsApp Reply Bot

An automated WhatsApp bot that responds to messages using AI, specifically designed to reply as "Tejesh Reddy" with a Telugu/English speaking persona.

## Features

- **Auto-detection**: Monitors WhatsApp chat for new messages from specific senders
- **AI-powered responses**: Uses GROQ AI API (llama3-70b-8192 model) to generate contextual replies
- **Personalized responses**: Responds in the style of Tejesh Reddy, mixing English and Telugu
- **Memory system**: Prevents duplicate responses by tracking last processed message
- **Automatic interaction**: Uses PyAutoGUI to automate WhatsApp interactions

## Requirements

- Python 3.7+
- PyAutoGUI
- PyPerClip
- python-dotenv
- requests

## Installation

1. Clone this repository
2. Install required packages:
   ```bash
   pip install pyautogui pyperclip python-dotenv requests
   ```
3. Create a `.env` file and add your GROQ API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Open WhatsApp Web or WhatsApp Desktop
2. Position the chat window properly
3. Run the bot:
   ```bash
   python program.py
   ```

## Files

- `program.py` - Main bot application
- `main.py` - Utility script for finding mouse coordinates
- `.env` - Configuration file (not included in repository)
- `trail.py` - Test/development file

## Configuration

The bot is currently configured to:
- Monitor messages from "Vanga" (can be changed in code)
- Respond as "Tejesh Reddy"
- Use specific screen coordinates for WhatsApp interaction

## Note

This bot requires screen coordinates to be calibrated for your specific WhatsApp setup. Use `main.py` to find the correct coordinates for your screen resolution and WhatsApp window position.

## Disclaimer

This project is for educational purposes. Make sure to comply with WhatsApp's terms of service and use responsibly.
