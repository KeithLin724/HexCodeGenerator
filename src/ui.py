from ttkbootstrap import *
from TextLineBoard import TextLineBoard


class ui:
    BNT_WIDTH_SHORT, BNT_WIDTH = 3, 5
    SEGMENT_BOOTSTYLE_THEME = "danger-toolbutton"
    MODE_STR = ("Left to Right", "Right to Left")

    def __settingSegmentFrame(self) -> None:  # in right
        """_summary_
            about the GUI settings
        """
        mainNumberFrame = Labelframe(self.__leftFrame,
                                     text="SevenSegment",
                                     width=400,
                                     height=300,
                                     bootstyle='info')
        "NOTE:--upper Button--"
        upperButton = Checkbutton(mainNumberFrame,
                                  width=ui.BNT_WIDTH,
                                  bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)

        upperButton.grid(column=1, row=0)
        self.segmentBntDict.update({1: upperButton})
        "NOTE:--upper left right Button--"
        upperLeftBnt = Checkbutton(mainNumberFrame,
                                   width=ui.BNT_WIDTH_SHORT,
                                   bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)

        upperLeftBnt.grid(column=0, row=1)
        self.segmentBntDict.update({6: upperLeftBnt})

        upperRightBnt = Checkbutton(mainNumberFrame,
                                    width=ui.BNT_WIDTH_SHORT,
                                    bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)
        upperRightBnt.grid(column=2, row=1)
        self.segmentBntDict.update({2: upperRightBnt})
        "--------------------------------"
        "NOTE:--mid Button--"
        midButton = Checkbutton(mainNumberFrame,
                                width=ui.BNT_WIDTH,
                                bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)
        midButton.grid(column=1, row=2)
        self.segmentBntDict.update({7: midButton})
        "NOTE:--down left right Button--"
        downLeftBnt = Checkbutton(mainNumberFrame,
                                  width=ui.BNT_WIDTH_SHORT,
                                  bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)

        downLeftBnt.grid(column=0, row=3)
        self.segmentBntDict.update({5: downLeftBnt})

        downRightBnt = Checkbutton(mainNumberFrame,
                                   width=ui.BNT_WIDTH_SHORT,
                                   bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)
        downRightBnt.grid(column=2, row=3)
        self.segmentBntDict.update({3: downRightBnt})
        "NOTE:--down end Button--"
        downButton = Checkbutton(mainNumberFrame,
                                 width=ui.BNT_WIDTH,
                                 bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)
        downButton.grid(column=1, row=4)
        self.segmentBntDict.update({4: downButton})

        dpButton = Checkbutton(mainNumberFrame,
                               text="DP",
                               width=ui.BNT_WIDTH_SHORT,
                               bootstyle=ui.SEGMENT_BOOTSTYLE_THEME)
        dpButton.grid(column=2, row=5)
        self.segmentBntDict.update({8: dpButton})
        "--End of Number Frame--"
        mainNumberFrame.pack()

        return

    def __settingLeftFrame(self) -> None:
        preViewFrame = Frame(self.__leftFrame, bootstyle='info')
        preViewLabel = Label(preViewFrame,
                             text='pre-view',
                             bootstyle='inverse-info')
        preViewLabel.pack(side=LEFT)

        self.preViewText = Text(preViewFrame, width=10, height=1)
        self.preViewText.pack(side=RIGHT)

        preViewFrame.pack()

        self.showCharacterBnt = Button(self.__leftFrame, text="Show Character")
        self.showCharacterBnt.pack()
        return

    def __settingSegmentControl(self) -> None:
        """_summary_
            setting the Number Control Frame 
        """

        bottomFrame = Frame(self.__leftFrame)

        self.clearSegmentBnt = Button(bottomFrame, text="Clear", width=8)
        self.clearSegmentBnt.pack(side=LEFT)

        self.addNumberBnt = Button(bottomFrame, text="Add", width=8)
        self.addNumberBnt.pack(side=RIGHT)

        bottomFrame.pack()

        self.changeModeBnt = Checkbutton(self.__leftFrame,
                                         text=ui.MODE_STR[0],
                                         bootstyle="warning-toolbutton")
        self.changeModeBnt.pack()
        return

    def __settingRightFrame(self) -> None:
        '----input Frame----'
        inputHeadEndFrame = LabelFrame(self.__rightFrame,
                                       text='Input',
                                       bootstyle='info')
        inputFrame = Frame(inputHeadEndFrame)
        leftInputFrame = Frame(inputFrame)

        leftAddLabel = Label(leftInputFrame,
                             text='Left Add',
                             bootstyle='inverse-success')
        leftAddLabel.pack(side=LEFT)

        self.leftAddEntry = Entry(leftInputFrame, bootstyle='success')
        self.leftAddEntry.pack(side=RIGHT)

        leftInputFrame.pack(side=LEFT)

        rightInputFrame = Frame(inputFrame)

        rightAddLabel = Label(rightInputFrame,
                              text='Right Add',
                              bootstyle='inverse-success')
        rightAddLabel.pack(side=LEFT)

        self.rightAddEntry = Entry(rightInputFrame, bootstyle='success')
        self.rightAddEntry.pack(side=RIGHT)

        rightInputFrame.pack(side=RIGHT)
        inputFrame.pack()

        self.addInputBnt = Button(inputHeadEndFrame,
                                  text='Add Input',
                                  bootstyle='success')
        self.addInputBnt.pack(side=LEFT)

        self.clearInputBnt = Button(inputHeadEndFrame,
                                    text='Clear Input',
                                    bootstyle='warning')
        self.clearInputBnt.pack(side=RIGHT)

        inputHeadEndFrame.pack()
        '------------------------'
        self.outPutText = TextLineBoard(self.__rightFrame)
        self.outPutText.pack()

        bntFrame = Frame(self.__rightFrame)
        self.clearAllBnt = Button(bntFrame,
                                  text="Clear All",
                                  bootstyle='danger')
        self.clearAllBnt.pack(side=LEFT)

        self.clearTextBoardBnt = Button(bntFrame, text="Clear Text Board")
        self.clearTextBoardBnt.pack(side=RIGHT)
        bntFrame.pack()

        return

    def __settingStyle(self) -> None:
        self.__styleMain.configure('TButton', font=('Arial', 13))
        self.__styleMain.configure('TLabelFrame', font=('Arial', 24))
        return

    def __init__(self):
        super().__init__()
        self.segmentBntDict = {}
        self.textDict = {}
        "---GUI Setting---"

        self.windows = Window(title="Hex Code Generator",
                              themename='superhero')
        self.__styleMain = Style()

        self.__settingStyle()
        "-- Right Frame"
        self.__leftFrame = Frame(self.windows)

        self.__settingLeftFrame()
        self.__settingSegmentFrame()
        self.__settingSegmentControl()

        self.__leftFrame.pack(side=LEFT)
        "--End of Right Frame--"
        "--Left Frame"
        self.__rightFrame = Frame(self.windows)
        self.__settingRightFrame()
        self.__rightFrame.pack(side=RIGHT)
        "-- End of Left Frame--"
        "--- End of GUI ---"
