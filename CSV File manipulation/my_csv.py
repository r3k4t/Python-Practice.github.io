'''
import csv
file = open('example.csv')
file_reader = csv.reader(file)

data = list(file_reader)
print(data)
print(data[0][2])
'''

'''
#Fast Work with looping 

import csv
file = open ('example.csv')
file_reader = csv.reader(file)

# for loop
for  row in  file_reader:
    print('Row on :'+str(file_reader.line_num)+' '+str(row))
'''



'''

#newline

import csv
output_file = open('output.csv','w',newline='')
output_writer=csv.writer(output_file)
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['15','25','35','45'])
output_file.close()
'''

'''

import csv
output_file = open('output.csv','w')
output_writer = csv.writer(output_file)
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['15','25','35','45'])
output_file.close()
'''

#delimiter 

import csv
output_file = open('output.csv','w')
output_writer = csv.writer(output_file,delimiter ='.')
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['15','25','35','45'])
output_file.close()


