import hashlib
from typing import Final
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import imghdr
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
print('[...] Starting up bot...')

TOKEN: Final = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"[*] Welcome {update.message.from_user.first_name}! upload your JPG/JPEG images and get their hashes.")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'[x] Update {update} caused error {context.error}')

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message.photo:
        photo = message.photo[-1]
        file_id = photo.file_id
        file = await context.bot.get_file(file_id)
        file_url = file.file_path
        response = requests.get(file_url)
        if response.status_code == 200:
            image_data = response.content
            image_format = imghdr.what(None, h=image_data) 
            if image_format.lower() == 'jpeg' or image_format.lower() == 'jpg': # Check if the photo is JPG/JPEG
                image_hash = hashlib.md5(image_data).hexdigest()
                await message.reply_text(f"[*] The md5 hash of the image is: {image_hash}")
            else:
                await message.reply_text("[x] Unsupported image format.")
        else:
            await message.reply_text("[x] Failed to download the image.")
    else:
        await message.reply_text("[x] The received message is not an image.")


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()    
    app.add_handler(CommandHandler('start', start_command))    
    app.add_handler(MessageHandler(filters.ALL, message_handler))    
    app.add_error_handler(error)
    app.run_polling(poll_interval=1)






#python3 bot.py