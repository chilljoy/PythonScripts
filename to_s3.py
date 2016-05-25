import os

source = raw_input('Enter source item name, case sensitve: ')

dest = raw_input('Enter dest folder name, case sensitve: ')

os.system("s3cmd put "+ source + " s3://employeebackups/" + dest + "/ -vv --multipart-chunk-size-mb=200")