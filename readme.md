# 環境構築

## windows


## mac

0.  事前準備

* homebrewがインストールされていること

1. pythonとpipenvインストール 

    ```
   $ brew install python
    ```
    ```
   $ brew install pipenv
    ```
   
   #インストール確認

    ```
   $ python --version
   ```
    ```
   $ pipenv --version
   ```
   
2. プロジェクトに移動

    ```
    $ cd <プロジェクトのパス>
    ```


3. 仮想環境に依存パッケージのインストール

    ```
    $ pipenv install
    ```

4. 仮想環境のシェルに入る
    ```
    $ pipenv shell
    ```

6. 「実行方法」へ

# 実行方法

1. srcディレクトにエビデンスとなる画像を全て格納する

2. エディタでmain.pyを開き変数名「saveFileName」の値を作成したいエクセルブック名に変更する

