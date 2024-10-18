import discord

from .commands import voice
from .listeners import voice as voice_listener

# Inicializa o cliente do Discord
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
client = discord.Client(intents=intents)

# Registra os comandos
@client.slash_command(name="entrar", description="Entra na chamada de voz.")
async def entrar(ctx):
    await voice.entrar(ctx)

# Registra os listeners
@client.event
async def on_ready():
    voice_listener.on_ready(client)

@client.event
async def on_voice_state_update(member, before, after):
    await voice_listener.on_voice_state_update(member, before, after, client)

def run():
    client.run(client.config.DISCORD_TOKEN)
