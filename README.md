# record_analysis

## ブランチを切って開発するのを忘れずに(mainで開発しない)

## templates

htmlファイルはここ </br>
layout.htmlを使ってテンプレート作成すると楽

## static

javascriptとcss, 画像ファイルはここ </br>
録音した音声ファイルも後々ここに保存するつもり

## 環境構築

python -m venv .env </br>
.envは任意の名前

pip install -r requirements.txtで同じ環境を構築できる </br>
これ＋αでpip installしたものがあれば、**pip freeze > requirment.txt**で更新してほしい </br>

## 目標

1. web上で録音
2. 録音データをそのままグラフで可視化
3. フーリエ変換で周波数可視化
4. カットしたい周波数を入力して、カットした後の周波数信号を可視化
5. ピアノ、ギター、声を同時に入力して、ピアノだけ録音からカットして、録音データ保存などをしてみたい

他にも何かあれば
