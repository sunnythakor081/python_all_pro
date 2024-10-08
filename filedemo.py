import sys
infile = open(sys.argv[1] , 'r') # open for reading
outfile = open(sys.argv[2] , 'w') # open for writing

for line in infile: # read
    print(line, file=outfile, end='') # write

infile.close()
outfile.close() 