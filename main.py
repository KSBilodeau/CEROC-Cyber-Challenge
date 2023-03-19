import discord
import logging

from discord.ext import commands


class MyBot(commands.Bot):
    # Retrieve the logging object for the client.
    logger = logging.getLogger('discord.bot')

    async def on_ready(self):
        # Load the extension
        await self.load_extension('challenge')

        # Note the bot successfully logged in and is ready to work.
        self.logger.info(f'Logged is as {self.user}!')


# Create an intents object and enable the MSG_CONTENT intent for the on_message event
intents = discord.Intents.default()
intents.message_content = True

# Construct an instance of the Client with the given intents.
bot = MyBot(intents=intents, command_prefix="nibble ")
# Request console input for the bot token and pass it to the client for it to initialize
bot.run(input('Enter a bot token: '))
