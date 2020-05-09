# Moves temporary dumped files to dump, and documents to temporary dump
# Similarly for pictures

import os
import shutil
from os import path
from os.path import isfile, join


BGIS_Drive = r'C:\Users\pgeras\OneDrive - BGIS'

Folders = [
	{
		'Id': "Documents",
		'Initial': BGIS_Drive + r'\_Documents',
		'Temporary': BGIS_Drive + r'\Other\_Dump\_Dump Documents',
		'History': BGIS_Drive + r'\Other\_Dump\_Dump Documents\_Dump History'
	},
	{
		'Id': "Pictures",
		'Initial': BGIS_Drive + r'\Other\Pictures\Screenpresso',
		'Temporary': BGIS_Drive + r'\Other\_Dump\_Dump Pictures',
		'History': BGIS_Drive + r'\Other\_Dump\_Dump Pictures\_Dump History'
	}
]

def TEST_Files():
	TEST_PrintNames(Folders[0])

def TEST_PrintNames(Directories):
	
	L1 = Directories['Initial']
	L2 = Directories['Temporary']
	L3 = Directories['History']
	
	L1_Files = os.listdir(L1)
	
	for i in range(len(L1_Files)):
		# print(L1_Files[i])
		filePath = os.path.join(L1, L1_Files[i])
		print(os.path.isdir(filePath), " - ", L1_Files[i])
		
	
	return
	

def Dump_Documents():
	
	for i in range(len(Folders)):
		for key, value in Folders[i].items():
			if (key == 'Id' and value == 'Documents'):
				Dump(Folders[i])
			
	return
	
def Dump_Pictures():
	
	for i in range(len(Folders)):
		for key, value in Folders[i].items():
			if (key == 'Id' and value == 'Pictures'):
				Dump(Folders[i])
			
	return
	
def Dump(Directories):
	
	L1 = Directories['Initial']
	L2 = Directories['Temporary']
	L3 = Directories['History']
	
	L1_Files = os.listdir(L1)
	L2_Files = [f for f in os.listdir(L2) if not f.startswith('_Dump')]
	
	Move(L2_Files, L2, L3)
	
	Move(L1_Files, L1, L2)
	
	return
	
def Move(Files, From, To):
	
	for file in Files:
		count = 0
		head, tail = os.path.splitext(file)
		dest_file = os.path.join(To,file) # may be updated, later is file_to
		file_from = os.path.join(From, file)
		
		if os.path.isdir(file):
			if os.path.exists(dest_file) and os.path.isdir(dest_file):
				
		elif os.path.isfile(file):
			while os.path.exists(dest_file):
				count += 1
				dest_file = os.path.join(To, '%s (%d)%s' % (head, count, tail))
		
		
		file_to = os.path.join(To, dest_file)
		print("dest_file - " + dest_file)
		# shutil.move(file_from, file_to)
		
		print("FROM - " + file_from + "\n" + "TO - " + file_to + "\n")
	
	return

if __name__ == '__main__':
	Dump_Documents()
	# Dump_Pictures()
	# TEST_Files()