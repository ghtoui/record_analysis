from flask import Flask, request, render_template
import numpy
import soundfile as sf
from web_app.freq_analysis import FreqAnalysisClass
from web_app.visual_data import VisualDataClass
from web_app import app

fa = FreqAnalysisClass()
vd = VisualDataClass()

@app.route('/upload', methods = ['POST'])
def upload_file():
    FILE_NAME = 'record_file'

    # POSTで送られてきた音楽ファイルを取り出す
    record_file = request.files[FILE_NAME]
    # 音楽ファイルを読み込む
    record_data, samplerate = sf.read(FILE_NAME)
    # 高速フーリエ変換
    freq_data = fa.fft_freq_data(record_file)

    # 周波数データとレコードデータをHTML形式の画像データに
    original_plot_data = vd.data_plot(record_data)
    freq_plot_data = vd.data_plot(freq_data)

    # ここをどこのHTMLファイルに送るか迷う
    return render_template('/upload.html', plot_original_img = original_plot_data,
                           plot_freq_img = freq_plot_data)

