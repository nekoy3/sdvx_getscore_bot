from bot import MyClient
from webmanage import MyWebmanageController

#ChatGPTさま様からの助言

#MyConfigのメンバ変数・関数を大量に使う、MyClientクラスのインスタンスを何度も使う
#のであれば、MyClientクラスに対して継承を使う方が良い

#あまりMyConfigクラスのメンバー変数・関数を使わない、MyClientクラスのインスタンスを一度しか生成しない
#のであればMyClientクラスのコンストラクタでインスタンスを生成して保持するほうが良い
def main():
    webmanageController = MyWebmanageController()
    #configはMyClientに継承する
    client = MyClient(webmanageController)
    #オーバーライドされたメソッド(clienbtでtokenを保持しているため)
    client.run() 

if __name__ == '__main__':
    main()