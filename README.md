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
    Create a `.env` file and add your Telegram Bot API Token, Telegram Bot Name, Telegram App ID, Telegram App Hash, Telethon session


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
[![Watch the video]()

### Resources
[How to Build a Telegram Bot: A Beginner's Step-by-Step Guide](https://tjtanjin.medium.com/how-to-build-a-telegram-bot-a-beginners-step-by-step-guide-c671ce027c55)

[Telegram File Handling Documentation](https://docs.python-telegram-bot.org/en/v13.1/telegram.file.html)

[Receiving Files in Telegram Bot](https://grammy.dev/guide/files#receiving-files)

[Python MD5 Hashing Example](https://mkyong.com/python/python-md5-hashing-example/)

[How to Dockerize a Telegram Bot: A Step-by-Step Guide](https://tjtanjin.medium.com/how-to-dockerize-a-telegram-bot-a-step-by-step-guide-b14bc427f5dc)

[Creating Unit Tests for a Python Telegram Bot](https://stackoverflow.com/questions/63623930/how-to-create-unit-test-for-a-python-telegram-bot)

[Integration Tests for a Telegram Bot](https://dev.to/blueset/how-to-write-integration-tests-for-a-telegram-bot-4c0e)

