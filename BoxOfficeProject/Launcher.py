from tkinter import *
from Interface import *

def main():
	window = Tk()
	window.title("Box Office")
	window.geometry("940x600+400+200")
	window.resizable(False, False)
	
	menu = Interface(window, 940, 600)
	menu.Draw()

	window.mainloop()

main()