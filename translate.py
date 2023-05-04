import discord
import requests
from langdetect import detect

client = discord.Client()
deepl_auth_key = "<your-deepl-auth-key>"

language_emojis = {
    "en": "🇬🇧",
    "fr": "🇫🇷",
    "de": "🇩🇪",
    "es": "🇪🇸",
    "it": "🇮🇹",
    "nl": "🇳🇱",
    "pt": "🇵🇹",
    "sv": "🇸🇪",
    "ru": "🇷🇺",
    "zh-cn": "🇨🇳"
}

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # Check if the message was sent by the bot itself
    if message.author == client.user:
        return

    # Detect the language of the message
    try:
        language = detect(message.content)
    except:
        return

    # Add the appropriate flag emoji for the detected language
    if language in language_emojis:
        await message.add_reaction(language_emojis[language])
    else:
        await message.add_reaction("❓")

    # If the message is not in English, translate it using DeepL API
    if language != "en":
        text = message.content
        headers = {"Authorization": f"DeepL-Auth-Key {deepl_auth_key}:fx"}
        data = {"text": text, "target_lang": "EN"}
        response = requests.post("https://api-free.deepl.com/v2/translate", headers=headers, data=data)
        if response.status_code != 200:
            await message.channel.send("Translation failed :(")
            return
        translated_text = response.json()["translations"][0]["text"]

        # Send a message with the Great Britain emoji and the translated text
        await message.channel.send(f"🇬🇧 {translated_text}")

client.run('<your-bot-token>')
