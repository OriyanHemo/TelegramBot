# Telegram Bot README

## Introduction

This project is a simple Telegram bot that interacts with users by calculating and returning the hash of given image files (*.jpg/*.jpeg only). Any other file types or text messages will result in an error. The bot is tested through an automated black-box testing framework, ensuring robust functionality without accessing the internal code.

## Features

- **Image Hash Calculation**: When a *.jpg or *.jpeg image file is sent to the bot, it calculates the hash of the image and returns it.
- **Error Handling**:
  - Sending files other than *.jpg/*.jpeg will return an error message.
  - Sending text messages will return an error message.


### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/OriyanHemo/TelegramBot
    cd TelegramBot
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Set Up Environment Variables**:
    Create a `.env` file and add your Telegram Bot API Token(6970268054:AAG-nYrs8VwwOE8Fv6mGbZNIiRQVIpEhRd4), Telegram Bot Name(@NSO145Bot), Telegram App ID, Telegram App Hash, Telethon session


### Running the Bot

To run the bot, execute the following command:
```python
python3 -u ./main.py
```
### Running the Tests

To run the test, execute the following command:
```python
python3 -m pytest ./test_nsobot.py
```

### Running in a Docker
To run the docker, execute the following command:
```python
- sudo systemctl start docker
- docker build -t my_telegram_bot .
- sudo docker run my_telegram_bot
```
### Video Demonstration
[Screencast from 2024-05-17 17-10-26.webm](https://github.com/OriyanHemo/TelegramBot/assets/121008849/c08d1bbe-1256-4770-b6fd-2bad3ff94ae4)



