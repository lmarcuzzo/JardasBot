import random
import datetime
from datetime import timedelta

from discord import Message
from database import DBdelete
from database import DBupdate
from database import DBquery

from responses import BomDia
from responses import Wronged
from responses import Warning
from responses import Thanks
from responses import Roasting
from responses import Fortunes

from utils.state import STATE
from fortune import fortune as fortuneQuote

######################################################
async def handle_roast(message: Message):
    roast = random.choice(Roasting.arr_roast)
    for mentioned_user in message.mentions:
        response = f"{mentioned_user.mention}, {roast}"
        await message.channel.send(response)


async def self_roast(message: Message):
    roast = random.choice(Roasting.arr_roast)
    response = f"{message.author.mention}, {roast}"
    await message.channel.send(response)


############################
async def change_intensity(value: str):
    value = int(value)
    if value >= 1 and value <= 4:
        intensity = value

    return intensity


####################################################################
async def wakeup(message, state):
    print(state)
    if state == STATE.SLEEP:
        await respond_acordar(message)
    else:
        await message.channel.send("Já tou acordado caralho, cala-te")


async def respond_acordar(message: Message):
    response = random.choice(BomDia.arr_wake)
    excluded = DBquery.query_leastFavourable()
    DBupdate.update_positiveFavour(str(message.author))
    if excluded:
        response += f" Excepto tu {excluded}! Tu podes ir pro caralho"
    await message.channel.send(response)


####################################################################
async def vaidormir(message: Message):
    DBupdate.update_negativeFavour(str(message.author))
    response = random.choice(Wronged.arr_wronged)
    await message.channel.send(response)


#####################################################
async def respond_nuke(message, allowed_mentions):
    today = datetime.date.today()
    last_date = DBquery.query_nuke_last_date()
    if str(last_date) != str(today):
        DBdelete.clear_nuke_table()

    prev_cnt = DBquery.query_nuke_count()
    DBupdate.update_nuke_count(str(message.author))
    counter = DBquery.query_nuke_count()

    if counter == prev_cnt:
        await message.channel.send("Não há repeats")
        return
    else:
        DBupdate.update_negativeFavour(str(message.author))

    if counter % 10 == 0:
        await nuke_channel(message, allowed_mentions)
    else:
        response = random.choice(Warning.arr_warn)
        await message.channel.send(response)


#################################################################
async def russian_roulette(message: Message):
    bullet = random.randint(1, 6)
    if bullet == 1:
        try:
            timeout_duration = timedelta(hours=1)
            await message.author.timeout(timeout_duration, reason="Drawn the bullet in Russian Roulette")
            await message.channel.send(f"{message.author.mention} has died")
        except Exception as e:
            await message.channel.send(f"Error timing out {message.author.mention}: {e}")
    else:
        await message.channel.send(f"{message.author.mention} is safe!")

#################################################
async def handle_fortune(message:Message):
    #fortune = random.choice(Fortunes.arr_fortune)
    response = f"{message.author.mention}, esta semana {fortuneQuote()}"
    await message.channel.send(response)

async def nuke_channel(message, allowed_mentions):
    pass
    # await message.channel.send("Nuke activated...")
    # await message.channel.send("NOW I AM BECOME DEATH, THE DESTROYER OF WORLDS...")
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
    # time.sleep(5)
    # await message.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)


#####################################################
async def respond_defuse(message: Message):
    prev_cnt = DBquery.query_nuke_count()
    DBupdate.update_defuse_count(str(message.author))
    counter = DBquery.query_nuke_count()

    if counter == prev_cnt:
        await message.channel.send("Não há repeats")
        return
    else:
        DBupdate.update_positiveFavour(str(message.author))

    response = random.choice(Thanks.arr_thanks)
    await message.channel.send(response)


#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

async def glock_roulette(message: Message):
    bullet = random.randint(1, 99)
    if bullet != 1:
        try:
            timeout_duration = timedelta(minutes=10)
            await message.author.timeout(timeout_duration, reason="Drawn the bullet with a gun.")
            await message.channel.send(f"{message.author.mention} has died")
        except Exception as e:
            await message.channel.send(f"Error timing out {message.author.mention}: {e}")
    else:
        await message.channel.send(f"{message.author.mention} is safe! The gun jammed.")

async def call_JECS(message: Message):
    if str(message.author) == "leomarcuzzo":
        try:
            await message.channel.send("<@192306440315076608> anda cá.")
            await message.channel.send("<@192306440315076608> anda cá.")
            await message.channel.send("<@192306440315076608> anda cá.")
        except Exception as e:
            await message.channel.send("Error sending message: {e}")
    else:
        pass

async def callKika(message: Message):
    if str(message.author) == "leomarcuzzo":
        try:
            await message.channel.send("<@402215966169235466> desenvolva-me.")
        except Exception as e:
            await message.channel.send("Error sending message: {e}")
    else:
        pass
