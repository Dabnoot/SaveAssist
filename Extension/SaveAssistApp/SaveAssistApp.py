#!/usr/bin/env python

import sys
import json
import struct
import ctypes  # An included library with Python install. Used for msgbox.
from tkinter import filedialog
from tkinter import *

currentFilePath = ""

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



while True:
	receivedMessage = getMessage()
	if receivedMessage != "":
		#Open a messagebox with the version number:
		ctypes.windll.user32.MessageBoxW(0, "Revision: 15", "SaveAssist", 1)
		
		#Split the message into Save/SaveAs and the URL:
		sArgs = receivedMessage.split("<")
		#Print a message box showing the data received:
		#ctypes.windll.user32.MessageBoxW(0, "Received message: " + receivedMessage, "Your title", 1)
		 # If there is no current path, ask the user for a path.
		if currentFilePath == "" or sArgs[0] == "SaveAs":
			root = Tk()
			
			#Minimize the Tk window:
			root.withdraw()
			#Set 'always be on top' attribute:
			root.attributes("-topmost", True)
			root.filename =  filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
			#Remove 'always on top' attribute:
			root.attributes("-topmost", False)
			currentFilePath = root.filename
#		
#		#Save the file if a path exists:
#		#if currentFilePath != ""
#		#

