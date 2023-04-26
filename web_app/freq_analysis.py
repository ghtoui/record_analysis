import numpy as np

# 周波数変換、フーリエ変換、フィルタリングをするクラス
class FreqAnalysisClass:
    def __init__ (self):

        self.med_fil_list = []
        # RCローパスフィルタ計算結果を格納する
        self.low_rc_result = 0

    # 高速フーリエ変換
    # 引数
    # data: フーリエ変換するデータ
    # 返り値
    # freq: 周波数変換したデータ
    def fft_freq_data(self, data):
        # 変換のためにデータを1次元に変換する
        data = np.array(data).flatten()
        # 周波数信号に変換
        freq = np.fft.fft(data)
        # 正規化と交流成分2倍
        freq = freq / (data.size / 2)
        freq[0] = freq[0] / 2

        return freq

    # 高速逆フーリエ変換
    # カットオフ周波数は、fft_freq_dataメソッドで周波数を確認して設定する
    # 引数
    # cf: カットオフ周波数
    # sf: サンプリング周期
    # 返り値
    # inv_freq_data: 逆フーリエ変換で生成したデータ
    # freq_data: inv_freq_dataの周波数データ
    def fft_inv_freq_data(self, data, cf, sp):
        # サンプリング周波数
        freq = np.linspace(0, 1.0 / sp, data.size)
        data = np.array(data).flatten()
        n = data.size
        freq_data = self.fft_freq_data(data)
        # ローパスフィルタ処理 (cfを超える帯域の周波数信号を0にする)
        freq_data[(freq > cf)] = 0
        # 時間信号に戻す
        inv_freq_data = np.fft.ifft(freq_data)
        inv_freq_data = np.real(inv_freq_data * n)

        return inv_freq_data, freq_data

    # RCローパスフィルタ
    def rc_low_filter(self, data):
        CUTOFF = 0.7
        data = data[-1]
        self.low_rc_result = CUTOFF*data + (1 - CUTOFF)*self.low_rc_result

        return self.low_rc_result

