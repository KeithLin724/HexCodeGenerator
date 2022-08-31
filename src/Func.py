from copy import deepcopy
from ui import ui
from ttkbootstrap.constants import *
from functools import partial
import logging


class Func(ui):
    EMPTY_STR_LIST, STR_LIST = [""] * 7, [chr(97 + i) for i in range(7)]
    DISPLAY_FORMAT = "%(asctime)s %(funcName)s: %(message)s"

    def __link(self) -> None:
        """
            link function with button 
        """
        for k in self.segmentBntDict.keys():
            self.segmentBntDict[k]\
                .config(command=partial(self.__addNumberFunc, k))

        self.showCharacterBnt.configure(command=self.__showCharacterFunc)
        self.clearSegmentBnt.configure(command=self.__clearSegmentFunc)
        self.addNumberBnt.configure(command=self.__addToTotalHexFunc)
        self.clearTextBoardBnt.configure(command=self.__clearTextBoardFunc)
        self.clearAllBnt.configure(command=self.__clearAllFunc)
        self.changeModeBnt.configure(command=self.__changeModeFunc)
        self.clearInputBnt.configure(command=self.__clearInputFunc)
        self.addInputBnt.configure(command=self.__addInputFunc)
        self.invBnt.configure(command=self.__invModeFunc)
        return

    def __init__(self):
        super().__init__()

        self.__listHexCode = []  # original list
        self.__listDisplayHexCode = []  # make some thing and display
        self.__hexCodeBuilder = [0] * 8
        self.__showState = False
        self.__poseMode = False  # False -> True <-
        self.__addInputStr = ('', '')
        self.__invMode = False  # True inv Mode

        logging.basicConfig(level=logging.DEBUG, format=Func.DISPLAY_FORMAT)
        self.__link()
        return

    def run(self) -> None:
        self.windows.mainloop()
        return

    def __addNumberFunc(self, numberID: int) -> None:
        """_summary_
            add a numberID to the HexBuilder
        Args:
            numberID (int): _description_
        """
        invBit = lambda x: int(not bool(x))

        logging.info(f"on click {numberID}")

        self.__hexCodeBuilder[numberID - 1] = invBit(
            self.__hexCodeBuilder[numberID - 1])

        self.__refreshPreView()

        logging.info(
            f"now Build is {self.__hexCodeBuilder } state:{self.segmentBntDict[numberID].instate(['selected'])}"
        )
        return

    def __showCharacterFunc(self) -> None:
        """_summary_
        
            this function is display char in seven segment 
        """

        self.__showState = not self.__showState
        logging.info(f"state {self.__showState}")
        tmpList = Func.STR_LIST if self.__showState else Func.EMPTY_STR_LIST

        for k in self.segmentBntDict.keys():
            if k < 8:
                self.segmentBntDict[k].configure(text=deepcopy(tmpList[k - 1]))
        return

    def __refreshPreView(self) -> None:
        self.preViewText.configure(state='normal')

        self.preViewText.delete(1.0, END)

        tmpInvStr = self.__hexCodeBuilder if not self.__invMode \
                                          else Func.__invList(self.__hexCodeBuilder)

        tmpStr = ''.join(
            map(str, tmpInvStr if not self.__poseMode else tmpInvStr[::-1]))

        self.preViewText.insert(1.0, tmpStr)

        self.preViewText.configure(state='disabled')

        logging.info(f"pre view refresh")
        return

    def __refresh(self) -> None:
        """
            refresh the window
        """
        self.outPutText.text.configure(state='normal')

        self.outPutText.text.delete(1.0, END)
        tmpInvDisplay = self.__listDisplayHexCode if not self.__invMode \
                                                  else [Func.__invList(elm) for elm in self.__listDisplayHexCode]

        tmp = tmpInvDisplay if not self.__poseMode  \
                            else [elm[::-1] for elm in tmpInvDisplay]

        if (self.__addInputStr != ('', '')):
            tmp = [
                f'{self.__addInputStr[0]}{elm}{self.__addInputStr[1]}'
                for elm in tmp
            ]

        self.outPutText.text.insert(1.0, index='\n'.join(tmp))

        self.outPutText.text.configure(state='disabled')
        logging.info('refresh')

        return

    def __clearSegmentFunc(self) -> None:
        """_summary_
        clear the segment button and the builder 
        https://stackoverflow.com/questions/4236910/getting-checkbutton-state
        """
        logging.info(f"clear Segment function")
        self.__hexCodeBuilder = [0] * 8

        for k in self.segmentBntDict.keys():
            self.segmentBntDict[k].state(['!selected'])

        self.__refreshPreView()

        return

    def __addToTotalHexFunc(self) -> None:
        logging.info('Add func')
        tmpStr = ''.join(map(str, self.__hexCodeBuilder))
        self.__listHexCode.append(tmpStr)
        self.__listDisplayHexCode.append(tmpStr)
        self.__refresh()

        return

    def __clearTextBoardFunc(self) -> None:
        """Clear Text Board function"""
        logging.info("clear text board")
        self.__listHexCode.clear()
        self.__listDisplayHexCode.clear()

        self.__refresh()

        return

    def __clearAllFunc(self) -> None:
        logging.info("clear all")
        self.__clearSegmentFunc()
        self.__clearTextBoardFunc()
        self.__clearInputFunc()
        return

    def __changeModeFunc(self) -> None:

        self.__poseMode = not self.__poseMode
        self.changeModeBnt.configure(text=ui.MODE_STR[self.__poseMode])
        logging.info(f"change Mode -> {ui.MODE_STR[self.__poseMode]}")
        self.__refreshPreView()
        self.__refresh()

        return

    def __addInputFunc(self) -> None:
        logging.info('add input function')
        self.__addInputStr = (self.leftAddEntry.get(),
                              self.rightAddEntry.get())

        self.addInputBnt.state(['!selected'])
        self.__refresh()
        return

    def __clearInputFunc(self) -> None:
        logging.info("clear input")
        self.leftAddEntry.delete(0, END)
        self.rightAddEntry.delete(0, END)
        self.__addInputStr = ('', '')

        self.clearInputBnt.state(['!selected'])
        return

    def __invList(lst):

        numList = lambda tmp: [int(not elm) for elm in tmp]

        if type(lst) is list:

            return numList(lst)

        if type(lst) is str:

            return ''.join(map(str, numList(list(map(int, list(lst))))))

    def __invModeFunc(self):

        self.__invMode = not self.__invMode
        logging.info(f"invMode :{self.__invMode}")
        self.__refreshPreView()
        self.__refresh()
        return
