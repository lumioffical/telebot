import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "7718369766:AAEGUox4TQ3H5rXP83MiuIJRuyR_YfHS-RY"
WEB_APP_URL = "https://telebot-4x0u.onrender.com"  # Замени на свою ссылку

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Открыть мини-приложение", web_app=WebAppInfo(WEB_APP_URL))
    keyboard.add(button)
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы открыть мини-приложение:", reply_markup=keyboard)

bot.polling(none_stop=True,
timeout=60)