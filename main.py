import discord
import logging
from discord.ext import commands


class MyClient(discord.Bot):
    # Retrieve the logging object for the client.
    logger = logging.getLogger('discord.client')

    async def on_ready(self):
        # Note the bot successfully logged in and is ready to work.
        self.logger.info(f'Logged is as {self.user}!')

    # Requires the MSG_CONTENT intent to work.
    # See https://support-dev.discord.com/hc/en-us/articles/4404772028055-Message-Content-Privileged-Intent-FAQ
    async def on_message(self, message: discord.Message):
        if message.content == "PING":
            # Respond to any 'PING' messages with a message that says 'PONG'.
            channel = message.channel
            await channel.send('PONG')

        # Log any messages sent on the server.
        self.logger.info(f'Message from {message.author}: {message.content}')


# Create an intents object and enable the MSG_CONTENT intent for the on_message event
intents = discord.Intents.default()
intents.message_content = True

# Construct an instance of the Client with the given intents.
client = MyClient(intents=intents)
# Request console input for the bot token and pass it to the client for it to initialize
client.run(input('Enter a bot token: '))
