# Easier to run using Python 3
try:
    import lzma
except ImportError:
    from backports import lzma
import sys
import argparse

print('\033[0;32m'+"LZMA file decompressor : " + '1.0' + " Updated: " + 'May 15, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'Decompress a file using LZMA'+'\033[0;39m')
parser.add_argument("-input", metavar='file', type=str, default="file.lzma", help='Input file to LZMA decompress (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="file3.out", help='Output decompressed file (default: %(default)s)')
args = parser.parse_args()

str_object1 = open(args.input, 'rb').read()
str_object2 = lzma.decompress(str_object1)
with open(args.output, 'wb') as f:
    f.write(str_object2)