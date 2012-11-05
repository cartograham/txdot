from Tkinter import *
import tkMessageBox
import os

def generateMaps():
	global MXDValue
	global gridValue
	
	def checkValue(val):
		
		if not os.path.exists(val):
			tkMessageBox.showerror("Error", "\"%s\" is not valid" % val)
			validInput = False
		else:
			tkMessageBox.showinfo("OK", "\"%s\" is valid" % val)
			validInput = True
		return validInput

	validMXD = checkValue(MXDValue.get().strip())
	validGrid = checkValue(gridValue.get().strip())
	
	if validMXD and validGrid:
		tkMessageBox.showerror("Error:", "\"%s\" is not valid" % val)
	
	
##mxdLocation = arcpy.GetParameterAsText(0)
##grid = arcpy.GetParameterAsText(1)
##defQ = arcpy.GetParameterAsText(2)
##outputDirectory = arcpy.GetParameterAsText(3)
##mapType = arcpy.GetParameterAsText(4)

if __name__ == "__main__":

	interface = Tk()
	interface.title("Create FC PDF Maps")
	interface["padx"] = 40
	interface["pady"] = 20       

	mxdFrame = Frame(interface)
	mxdFrameLabel = Label(mxdFrame)
	mxdFrameLabel["text"] = "MXD:"
	mxdFrameLabel.pack(side=LEFT)
	MXDValue = Entry(mxdFrame)
	MXDValue["width"] = 50
	MXDValue.pack(side=LEFT)
	mxdFrame.pack()

	gridFrame = Frame(interface)
	gridFrameLabel = Label(gridFrame)
	gridFrameLabel["text"] = "Grid:"
	gridFrameLabel.pack(side=LEFT)
	gridValue = Entry(gridFrame)
	gridValue["width"] = 50
	gridValue.pack(side=LEFT)
	gridFrame.pack()
	
	button = Button(interface, text="Generate PDF Maps", command=generateMaps)
	button.pack()
	interface.mainloop()
