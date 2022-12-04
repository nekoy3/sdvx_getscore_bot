# coding: utf-8

# configparserモジュールとosモジュールをインポート
import configparser
import os
import getpass

class MyConfig:
    # config.iniファイルが存在するかどうかを確認する
    def __init__(self):
        # configparserオブジェクトを作成
        self.config = configparser.ConfigParser(comment_prefixes='#', allow_no_value=True)

        # config.iniファイルが存在するかどうかを確認
        if not os.path.exists('config.ini'):
            # config.iniファイルが無い場合はconfig.iniファイルを生成
            self.create_config()
            raise Exception("config created.")

        self.read_config()

    # config.iniファイルを生成する
    def create_config(self):
        # パスワードを暗号化して記述
        #この時ターミナルにぽすわーどを入力する必要があり
        import base64
        password = base64.b64encode(getpass.getpass(prompt='Enter your konami e-mail password: ').encode('utf-8')).decode('utf-8')
        self.config['USER'] = {
            'e-mail': 'example@example.com',
            'password': password
            }
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    # config.iniファイルから設定を読み込む
    def read_config(self):
        self.config.read('config.ini')
    
    def get_user(self):
        self.e_mail = self.config['USER']['e-mail']
        # config.iniファイルからpasswordの値を取得
        # パスワードは暗号化されているため、復号する必要がある
        import base64
        self.password = base64.b64decode(self.config['USER']['password'].encode('utf-8')).decode('utf-8')

if __name__ == '__main__':
    mc = MyConfig()
    mc.get_user()
    print(mc.password)