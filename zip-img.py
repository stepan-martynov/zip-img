import os
import subprocess
import glob

def cp_imgs(imgs, dirname_source, dirname_copy):
	for img in imgs:
		# img_path_copy = dirname_copy + '/' + img
		subprocess.run(['cp', img, dirname_copy + '/' + img.split('/')[1]])

def zip_imgs(dirname_copy):
	imgs = glob.glob(os.path.join(dirname_copy, "*.jpg"))
	for img in imgs:
		subprocess.run(['sips', '--resampleWidth', '200', img])

def main():
	dirname_source = 'Source'
	dirname_copy = 'Copy'
	imgs = glob.glob(os.path.join(dirname_source, "*.jpg"))
	subprocess.run(['mkdir', dirname_copy])
	cp_imgs(imgs, dirname_source, dirname_copy)
	zip_imgs(dirname_copy)

if __name__ == '__main__':
	main()