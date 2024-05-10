import discord
import random

client = discord.Client()

# List of welcome messages
welcome_messages = [
    "Welcome to the server!",
    "Hey there! Welcome aboard!",
    "Nice to meet you! Welcome to our server!",
    "Greetings! Welcome to our community!",
    "Hello and welcome! We're glad to have you here!",
]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):
    # Select a random welcome message
    welcome_message = random.choice(welcome_messages)
    # Send the welcome message to the new member
    await member.send(welcome_message)

# Replace 'YOUR_TOKEN' with your actual bot token
client.run('YOUR_TOKEN')
