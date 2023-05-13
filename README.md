# 🤖InstaBot_Telegram


## 🧰 Tecnologias utilizadas

-   Python 3.8 ou superior
-   Instaloader 4.9
-   Python-Telegram-Bot 13.14
-   Screen
-   Acesso à conta do Instagram (para obter as credenciais de login)
-   Google Chrome (recomendado para fazer login no Instagram em uma VPS)
-   VNC (recomendado para acesso remoto à VPS)

## 🚀 Instruções de instalação e uso do código

**Passo 1: Instalação do Python 3.8**

Verifique se o Python 3.8 já está instalado em seu sistema. Se não estiver, você pode instalá-lo seguindo as instruções do site oficial do Python.

**Passo 2: Instalação do Instaloader e Python-Telegram-Bot**

Para instalar o Instaloader e Python-Telegram-Bot, abra o terminal e execute os seguintes comandos:

    pip install -r requirements.txt

 - **Passo 3: Instalação do Screen**

No Ubuntu, você pode instalar o Screen executando o seguinte comando:

    sudo apt-get install screen

 - **Passo 4: Obtenção das credenciais de login do Instagram**

Para obter as credenciais de login do Instagram, você precisa fazer login manualmente na sua conta do Instagram. Depois de fazer login, abra o código e substitua "USERNAME" e "PASSWORD" por suas credenciais de login.

 - **Passo 5: Executando o código em uma VPS**

Se você estiver executando o código em uma VPS, é recomendável que você instale o VNC para facilitar o processo de login no Instagram. Para instalar o VNC, siga as instruções do link fornecido no link :
[# Como-instalar-e-configurar-o VNC no Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04-pt).

Depois de instalar o VNC, inicie o servidor VNC e faça login na VPS usando o cliente VNC.

Instale o Google Chrome usando as instruções fornecidas no link:
 [# Como instalar o Google Chrome no Linux Ubuntu](https://www.webmundi.com/sistema-operacional/linux/como-instalar-o-google-chrome-no-linux-ubuntu/).

Abra o Google Chrome e faça login na sua conta do Instagram.

Depois de fazer login, execute o código em segundo plano usando o Screen. Para fazer isso, execute o seguinte comando:

    screen -S bot python3 nome_do_arquivo.py

Substitua "nome_do_arquivo.py" pelo nome do arquivo que contém o código.

 - **Passo 6: Uso do bot**

Para usar o bot, envie uma mensagem para o bot no Telegram com o link da postagem do Instagram que você deseja baixar. O bot baixará as mídias do post e enviará as mídias para você. Se ocorrer um erro durante o processo de download, o bot enviará uma mensagem de erro para você.

## 📝 Comandos disponíveis:

-   /start - Inicia o bot e exibe uma mensagem de boas-vindas
-   /help - Exibe uma mensagem de ajuda
