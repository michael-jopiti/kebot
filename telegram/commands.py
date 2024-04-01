from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

import sys
sys.path.append("/Users/michaeljopiti/kebot")



categoryCommands = ["General", "Spotify"]
categoryCommands_str = ", ".join(element for element in categoryCommands)

spotifyCommands = ["/addSong", "/shuffle", "/Name"]
spotify_Commands_str = ", ".join(element for element in spotifyCommands)

#   Start the bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! What's up?")

#   Return all commands' categories
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"At the moment commands are available for the following categories: \n{categoryCommands_str}\n\n to see what they can do, type /CategoryOfInterestHelp")

#   Return all commands for spotify
async def spotifyHelp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"This is a comprehensive list of all the commands available for spotify: {spotify_Commands_str}")


#   Add song to a Playlist
async def addSong_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Your song is being added ...") # make sure the users feels listened

    text: str = update.message.text #store the input
    query = [key for key in text.split(",") if key != "/addSong"]   #split the input to store all information to send to the spotify API
    query[0] = " ".join(query[0].split()[1:]) #remove the /addSong

    print(f"\t Song request: {query}")  #debugging content of the request

    await update.message.reply_text("Your song has been added :)")