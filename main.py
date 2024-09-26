import logging
from googletrans import Translator
from aiogram import Bot, Dispatcher, executor, types
from define import get_definitions

API_TOKEN = '7363152877:AAGgfO5VTiRkWn_73kB9Rp4CExSTE1ndmwM'

translator = Translator()

# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)






@dp.message_handler(commands=['start'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends   `/help` command

    """

    await message.reply("WELCOME to asadbek's bot \n u gonna love this 🗿")








@dp.message_handler(commands=['help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends  `/help` command

    """

    await message.reply("TROUBLE? contact to @HackSecure_admin")









@dp.message_handler()
async def trans(message: types.Message):
    lang = translator.detect(message.text).lang
    
    if len(message.text.split()) > 2:  # Translate if more than two words
        dest = 'uz' if lang == 'en' else 'en'
        translated_text = translator.translate(message.text, dest).text
        await message.reply(translated_text)
    else:
        # If it's a single word, fetch its definition
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = get_definitions(word_id)

        # Handle the case where the word is not found
        if 'error' in lookup:
            await message.reply(lookup['error'])
        else:
            # Send definitions and phonetic/audio details
            definitions_text = "\n".join(lookup["definitions"]) if lookup.get("definitions") else "No definitions found"
            await message.reply(f"""Word: {word_id}
Phonetic: {lookup["phonetic"]}
Definitions:
{definitions_text}""")

            # Send audio if available
            if lookup['audio'] != 'No audio available':
                await message.reply_voice(lookup['audio'])
            else:
                await message.reply('unfortunately audio is not available🥲')










if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
