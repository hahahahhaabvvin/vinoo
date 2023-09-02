import discord
import random
import os
import requests
from discord.ext import commands
from m1l2.bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
guess_game = None

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pwd(ctx):
    await ctx.send(gen_pass())

@bot.command()
async def guess(ctx):
    global guess_game

    guess_game = random.randint(1, 10)
    
    await ctx.send("Tebak angka 1 sampai 10, jawab dengan $answer")

@bot.command()
async def answer(ctx, number):
    if guess_game == int(number):
        await ctx.send("Selamat anda benar")
    else:
        await ctx.send("Jawaban salah, silahkan coba lagi")

@bot.command()
async def mem(ctx):
    daftar_gambar = os.listdir('images')
    gambar = random.choice(daftar_gambar)
    
    with open(f'images/{gambar}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")
