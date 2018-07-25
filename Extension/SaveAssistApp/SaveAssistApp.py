#!/usr/bin/env python

import sys
import json
import struct
import ctypes  # An included library with Python install. Used for msgbox.
from tkinter import filedialog
from tkinter import *
import urllib.request #Use to download and save a file.
import os #For listing files in a directory

gsCurrentFilePath = ""

# Read a message from stdin and decode it.
def getMessage():
	rawLength = sys.stdin.buffer.read(4)
	if len(rawLength) == 0:
		sys.exit(0)
	messageLength = struct.unpack('@I', rawLength)[0]
	message = sys.stdin.buffer.read(messageLength).decode('utf-8')
	return json.loads(message)

# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
	encodedContent = json.dumps(messageContent).encode('utf-8')
	encodedLength = struct.pack('@I', len(encodedContent))
	return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
	sys.stdout.buffer.write(encodedMessage['length'])
	sys.stdout.buffer.write(encodedMessage['content'])
	sys.stdout.buffer.flush()

#root = Tk()
#root.withdraw()
#root.lift()
#root.attributes("-topmost", True)
#root.attributes("-topmost", False)
#root.filename =  filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
#currentFilePath = root.filename

#sLocation = "https://sgcdn.startech.com/005329/media/products/main/RK2620WALHM.main.jpg"
#iDotPosition = sLocation.rfind('.')
#iLength = len(sLocation) - iDotPosition
#sFileType = sLocation[iDotPosition + 1:len(sLocation)]
#ctypes.windll.user32.MessageBoxW(0,"FileType: " + sFileType, "SaveAssist", 1)

#iFileNumber = 1
#listOfEntries = os.scandir("C:\Chapman")
#for entry in listOfEntries:
#	# print all entries that are files
#	if entry.is_file():
#		sFName = entry.name
#		iDotPosition = sFName.rfind('.')
#		sFName = sFName[0:iDotPosition]
#		if sFName.isnumeric():
#			if int(sFName) > iFileNumber:
#				iFileNumber = int(sFName)
#sFName = '{0:04d}'.format(iFileNumber)
#print(sFName)

bDebug = True

while True:
	receivedMessage = getMessage()
	if receivedMessage != "":
		#Open a messagebox with the version number:
		if bDebug:
			ctypes.windll.user32.MessageBoxW(0, "Revision: 21", "SaveAssist", 1)
		
		#Split the message into Save/SaveAs and the URL:
		sArgs = receivedMessage.split("<")
		#Print a message box showing the data received:
		#ctypes.windll.user32.MessageBoxW(0, "Received message: " + receivedMessage, "Your title", 1)
		 # If there is no current path, ask the user for a path.
		if gsCurrentFilePath == "" or sArgs[0] == "SaveAs":
			#Declare an instance of the Tk system
			#  used to display the folder selector dialog.
			root = Tk()
			
			#Minimize the Tk window:
			root.withdraw()
			#Set 'always be on top' attribute:
			root.attributes("-topmost", True)
			root.filename =  filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
			#Remove 'always on top' attribute:
			root.attributes("-topmost", False)
			gsCurrentFilePath = root.filename
		
		#Reset the file number:
		iFileNumber = 1
		
		#Save the file if a path exists:
		if gsCurrentFilePath != "":
			#Get the file number for use in the file name:
			listOfEntries = os.scandir(gsCurrentFilePath)
			for entry in listOfEntries:
				# print all entries that are files
				if entry.is_file():
					sFName = entry.name
					iDotPosition = sFName.rfind('.')
					sFName = sFName[0:iDotPosition]
					if sFName.isnumeric():
						if int(sFName) >= iFileNumber:
							iFileNumber = int(sFName) + 1
			sFName = '{0:05d}'.format(iFileNumber)
			
			#Get the file type:
			sLocation = sArgs[1]
			iDotPosition = sLocation.rfind('.')
			sFileType = sLocation[iDotPosition + 1:len(sLocation)]
			
			#Form the file location and file name:
			sFileNamePath = gsCurrentFilePath + "/" + sFName + "." + sFileType
			if bDebug:
				ctypes.windll.user32.MessageBoxW(0,"File name and save location: " + sFileNamePath, "SaveAssist", 1)
			urllib.request.urlretrieve(sArgs[1], sFileNamePath)
			if bDebug:
				ctypes.windll.user32.MessageBoxW(0,"File save attempt executed. " + sFileNamePath, "SaveAssist", 1)
			
#		
#		

