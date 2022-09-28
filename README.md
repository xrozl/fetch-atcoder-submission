## このプログラムについて
このプログラムはAtCoder上にアップロードされたACかつ最新のコードを全て取得するものです。
取得はAtCoderのユーザーIDを指定して行います。

### 使い方
```
git clone https://github.com/yu7400ki/fetch-atcoder-submission.git
cd fetch-atcoder-submission
pip install -r requirements.txt
python ./src/main.py

Please input your atcoder id:{your id}
```
もしpoetryがインストールされていれば```pip```の代わりに以下が使えます。
```
poetry install --without dev
```

取得したコードは```./dist```に保存されます。


## 開発環境

### 前提
```
python 3.10
poetry 1.2
git
```

### セットアップ
```
git init
poetry shell
poetry install
pre-commit install
```

### docker
```
docker compose up -d --build
```
