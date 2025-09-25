from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "import os BOT_TOKEN = os.environ["BOT_TOKEN"]"  # mantenha as aspas

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Eu sou o CIMIAX.\n\n"
        "Digite ACEITO para confirmar os termos e continuar."
    )

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = (update.message.text or "").strip().lower()
    if "aceito" in txt:
        await update.message.reply_text(
            "✅ Termos aceitos! Vamos descobrir seu perfil.\n"
            "Qual sua experiência com investimentos? (Nunca / Um pouco / Frequente)"
        )
    else:
        await update.message.reply_text("Digite ACEITO para prosseguir 😉")

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

    print("Bot rodando 🚀  (volte ao Telegram e envie /start)")
    application.run_polling()

if __name__ == "__main__":
    main()
