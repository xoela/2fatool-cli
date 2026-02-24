# 2FA Code Generator

A terminal-based TOTP code generator. Enter your 2FA secret key and get live codes with a countdown timer.

![Python](https://img.shields.io/badge/Python-3.x-blue)

## Features

- Live 6-digit TOTP code display
- Color-coded countdown timer with progress bar
- "Code expired!" alert in red when the timer runs out
- Backspace to switch to a different secret key
- Works with any standard TOTP secret (Google Authenticator, Authy, etc.)

## Setup

```bash
pip install -r requirements.txt
```
## Usage

```bash
python 2fa.py
```

1. Enter your 2FA secret key when prompted
2. Your code and time remaining will display on screen
3. Press **Backspace** to enter a different key
4. Press **Ctrl+C** to exit
