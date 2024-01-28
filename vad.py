import tkinter as tk
from playsound import playsound


class VeteAlDiablo(tk.Tk):
    def __init__(self, **kwargs):
        super(VeteAlDiablo, self).__init__(**kwargs)

        icx='''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAoUlEQVR4nM2SsRUCIRBEh3vGk
        EEDVwEUZQV3RWAFFoUV2ABmWIBjJA85ATXRSXfmP2ZZ4K9EciG59GZa2mMzrKWllpY1pJ5tIKWhhrRmD
        8iuVcco50nCKOd7tUX5ipEZAGIKq1FuvlxPewCYMkmIQ0xh/ST8BPhWGfBOBaOcjymcy1+YeuFXlWpIW
        eFWh41y82gvWb1jGR5SaWwZhqf8M90BHhCZEDtYfCgAAAAASUVORK5CYII='''

        self.geometry('250x250')
        self.cv = tk.Canvas(self, bg='black', highlightthickness=0)
        self.cv.pack(fill='both', expand=1)
        self.bg = tk.PhotoImage(file='bn_240.png')
        self.fondo = self.cv.create_image(5,5,image=self.bg, anchor='nw')

        # self.cv.tag_bind('ic', '<ButtonPress-1>', self.callate)
        self.i60 = tk.PhotoImage(file='bw60.png')
        self.btnw = tk.PhotoImage(file='bw65.png')
        self.cv.create_image(87,92, image=self.i60, tags='ic')
        self.cv.tag_bind('ic', '<ButtonPress-1>', lambda e:self.play(e, 'callate'))
        self.cv.create_image(85,90,image=self.btnw, tags='callate')
        self.cv.tag_bind('callate', '<Enter>', lambda e:self._oculta('callate'))

        self.cv.create_image(167,93, image=self.i60, tags='ip')
        self.cv.tag_bind('ip', '<ButtonPress-1>', lambda e:self.play(e, 'idiota'))
        self.cv.create_image(165,90,image=self.btnw, tags='idiota')
        self.cv.tag_bind('idiota', '<Enter>', lambda e: self._oculta('idiota'))

        self.cv.create_image(127,172, image=self.i60, tags='iv')
        self.cv.tag_bind('iv', '<ButtonPress-1>', lambda e:self.play(e, 'vete_al_diablo'))
        self.cv.create_image(125,170,image=self.btnw, tags='vete_al_diablo')
        self.cv.tag_bind('vete_al_diablo', '<Enter>', lambda e: self._oculta('vete_al_diablo'))

        self.icox = tk.PhotoImage(data=icx)
        self.cv.create_image(180,40,image=self.icox, tags='cerrarx')
        self.cv.tag_bind('cerrarx', '<ButtonPress-1>', lambda e:self.quit())

        self.cv2 = tk.Canvas(self, bg='#202020', width=58, height=25, highlightthickness=0)
        self.cv2.place(x=30, y=130)
        self.cv2.bind('<B1-Motion>', self.mover_ventana)
        self.cv2.create_text(28,15,fill='gray', text='MOVER', font=('Arial', 10, 'bold'))
        self.overrideredirect(True)
        self.attributes('-transparentcolor', 'black')
        self.attributes('-topmost', True)

    def play(self, e, tag):
        playsound(f'{tag}.mp3')
        self.hm(tag)
        self._oculta(tag)

    def _muestra(self, tag):
        self.cv.itemconfig(tag, state='normal')
        if hasattr(self, '_'):
            self.cv.after_cancel(self._)

    def hm(self, tag):
        self.cv.itemconfig(tag, state='hidden')   
        self._ = self.cv.after(100, self._muestra, (tag,))

    def _oculta(self, tag):
        self.cv.itemconfig(tag, state='hidden')

    def mover_ventana(self, e):
        self.geometry(f"+{e.x_root}+{e.y_root}")
        

if __name__=="__main__":
    app = VeteAlDiablo()
    app.mainloop()