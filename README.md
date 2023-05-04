# Discord Language Flag Bot

A Discord bot that detects messages in different languages and reacts with the appropriate flag emoji for each language. The bot also translates non-English messages to English and sends the translated text to the chat.

<img src="https://github.com/lewispour/discord-translate-messages-to-english-bot/blob/a3a6f18d3ead5631c1f04ceef5fb979aaf8b3051/usage.gif" alt="Usage GIF" width="800">

## Features

- Detects messages in various languages
- Reacts to messages with the corresponding flag emojis
- Translates non-English messages to English using the DeepL API
- Sends translated messages to the chat

## Supported Languages

- English (🇬🇧)
- French (🇫🇷)
- German (🇩🇪)
- Spanish (🇪🇸)
- Italian (🇮🇹)
- Dutch (🇳🇱)
- Portuguese (🇵🇹)
- Swedish (🇸🇪)
- Russian (🇷🇺)
- Chinese Simplified (🇨🇳)
- Chinese Traditional (🇹🇼)

## Requirements

- Python 3.6+
- `discord.py` library
- `requests` library
- `langdetect` library

You can install the required libraries using the following command:

```
pip3 install discord.py requests langdetect
```
## Configuration

1. Create a new bot on the [Discord Developer Portal](https://discord.com/developers/applications) and obtain the bot token.
2. Replace the placeholder text `<your-bot-token>` in the code with your bot's token.
3. Sign up for a [DeepL API key](https://www.deepl.com/pro#developer) and replace the placeholder text `<your-deepl-auth-key>` in the code with your API key.
4. Invite the bot to your server.

## Usage

Run the Python script, and the bot will start detecting languages of messages sent in the server. It will react to messages with the corresponding flag emojis and translate non-English messages to English.

## Contributing

We encourage you to contribute to this project by adding support for more languages or improving its existing features. To get started, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement the new language or feature you wish to add.
4. Test your changes to ensure everything works as expected.
5. Submit a pull request with a clear description of the changes you made.

Your contributions will help make the bot more versatile and useful for a wider range of Discord communities.
