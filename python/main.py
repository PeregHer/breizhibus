import tkinter
from interface import Interface


def main():
    window = tkinter.Tk()
    Interface(window).menu_lignes()
    window.mainloop()

main()