from telebot import TeleBot, formatting
import os


from dotenv import load_dotenv
load_dotenv()

bot = TeleBot(
    token=os.getenv("BOT_TOKEN"),
    parse_mode='html',
    disable_web_page_preview=True
)
chat_id = os.getenv("CHAT_ID")
if __name__ == '__main__':
    # bot.send_message(chat_id=os.getenv("CHAT_ID"), text=f"Bot {formatting.hbold('python')} dasturlash tilida yozilgan")
    bot.send_photo(photo=open("logo.png", "rb"), chat_id=chat_id, caption=f"{formatting.mbold('Logo')}ga baho beriing")
