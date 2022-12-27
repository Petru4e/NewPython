# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.


path1 = 'file_1.txt'
file1 = open(path1, 'r')
path2 = 'file_2.txt'
file2 = open(path2, 'r')
path_res = 'file_res.txt'

file_result = open(path_res, 'w')
file_result.write(f'{file1.read()} + {file2.read()}')

file1.close()
file2.close()
file_result.close()