from Func import Func


class App(Func):

    def __init__(self) -> None:
        super().__init__()
        self.run()


if __name__ == '__main__':
    app = App()
