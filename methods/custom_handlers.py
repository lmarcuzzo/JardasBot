import random
from discord import Message
##
#from responses import German,Latin


###########################################################################
async def rebola_is_conas(message: Message):
    message.channel.send(message, "oh caralho e parares com essa merda?")
    message.channel.send(message, "És estupido ou que?")
    message.channel.send(message, "Deves ter batido com a cabeça em miudo só pode")
    message.channel.send(message, "Caralho do moço")

######################################################
async def german_reply(message: Message):
    roll = random.randint(1, 30)
    if roll == 1:
        response = random.choice(dict_german)
        await message.channel.send(response)
        return True
    return False

######################################################
async def latin_reply(message: Message):
    roll = random.randint(1, 30)
    if roll == 1:
        response = random.choice(dict_latin)
        await message.channel.send(response)
        return True
    return False


######################################################
async def french_reply(message: Message):
    roll = random.randint(1, 30)
    if roll == 1:
        response = random.choice(dict_french)
        await message.channel.send(response)
        return True
    return False

##DICTS
dict_german = [
    "Ich lerne Deutsch für dich <3",
    "Es ist Mamma",
    "Heil JardasBot",
    "Du bist mein Liebling",
    "Scheiße",
    "Scheiß drauf, wir Ball",
    "gespannt",
    "Ich, deine Mutter",
    "Das war's und hör auf, dumm zu sein",
    "90 Tage Verlobte heute?",
]

dict_latin = [
    "Carpe diem",
    "Tua mater latior quam Rubicon est",
    "Quid quid latine dictum sit, altum viditur",
    "In vino veritas",
    "Cave Canem",
    "Dictum factum.",
    "Dum vita est, spes est.",
    "Sapientia potentia est.",
    "Pax vobiscum.",
    "Suus 'tempus ad duolingo lectionem.",
    "Accusare nemo se debet nisi coram Deo.",
]
