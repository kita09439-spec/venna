from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext
import logging

# --- KONFIGURASI ---
TOKEN = '8106816083:AAG_etalWeBPru8LTF3ddI7EPkh2cGReztw'  # Token bot kamu
CHANNEL_ID = '@MENANG123_RESMI'  # Channel tujuan
INTERVAL_SECONDS = 10800  # 3 jam = 10800 detik

# --- PESAN YANG DIKIRIM ---
def kirim_pesan(context: CallbackContext):
    teks = (
        "🎰 Selamat datang di <b>MENANG123</b>!\n\n"
        "Klik tombol di bawah untuk mulai bermain dengan provider SLOT ternama 🏆\n\n"
        "💵 <b>Jaminan menang berapapun kami bayar tuntas!</b>\n\n"
        "📲 Deposit via Transfer Bank, E-Money, atau Pulsa.\n\n"
        "🆘 Butuh bantuan? @MENANG123RAJASLOT"
    )

    tombol = [
        [InlineKeyboardButton("▶️ MAIN SEKARANG", url="https://t.me/Venna123Bot?start=start")],
        [InlineKeyboardButton("📲 DOWNLOAD APLIKASI", url="https://Bit.ly/MENANG123")],
        [InlineKeyboardButton("💬 LIVE CHAT", url="https://t.me/MENANG123RAJASLOT")]
    ]

    markup = InlineKeyboardMarkup(tombol)

    context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=teks,
        parse_mode='HTML',
        reply_markup=markup
    )

# --- MAIN ---
def main():
    logging.basicConfig(level=logging.INFO)
    updater = Updater(TOKEN, use_context=True)
    job_queue = updater.job_queue

    # Kirim pertama kali setelah 5 detik, lalu setiap 3 jam
    job_queue.run_repeating(kirim_pesan, interval=INTERVAL_SECONDS, first=5)

    print("🤖 Bot autopost aktif. Akan kirim ke channel setiap 3 jam.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
