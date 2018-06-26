import shutil
import os

def walk(path):
	if not os.path.exists(path):
		return -1

	for root, dirs, names in os.walk(path):
		for dirname in dirs:
			if dirname == 'unitTest':
				print("Deleting: " + os.path.join(root,dirname))
				shutil.rmtree(os.path.join(root,dirname))

path = ".\\mst0626"
walk(path)