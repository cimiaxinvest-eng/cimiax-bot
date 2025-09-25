import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Pega o token do BotFather que você configurou no Render
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Início do bot (com termos de uso)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Eu sou o CIMIAX.\n\n"
        "Antes de começarmos, você precisa aceitar os Termos de Uso:\n"
        "➡️ A responsabilidade pelas decisões de investimento é **do cliente**.\n"
        "➡️ O CIMIAX envia alertas baseados nos gatilhos combinados, mas não garante lucros.\n"
        "➡️ Ao digitar **ACEITO**, você confirma que entendeu e concorda.\n\n"
        "Digite **ACEITO** para continuar."
    )

# Fluxo inicial após aceitar os termos
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = (update.message.text or "").strip().lower()

    if "aceito" in txt:
        await update.message.reply_text(
            "✅ Termos aceitos! Agora vamos descobrir seu perfil de investidor.\n\n"
            "1️⃣ Qual a sua experiência com investimentos?\n"
            "- Nunca investi\n"
            "- Já investi um pouco\n"
            "- Invisto com frequência"
        )
    else:
        await update.message.reply_text("❌ Você precisa digitar **ACEITO** para prosseguir.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

    print("Bot rodando 🚀 (envie /start no Telegram)")
    app.run_polling()

if __name__ == "__main__":
    main()
