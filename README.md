# 🤖 Fancy Fonts Bot (for Telegram: Chat App)

A simple Telegram bot that runs inline and converts your input into cool looking, weird and unique unicode fonts 𝒍𝒊𝒌𝒆 𝒕𝒉𝒊𝒔! Fonts are stored in a JSON file (see below for more info).

### Example Usage

> **[Input]** `The quick brown fox jumps over the lazy dog.`
> **[Example Output]** `𝓣𝓱𝓮 𝓺𝓾𝓲𝓬𝓴 𝓫𝓻𝓸𝔀𝓷 𝓯𝓸𝔁 𝓳𝓾𝓶𝓹𝓼 𝓸𝓿𝓮𝓻 𝓽𝓱𝓮 𝓵𝓪𝔃𝔂 𝓭𝓸𝓰.`

There are a lot more pre-defined fonts. The above example is my personal favourite defined as "Script" in the fonts file.

## 🚀 Getting Started

### Public Instance

I do have a public instance of the bot under the username [`@FancyFontsBot`](https://t.me/FancyFontsBot). However, it is not always online as I only really use it for testing the bot. You'll have to self-host it if you want to reliably use it. Follow the steps down below to get started on hosting the bot yourself.

### Prerequisites

- [Python](https://www.python.org/) 3.8 or above.
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot) (API Wrapper)

### Installing

1. Clone the repository. (I recommend creating a virtual environment)
```
git clone https://github.com/waterrmalann/telegram-fancy-fonts-bot.git
```
2. Install the requirements.txt
```
python -m pip install -r requirements.txt
```
3. Create a bot and grab the bot token by messaging `@BotFather` on Telegram.
4. Open `config.json` and put the bot token in `botToken`.
5. Run the project
```
python bot.py
```

### Configuration

Bot configuration is stored in the root directory in a JSON file called `config.json`. The file would look something like this:

```json
{
    "botName": "Fancy Fonts Bot",
    "botOwner": "@waterrmalann",
    "botToken": "your-bot-token-here"
}
```

- *(string)* **botName**: The name of the bot. (printed in the console)
- *(string)* **botOwner**: The username of the bot owner. (printed in the console)
- *(string)* **botToken**: The bot token you got from `@BotFather` on Telegram.

### Adding new fonts

Fonts are stored in a json file in the root directory with the name `fonts.json`. Each font is stored in this format:

```json
{
    "fontName": "FullWidth",
    "fontLower": "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
    "fontUpper": "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ",
    "fontDigits": "０１２３４５６７８９"
}
```

Leave an empty string for empty parameters. It will default to english letters and numbers. This can also be changed if you modify the `default.json` in the fonts folder (for eg: using a custom fallback font).

- **fontName**: The name of the font.
- **fontUpper**: Uppercase letters of that font.
- **fontLower**: Lowercase letters of that font.
- **fontDigits**: Numbers of that font.

Note: **fontLower** and **fontUpper** must always be 26 characters. **fontDigits** must always be 10 characters. The pseudofont class currently isn't failsafe. Foolproofing it is on my todo list.

## 🤝 Contributing

Contributions are accepted and there really isn't any strict rules. Feel free to open a pull request to fix any issues or to make improvements you think that should be made. You can also add new fonts to the font database or help me with the to-do list down below. Any contribution will be accepted as long as it doesn't stray too much from the objective of the bot. If you're in doubt about whether the PR would be accepted or not, you can always open an issue to get my opinion on it.

## 📃 To-Do

- Foolproof the pseudofont class to support invalid definitions.
- Make the psuedofont class more advanced to support custom symbols and replacements with more than 1 character. (eg: "V" to "\\/")
- Add more fonts.

License
----

MIT License, see [LICENSE](LICENSE)