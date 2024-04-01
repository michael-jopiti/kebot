# Author: Michael Jopiti
# Date: 31.03.2024

import sys, os, traceback
from dotenv import load_dotenv

from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

import commands

import sys
sys.path.append("/Users/michaeljopiti/kebot")

from spotify import Spotify as spotify

##################
# Import TOKEN, BOT_NAME from .env
##################

load_dotenv()

TOKEN = os.getenv("TOKEN")
BOT_NAME = os.getenv("BOT_NAME")


##################
# Responses
##################

def handle_response(text: str) -> str:

    # As python is case sensitive, we need to process the text case!
    processed: str = text.lower()

    if "Hello" in text:
        return "Hello there!"
    
    return "I don't understand what you're saying, try again please :') \n If you don't know what to do, type: /help"


##  Logic to behave according to user input and type

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'\t \tUser ({update.message.chat.id}) in {message_type}: "{text}"')
    #according if it is in a group or in private chat, we need different behaviours

    if message_type == "group":
        if BOT_NAME in text:
            new_text: str = text.replace(BOT_NAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return 
        
    else: 
        response : str = handle_response(text)

    #for debugging purposes
    print('\t \tBot: ',  response)

    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _, _, tb = sys.exc_info()
    line_number = traceback.extract_tb(tb)[-1][1]
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
    print(f"Update {update} caused error {context.error}:\n{''.join(error_traceback)}")


def main():
    print("Starting kebot ... ")
    spotify.main()

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', commands.start_command))
    app.add_handler(CommandHandler('help', commands.help_command))
    app.add_handler(CommandHandler('spotifyHelp', commands.spotifyHelp_command))
    app.add_handler(CommandHandler('addSong', commands.addSong_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    ## Checks for new messages every 3 seconds
    print("\t Polling ... ")
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
  main()