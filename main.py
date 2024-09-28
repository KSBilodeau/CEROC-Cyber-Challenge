import discord
import logging

from discord.ext import commands

class MyBot(commands.Bot):
    # Retrieve the logging object for the client.
    logger = logging.getLogger('discord.bot')

    async def setup_hook(self):
        # Load the command extension/s before the bot starts
        await self.load_extension('challenge')

    async def on_ready(self):
        # Note the bot successfully logged in and is ready to work.
        self.logger.info(f'Logged is as {self.user}!')


# Create an intents object and enable the MSG_CONTENT intent for the on_message event
intents = discord.Intents.default()

# Construct an instance of the Client with the given intents.
bot = MyBot(intents=intents, command_prefix=[])
# Request console input for the bot token and pass it to the client for it to initialize
bot.run(input('Enter a bot token: '))
