import os, shutil
import random
import telegram
from telegram.ext import Updater, CommandHandler
import instaloader

# Cria uma instância do Instaloader
loader = instaloader.Instaloader()

# Entre com seu nome de usuário e senha
loader.login('USERNAME', 'PASSWORD')

# Define o token do bot do Telegram
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Cria uma instância do bot do Telegram
bot = telegram.Bot(token=TOKEN)

# Define a função de callback para o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Envie o link da postagem do Instagram que deseja baixar.")

# Define a função de callback para o comando /help
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Envie o link da postagem do Instagram que deseja baixar.")

# Define a função de callback para receber mensagens
def receive_message(update, context):
    # Obtém a mensagem enviada pelo usuário
    message = update.message.text
    
    # Verifica se a mensagem é uma URL do Instagram
    if "instagram.com" in message:
        try:
            # Envia uma mensagem de que o download está sendo feito
            context.bot.send_message(chat_id=update.effective_chat.id, text="O download está sendo feito, aguarde por favor...")

            # Obtém o post a partir da URL
            post = instaloader.Post.from_shortcode(loader.context, message.split("/")[-2])
            
            # Gera 5 números aleatórios
            random_nums = ''.join([str(random.randint(0, 9)) for _ in range(5)])

            # Concatena os números aleatórios com o nome do proprietário do post
            download_folder = post.owner_username + "_" + random_nums

            # Baixa as mídias do post
            loader.download_post(post, target=download_folder)

            # Envia as mídias para o usuário
            for filename in os.listdir(download_folder):
                if filename.endswith('.jpg') or filename.endswith('.mp4'):
                    with open(download_folder + "/" + filename, "rb") as file:
                        context.bot.send_document(chat_id=update.effective_chat.id, document=file)

            # Apaga o cache do download
            shutil.rmtree(download_folder)
            
            context.bot.send_message(chat_id=update.effective_chat.id, text="Download concluído!")
        except Exception as e:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Erro: " + str(e))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Por favor, envie uma URL do Instagram.")
    
# Cria uma instância do Updater
updater = Updater(token=TOKEN, use_context=True)

# Obtém o objeto de despacho de comandos do Updater
dispatcher = updater.dispatcher

# Adiciona o tratador de comandos /start
dispatcher.add_handler(CommandHandler("start", start))

# Adiciona o tratador de comandos /help
dispatcher.add_handler(CommandHandler("help", help))

# Adiciona o tratador de mensagens
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, receive_message))

# Inicia o bot
updater.start_polling()

# Espera o bot ser encerrado
updater.idle()
