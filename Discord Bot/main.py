import discord
import discord as db
import asyncio
import json
from bot_token import token


warned_people = {}
bad_words = ['hurensohn', 'hundesohn', 'badwordtest', 'huren.sohn', 'nudes', 'bastard', '!server', "abbo", "abo", "beeyotch", "biatch","bitch", "chinaman",]

client = db.Client()

@client.event
async def on_ready():
    print('Eingeloggt als {}'.format(client.user.display_name))
    print('')
    print('Hallo ByteException !')
    print('')
    print('Commands:')
    print('!setup : Setup Starten')
    print('!muteinfo : Mute Info')
    print('!bot : Bot Info ')
    print('!delete [] : Narichten Löschen')
    print('!invite : Einladungslink des Servers!')
    print('!update : Suche nach Bot Updates')
    print('!version : Frage die Version des Bots ab ')
    print('!info : Bot unterstützung')
    print('!admin : Admin rufen!')
    print('!help : Hilfe!')
    
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("Führt deine Befehle aus!"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("Programming ..."), status=discord.Status.online)
        await asyncio.sleep(1)
        await client.change_presence(activity=discord.Game("Programming .."), status=discord.Status.online)
        await asyncio.sleep(1)
        await client.change_presence(activity=discord.Game("Programming ."), status=discord.Status.online)
        await asyncio.sleep(2)

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    try:
        if len(warned_people[message.author.id]) >= 5:
            await message.channel.purge(limit=1)
            return
        
    except KeyError:
            warned_people[message.author.id] = []

    if message.content.startswith('!delete'):
        messagelimit = int(message.content.split('!delete ', 1)[1])
        await message.channel.purge(limit=messagelimit + 1)
        
    


    


    if any(word in message.content for word in bad_words):
        await warn_user(author=message.author.id, message=message.content)
        await message.channel.purge(limit=1)
        await message.channel.send("**Dieses Word ist auf der Blacklist!** *Deine Verwarnungen wurden automatisch um 1 erweitert!*")

    if message.content.startswith("!muteinfo"):
        await message.channel.send("**Solltest du die 5 Warns ereichen wirst du automatisch permanent gemutet!** *Diese nachricht verschwindet nach 10 Sekunden*")
        await asyncio.sleep(10)
        await message.channel.purge(limit=2)

    if message.content.startswith("!update"):
        await message.channel.send("**Suche nach Update ...**")
        await asyncio.sleep(4)
        await message.channel.send("**Kein Update gefunden!**")

    if message.content.startswith("!invite"):
        await message.channel.send("**Der Einladungslink des Server lautet** : https://discord.gg/DjKQkUmGCA")
    
    if message.content.startswith("!version"):
        await message.channel.send("**Ich laufe auf der Version 1.0 - BETA**")
    
    if message.content.startswith("!info"):
        await message.channel.send("**Dieser Bot Wird noch Unterstützt!**")
    
    if message.content.startswith("!setup"):
        await message.channel.send("**Solltest du das Setup bereits ausgeführt haben und du es nocheinmal Wiederholst könnte es deinen Server beschädigen!**")
        await asyncio.sleep(2)
        await message.channel.send("**Bot wird nun eingerichtet!**")
        await asyncio.sleep(5)
        await message.channel.send("**Der Bot ist nun Fertig eingerichtet!**")

    if message.content.startswith("!server"):
        await message.channel.send("**Dieser Command wurde gelocked !**")
    
    if message.content.startswith("!admin"):
        await message.channel.send("Admin gerufen!")
        await asyncio.sleep(2)
        await message.channel.purge(limit=2)

    if message.content.startswith("!myname"):
        await message.channel.send(message.channel.user.send.display_name)

        

    if message.content.startswith("!help"):
        await message.channel.send('**Hilfe** \r\n'
                                '!update - Suche nach einem Update! \r\n'
                                '!invite - Hiermit kannst du Freunde einladen! \r\n'
                                '!version - Frag die Version des Bots ab! \r\n'
                                '!info - Wird der Bot noch unterstützt? \r\n'
                                '!setup - Setzte den Bot auf! \r\n'
                                '!muteinfo - Mute info')


    if message.content.startswith("!bot"):

        zerotwo = discord.Embed(title = "ZeroTwo Bot!",
                                description = "[Hallo ich bin der ZeroTwo Bot solltest du hilfe brauchen schreibe einfach einen Befehl!]", color=0xff007b)
        zerotwo.set_image(url="https://ibb.co/gmv43XD")
        await message.channel.send(zerotwo)
    
async def warn_user(author, message):
    global warned_people
    if author in warned_people.keys():
        warned_people[author].append(message)

    else:
        warned_people[author] = [message]

    with open('userdata.json', mode='w') as file:
        json.dump(warned_people, file)





client.run(token)