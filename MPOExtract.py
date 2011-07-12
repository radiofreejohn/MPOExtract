#!/usr/bin/env python
import sys
import os

if len(sys.argv) == 2:
    inputFile = sys.argv[1]
    if os.path.isfile(inputFile):
        ff = open(inputFile, 'rb')
        ff.seek(6)
        data = ff.read()
        # find the marker for the second image
        offset = data.find('\xFF\xD8\xFF\xE1')
        dataLeft = data[offset:]
        print "size of left: ", len(dataLeft)
        ff.seek(0)
        data = ff.read()
        dataRight = data[:offset+6]
        filePair = os.path.splitext(inputFile)
        fileName = filePair[0]
        # write output
        left = open(fileName+'-L.jpg', 'wb')
        left.write(dataLeft)
        left.close()
        right = open(fileName+'-R.jpg', 'wb')
        right.write(dataRight)
        right.close()
    else:
        print "No such file, %s" % (inputFile)
else:
    print "%s takes only one argument, a single file ending with .mpo" % (sys.argv[0])
