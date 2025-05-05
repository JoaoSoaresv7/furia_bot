import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


BOT_TOKEN = "7829310509:AAFVqrdd0kwc7Do-Uin8EWgNd9FoEp9vYnc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("📰 Últimas Notícias", callback_data="noticias")],
        [InlineKeyboardButton("📅 Próximas Partidas", callback_data="partidas")],
        [InlineKeyboardButton("📊 Estatísticas de Jogadores", callback_data="estatisticas")],
        [InlineKeyboardButton("🛍️ Loja Oficial", callback_data="loja")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Bem-vindo ao Bot furioso CS:GO!\nEscolha uma opção abaixo:",
        reply_markup=reply_markup,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "noticias":
        await query.edit_message_text("📰 Últimas Notícias:\n- FURIA, MIBR, ODDIK e paiN conhecem adversários da estreia na PGL Astana 2025.\n- FURIA apresenta ex-Falcons como novo auxiliar técnico.")
    elif data == "partidas":
        await query.edit_message_text("📅 Próximas Partidas:\n- FURIA vs THE MONGOLZ - 10/05/2025\n")
    elif data == "estatisticas":
        await query.edit_message_text("📊 Estatísticas:\n- KSCERATO: 1.26 K/D\n- FalleN: 1.01 K/D")
    elif data == "loja":
        await query.edit_message_text("🛍️ Acesse nossa loja oficial: https://loja.furia.gg")


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()

if __name__ == "__main__":
    main()
