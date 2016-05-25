import os

rootdirectory = # ex: ~/Documents/SpecialFiles
bucket = #s3 bucket name
chunksize = 200 #mb 


folder = raw_input('Enter folder name, case sensitve: ')

os.system("s3cmd put " + rootdirectory + folder + " -r s3://" + bucket + "/ -vv --multipart-chunk-size-mb=" + chunksize)