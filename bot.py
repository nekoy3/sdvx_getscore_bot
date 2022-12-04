# coding: utf-8
import discord 
from config import MyConfig

class MyClient(discord.Client, MyConfig):
    def __init__(self, webmanageController):
        #intents設定
        intents = discord.Intents.all()
        super(discord.Client, self).__init__(intents=intents)

        #configの用意、読み込み、存在しなければファイルを生成してプログラムを停止
        super(MyConfig, self).__init__()

        #webmanageControllerを保持
        self.webmanageController = webmanageController
    
    #runメソッドをオーバーライドするメソッド
    def run(self):
        self.run(self.token)

    #ボットをセットアップするdiscord.Clientが持つ空のメソッド、オーバーライドすることでログイン時にon_ready()より精密に実行する
    async def setup_hook(self):
        self.channel = self.create_dm(self.get_user(self.user_id))
        self.channel.send(content="起動しました。")

    async def on_message(self, msg):
        if msg.type == discord.MessageType.default and msg.content.startswith('#'):
            # #hello のように実行してコマンドとする。
            cmd = msg.content[1:]
            if cmd == 'help':
                await msg.reply("ヘルプを参照・・・")
            elif cmd == 'login':
                await msg.reply("login...")
            else:
                await msg.reply("該当するコマンドが存在しません。#helpで参照してください。")
