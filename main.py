import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# Ganti dengan token bot Anda
my_bot_token = "BOT_TOKEN" #ambil bot token dari @BotDFather

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Ganti dengan ID channel dan username Instagram kalian
CHANNEL_ID = "@" #isi dengan nama ch kalian
INSTAGRAM_USERNAME = "@"  # Hapus @ di sini untuk membuat tautan

# Handler untuk perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.message.from_user.first_name  # Ambil nama depan pengguna
    keyboard = [
        [InlineKeyboardButton("sfs & follow ig", callback_data='subscribe_channel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Selamat datang, {user_first_name}! Gunakan tombol di bawah ini:", reply_markup=reply_markup)

# Handler untuk callback button
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    if query.data == 'subscribe_channel':
        await query.edit_message_text(
            text=f"Sfs? disini kak:\n{CHANNEL_ID}\n\n"
                 f"Follow ig? disini juga kak: https://instagram.com/{INSTAGRAM_USERNAME}",
            disable_web_page_preview=False  # Ubah ini menjadi True jika ingin menonaktifkan preview
        )

# Fungsi utama untuk menjalankan bot
def main() -> None:
    application = Application.builder().token(my_bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
