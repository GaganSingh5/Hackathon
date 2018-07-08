import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import threading

class Usage(threading.Thread):
    @classmethod
    def Graph(self):
        d1 = pd.read_csv("facebook.csv")
        d2 = pd.read_csv("insta.csv")
        d3 = pd.read_csv("twitter.csv")
        Fbyear = d1["year"]
        fbServral = d1["servral"]
        Instayear = d2["year"]
        instaServral = d2["servral"]
        Twitteryear = d3["year"]
        twitterServral = d3["servral"]
        style.use('ggplot')
        plt.figure(1)
        plt.plot(Fbyear, fbServral, 'r', label='Facebook', linewidth=1)
        plt.plot(Instayear, instaServral, 'c', label='Instagram', linewidth=1)
        plt.plot(Twitteryear, twitterServral, 'y', label='Twitter', linewidth=1)
        plt.title('USAGE')
        plt.ylabel('PEOPLE(%)')
        plt.xlabel('YEARS')
        plt.legend()
        plt.grid(True, color='k')
        plt.show()

    def run(self):
        self.Graph()


