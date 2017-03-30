import os
import subprocess
import glob

# import os.path

# def create_file_list(files, part_of_file):
# 	files_list = []
# 	for file in files:
# 		with open(file) as f:
# 			if part_of_file in f.read():
# 				files_list.append(file)
# 	return files_list


# def main():
# 	input_dirname = input('В какой папке будем искать?: ')
# 	files = glob.glob(os.path.join(input_dirname, "*.sql"))

# 	while True:
# 		part_of_file = input('Введите часть файла, которую помните: ')
# 		files = create_file_list(files, part_of_fileof_file)
# 		print(files)
# 		print(len(files))

# if __name__ == '__main__':
# 	main()

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