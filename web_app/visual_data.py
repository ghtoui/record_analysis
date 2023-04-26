import matplotlib.pyplot as plt
from io import BytesIO
import base64

class VisualDataClass:
    def __init__(self):
        pass

    # dataを引数で与えたら、HTMLで表示できる形式でプロットして、返却
    def data_plot(self, data):
        self.__init__()
        fig, ax = plt.subplots()
        ax.plot(range(len(data)), data, marker = '.',
                markersize = 8, label = "record_data")
        # x軸を45度回転させて、重ならず見切れないように
        plt.xticks(rotation = 45)
        fig.subplots_adjust(bottom = 0.2)
        plt.legend()

        # グラフをバイト列に変換してBase64でエンコード
        buffer = BytesIO()
        fig.savefig(buffer, format = "png")
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode()

        return image_data
