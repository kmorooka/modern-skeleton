# modern-skeleton プログラム説明

* modern-skeleton は、flaskアプリをコンテナ化、AppRunnerによるSaaS化、までをご覧いただくためのサンプルコードです。
* 当初、入力データを元にMatplotlibでグラフ描画をするプログラムでしたが、全体の流れを追いやすくするためにグラフ描画を削除し、コンテナ化、SaaS化の過程を学べるようにしています。（なので一部変数名、機能が残っている部分もあります。）

## 動作確認環境

1. Mac BigSur 11.6.2
2. Python version3.8.8 (Anacondaパッケージをインストール）
3. 各種pythonライブラリー(pip v3で導入）
  - 基本的にAnacondaでなくてもpython3と関連ライブラリー、日本語フォントがあれば稼働するはず。
4. docker
  - docker desktop: 4.5.0
  - Engine: 20.10.12

## 利用方法
利用方法には３つの方法があります。以下、それぞれの方法についてこの後説明しています。
1. ソースコードをもとに起動（手元のPCなどで）
2. Dockerイメージから起動（Docker環境で）
3. SaaS形式で利用（ブラウザからサイトへアクセスして）

### ソースをもとに実行する

#### ソースを取得する

`$ git clone (リポジトリURL)` にてクローンするか、または、GitHubの [Code]-[Download ZIP] から取得して、
`$ unzip apa-gui.zip` 等で展開してください。

#### 実行環境構築

1. pythonバージョン3 の確認  
  個別にPython v3を導入、またはAnacondaのようなAll-Inパッケージを導入してPython v3が利用できるようにしておきます。
2. 日本語フォントの事前導入（本来不要ですが、参考までに残しています）
  matplotlibで日本語表示をさせるために日本語フォントを導入設定しておく必要がありました。フォント「IPAexGothic」を使用しているため、予めこれを導入しておきます。Macの場合はフォントをダウンロードし、アプリであるFont Book を使ってフォントファイルを読込んで利用可能にしてください。
  フォントを変更したい場合、apa-config.py のパラメータ JP_FONT でフォント名を指定します。
  フォントのダウンロード元は、以下のサイトです。この中にMac向けのインストール手順も記載されています。
  https://moji.or.jp/ipafont/ipafontdownload/
3. pythonライブラリーのインストール  
  requirements.txt では、導入するライブラリーをリストしています。
```sh
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

#### 起動

以下のコマンドを実行し、表示されるURLにアクセスしてください。

```sh
$ python3 app.py
```

### Dockerイメージから起動する

Dockerを実行可能な環境にて、以下のコマンドを実行してください。

```sh
$ cd ./apa-gui
$ docker build . -t apa-gui
$ docker run -it --rm -p 5000:5000 apa-gui
```

### AWS App Runner で起動する

付属の `apprunner.yaml` を利用し、GitHubソースからデプロイできます。
