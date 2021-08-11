import data as data
import discord
import option as option
from discord.ext import commands
from pip._vendor.certifi.__main__ import args

from utils import *
from functions import *


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='!m ', intents=intents)
game = Game()
#kelime = Kelime()

@Bot.event
async def on_ready():
    print("I'm ready for the party ")

@Bot.event
async def on_member_join(member):
    channel= discord.utils.get(member.guild.text_channels, name=" hoşgeldiniz ")
    await channel.send(f"{member} aramıza katıldı. Hoş geldin {member}.")
    print(f"{member} aramıza katıldı. Hoş geldi.")
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="elveda")
    await channel.send(f"{member} aramızdan ayrıldı. Press F")
    print(f"{member} aramızdan ayrıldı. Press F")


@Bot.command(aliases=["game", "oyun"])
async def zar(msg, *args):
    if 'salla' in args:
        await msg.send(game.roll_dice())
    else:
        await msg.send('Zarı salla ')

@Bot.command()
async def naber(msg):
    await msg.send('Sanane Kardeş sanane')

@Bot.command()
@commands.has_role("admin")
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@Bot.command()
@commands.has_role("admin")
async def kick(ctx, member:discord.Member, *args, reason="Yok"):
   await member.kick(reason=reason)
   #await ctx.send('Kalk burdan git')

@Bot.command()
@commands.has_role("admin")
async def ban(ctx, member:discord.Member, *args, reason="Yok"):
   await member.ban(reason=reason)


#@Bot.command()
#async def kufur(msg, *args):
 #   if 'et' in args:
   #     await msg.send(kelime.liste)
    #else:
     #   await msg.send('Küfür etmiyorum ')
@Bot.command()
async def çal(msg, *args):
    if "çal" in args:
       #ilk önce yeniden cümleyi kelime kelime böler
       #data= data.split()
       #burada ise örneğin aleyna tilki çal diyoruz ya arananı aleyna tilki yani çaldan öncesi#olarak belirliyoruz.
       parcaismi = "pablo"
       for i in args:
           parcaismi = parcaismi + i
       # m.speak("Bekle Can Senin için "+ parcaismi + " yi çalıyorum")
       #Otomasyon uygulamamıza chrome'u açtırıyoruz
           driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chrome.exe')
       #burada youtube'un link oluşturma sisteminden yararlandım. #youtubeda şu şekilde link oluşturabilirsiniz#https://www.youtube.com/results?search_query=parcaismi şeklinde
           driver.get("https://www.youtube.com/results?search_query="+parcaismi);
       #burada tıklayacağı şeyi ben video başlığını seçtim onu belirliyoruz.
           select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
       #Bu döngüde ise ona tıklıyor.for option in select_element:
           option.find_element_by_xpath('//*[@id="video-title"]').click()
           break

Bot.run(Token)