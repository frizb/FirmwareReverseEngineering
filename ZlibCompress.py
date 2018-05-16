import zlib
import sys
import argparse


print('\033[0;32m'+"Zlib file compressor : " + '1.0' + " Updated: " + 'May 15, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'Compress a zlib file'+'\033[0;39m')
parser.add_argument("-input", metavar='file', type=str, default="file.out", help='Input file to compress (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="file.zlib", help='Output compressed zlib file (default: %(default)s)')
parser.add_argument("-compressionLevel", type=int, default=9, help='ZLib Compression level, in 0-9 or -1 (default: %(default)s)')
args = parser.parse_args()

str_object1 = open(args.input, 'rb').read()
str_object2 = zlib.compress(str_object1, args.compressionLevel)
f = open(args.output, 'wb')
f.write(str_object2)
f.close()