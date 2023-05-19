import discord
import firebase_admin
import logging

from discord.ext import commands
from firebase_admin import credentials


class MyBot(commands.Bot):
    # Retrieve the logging object for the client.
    logger = logging.getLogger('discord.bot')

    async def setup_hook(self):
        # Load the command extension/s before the bot starts
        await self.load_extension('challenge')

    async def on_ready(self):
        # Note the bot successfully logged in and is ready to work.
        self.logger.info(f'Logged is as {self.user}!')


# Fetch the database credentials using the user provided Firebase Service Account Key JSON file
cred = credentials.Certificate(input("Enter Service Account Key Path: "))

# Initialize the app with the user provided service credentials, establishing admin access
firebase_admin.initialize_app(cred, {
    'databaseURL': input("Enter Database URL: ")
})

# Set the bot to utilize default permissions necessary for the library to function
intents = discord.Intents.default()

# Construct an instance of the Client with the given intents.
bot = MyBot(intents=intents, command_prefix=[])

# Initialize the bot with the user provided token
bot.run(input('Enter a bot token: '))
