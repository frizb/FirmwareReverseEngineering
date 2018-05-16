# Easier to run using Python 3
try:
    import lzma
except ImportError:
    from backports import lzma
import sys
import argparse

print('\033[0;32m'+"LZMA file compressor : " + '1.0' + " Updated: " + 'May 15, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'Compress a file using LZMA'+'\033[0;39m')
parser.add_argument("-input", metavar='file', type=str, default="file.out", help='Input file to compress (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="file.lzma", help='Output compressed LZMA file (default: %(default)s)')
parser.add_argument("-format", type=int, default=None, help='LZMA compression format mode: ALONE = 2, AUTO = 0, RAW = 3, XZ = 1 (default: %(default)s)')
parser.add_argument("-check", type=int, default=0, help='LZMA integrity check type NONE = 0, CRC32 = 1, CRC64 = 4, ID_MAX = 15, SHA256 = 10, UNKNOWN = 16  (default: %(default)s)')
parser.add_argument("-preset", type=int, default=None, help='LZMA compression level preset, an integer between 0 and 9. Also can be OR-ed with the constant preset EXTREME Constant 2147483648 (default: %(default)s)')
args = parser.parse_args()

#parser.add_argument("-filter", type=int, default=None, help='LZMA filter chain OR-ed together: ARM = 7, ARMTHUMB = 8, DELTA = 3, IA64 = 6, LZMA1 = 4611686018427387905, LZMA2 = 33, POWERPC = 5, SPARC = 9, X86 = 4 (default: %(default)s)')

str_object1 = open(args.input, 'rb').read()
if args.format is None:
    str_object2 = lzma.compress(str_object1, preset=args.preset)
else:
    str_object2 = lzma.compress(str_object1, format=args.format, preset=args.preset)
with open(args.output, 'wb') as f:
    f.write(str_object2)