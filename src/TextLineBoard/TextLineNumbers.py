from ttkbootstrap import Canvas


class TextLineNumbers(Canvas):

    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.textWidget = None

    def attach(self, text_widget):
        self.textWidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textWidget.index("@0,0")
        while True:
            dLine = self.textWidget.dlineinfo(i)
            if dLine is None:
                break
            y = dLine[1]
            lineNumber = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=lineNumber, fill='yellow')
            i = self.textWidget.index("%s+1line" % i)
