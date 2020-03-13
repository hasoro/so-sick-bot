import discord
import random
client = discord.Client()
x=0
@client.event
async def on_ready():
    print(client.user.id)
    print('ready')
    game = discord.Game("\"안녕\"이라고 인사하세요!")
    await client.change_presence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("말걸지마라 애송이")
    if message.content.startswith("시발"):
        await message.channel.send("욕하지마라 애송이:middle_finger:")
    if message.content.startswith("주사위"):
        x = 0
        x = random.randint(1, 6)
        await message.channel.send("%d"%x)
    if message.content.startswith("동전"):
        x = 0
        x = random.randint(1, 2)
        if x == 1 :
            await message.channel.send("앞면")
        else:
            await message.channel.send("뒷면")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
