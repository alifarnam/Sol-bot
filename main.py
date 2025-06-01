import telebot
import requests

TOKEN = 'توکن رباتت اینجا'
USER_ID = 289615947  # آیدی عددی شما

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id == USER_ID:
        bot.send_message(message.chat.id, "🤖 ربات فعال است! منتظر سیگنال‌ باش...")

@bot.message_handler(commands=['trend'])
def get_trending_coins(message):
    if message.chat.id == USER_ID:
        url = "https://api.birdeye.so/public/tokenlist?sort_by=volume_24h&order=desc&limit=5"
        headers = {"x-chain": "solana"}
        res = requests.get(url, headers=headers)
        data = res.json().get('data', [])
        text = "🔥 5 میم‌کوین ترند سولانا:\n\n"
        for i, token in enumerate(data[:5]):
            text += f"{i+1}. {token['name']} - ${round(float(token['volume_24h'])/1e6, 2)}M\n"
        bot.send_message(message.chat.id, text)

bot.infinity_polling()
