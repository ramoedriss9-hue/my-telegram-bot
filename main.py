import telebot
import requests

# http://t.me/CryptoQiPrice_bot
BOT_TOKEN = '8912709590:AAGvO4dRaQA7_OqRx-FhUISOuhUebrD-acw'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'price'])
def send_prices(message):
    try:
        # هێنانی نرخی کریپتۆ لە CoinGecko
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,the-open-network&vs_currencies=usd"
        response = requests.get(url).json()
        
        btc_price = response['bitcoin']['usd']
        ton_price = response['the-open-network']['usd']
        
        # نرخی دۆلار بەرامبەر دینار
        usd_to_iqd = 151500 
        
        text = f"💰 **نرخی دەستبەجێی دراوەکان** 💰\n\n"
        text += f"🪙 بیتکۆین (BTC): ${btc_price:,}\n"
        text += f"💎 تۆنکۆین (TON): ${ton_price}\n"
        text += f"💵 100 دۆلار بەرامبەر دینار: {usd_to_iqd:,} IQD\n\n"
        text += f"🔄 بۆ نوێکردنەوە کلیل لەسەر /price بکە."
        
        bot.reply_to(message, text, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, "ببوورە، کێشەیەک لە هێنانی نرخەکاندا هەیە.")

print("بۆتەکە ئێستا کاردەکات...")
bot.infinity_polling()
