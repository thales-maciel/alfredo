import os

from alfredo.core import Alfredo

def main():
    # TODO add option to run with logs
    os.environ["KIVY_NO_CONSOLELOG"] = "1"

    from alfredo.gui.gui import MainApp

    MainApp().run()


if __name__ == "__main__":
    exit(main())
