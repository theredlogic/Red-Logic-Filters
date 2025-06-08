from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from redlogic import ADVANCED_WORDS_FILTER 


def contains_bad_word(text: str) -> bool:
    normalized = text.lower()
    return any(word in normalized for word in ADVANCED_WORDS_FILTER)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return

    if contains_bad_word(message.text):
        try:
            await message.reply_text("⚠️ فحش شناسایی شد. لطفاً رعایت کن 🙏")
            await message.delete()
            print(f"پیام حاوی فحش حذف شد: {message.text}")
        except Exception as e:
            print(f"خطا در حذف پیام یا ارسال پاسخ: {e}")

if __name__ == '__main__':
    import os

    TOKEN = ""

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات فعال شد.")
    app.run_polling()
