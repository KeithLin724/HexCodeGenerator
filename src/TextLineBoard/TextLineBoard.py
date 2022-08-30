from .CustomText import CustomText
from .TextLineNumbers import TextLineNumbers
from ttkbootstrap import Frame, Scrollbar


class TextLineBoard(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = Scrollbar(self, orient="vertical", command=self.text.yview)

        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))

        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        # self.text.insert("end", "one\ntwo\nthree\n")
        # self.text.insert("end", "four\n", ("bigfont", ))
        # self.text.insert("end", "five\n")

    def _on_change(self, event):
        self.linenumbers.redraw()
