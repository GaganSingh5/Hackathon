import threading
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


class Trust(threading.Thread):
    @classmethod
    def Graph(self):
        df = pd.read_csv("trust.csv")
        trustPrecent = df["percent"]
        trustYears = df["year"]

        style.use('ggplot')
        plt.figure(2)
        plt.plot(trustYears, trustPrecent, 'r', label='Facebook', linewidth=1)
        plt.title('Trust Depletion After Cambridge Scandal')
        plt.ylabel('PRECENTAGE OF TRUST OR SECURITY')
        plt.xlabel('YEARS')
        plt.legend()
        plt.grid(True, color='k')
        plt.show()

    def run(self):
        self.Graph()
