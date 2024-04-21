
from utils.aov import ipresolver, mail, friedcheck, linkedaccounts, stw, xboxinfo
import requests
import discord
from discord.ext import commands
from discord import Embed
intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix='!')
key = ""
que = 0
xuid = ''

@client.event
async def on_ready():
    print("Commands synced.")

@client.command(name="xbox_aov",description="Generate an AOV with an xBox username")
async def xbox_aov(ctx, username):
    global que
    que = que + 1
    msg = await ctx.send(content=f'Starting data scraping. You are number {que} in the que.')
    xuid = xboxinfo.xuid(username)
    ip = ipresolver.resolve(username)
    ipinfo = None
    if ip:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        country = data["country"]
        city = data["city"]
        zipCode = data["zip"]
        lat = data["lat"]
        lon = data["lon"]
        isp = data["isp"]
        region = data["regionName"]
        ipinfo=f'IP : {ip}\nRegion : {region}\nCountry : {country}\nCity : {city}\nZipCode : {zipCode}\nLatitude : {lat}\nLongitude : {lon}\nISP : {isp}'
    xuid = xboxinfo.xuid(username)
    print (xuid)
    _, _, year, _, = stw.get_achievement_data(key, xuid)
    _, month, _, _, = stw.get_achievement_data(key, xuid)
    _, _, _, day = stw.get_achievement_data(key, xuid)
    unlocked, _, _, _, = stw.get_achievement_data(key, xuid)
    email = mail.findmail(username, 'aov/xbox30iso.txt')
    epic = linkedaccounts.findepic(username)
    fried = friedcheck.fried(username)
    embed = Embed(color=0x0099ff, title=f'AOV For {username}', description=f":globe_with_meridians: **IP & Location**\n```{ipinfo}```\n:link: **Linked Accounts**\n```Epic: {epic}\nXBL: {username} / {xuid}```\n:e_mail: **Possible Emails**\n```{email}```\n:fire: **Fried Check**```\nFried Status : {fried}```\n:warning: **Activity Status**\n```Too lazy to code just skid off of tracker or something```\n:earth_americas:  **STW Status**```Owned: {unlocked}\nPurchase Date:{month}\{day}\{year}```\n:receipt: **Receipt**\n```Im too lazy to code this, if you cant figure out how u fr got -1 braincell```\n:speaking_head: **Profile Link**\n```https://gamerdvr.com/player/{username}```")
    await msg.edit(content='', embed=embed)
    que = que - 1
client.run('')
