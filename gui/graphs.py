import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.localization import _
import matplotlib.font_manager as fm

class NutritionGraphFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 日本語対応フォントの設定
        self.jpfont = fm.FontProperties(fname="C:/Windows/Fonts/meiryo.ttc")
        self.figure.suptitle(_('Nutrition Graph'), fontproperties=self.jpfont)

    def update_graph(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        nutrients = list(data.keys())
        values = list(data.values())
        bars = ax.bar(range(len(nutrients)), values)
        
        ax.set_ylabel(_('Grams'), fontproperties=self.jpfont)
        ax.set_title(_('Daily Nutrient Intake'), fontproperties=self.jpfont)
        ax.set_xticks(range(len(nutrients)))
        ax.set_xticklabels(nutrients, fontproperties=self.jpfont)
        
        # バーの上に値を表示
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom')
        
        self.canvas.draw()