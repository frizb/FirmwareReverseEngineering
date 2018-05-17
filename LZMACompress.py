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
parser.add_argument("-format", type=int, default=1, help='LZMA compression format mode: ALONE = 2, AUTO = 0, RAW = 3, XZ = 1 (default: %(default)s)')
parser.add_argument("-check", type=int, default=0, help='LZMA integrity check type NONE = 0, CRC32 = 1, CRC64 = 4, ID_MAX = 15, SHA256 = 10, UNKNOWN = 16  (default: %(default)s)')
parser.add_argument("-preset", type=int, default=None, help='LZMA compression level preset, an integer between 0 and 9. Also can be OR-ed with the constant preset EXTREME Constant 2147483648 (default: %(default)s)')
parser.add_argument("-lzma1", action='store_true', help='Use LZMA version 1 (default: XZ compression mode)')
parser.add_argument("-lzma2", action='store_true', help='Use LZMA version 2 (default: XZ compression mode)')
parser.add_argument("-rawlzma1", action='store_true', help='Use Raw LZMA version 1 (default: XZ compression mode)')
parser.add_argument("-rawarm", action='store_true', help='Use Raw LZMA ARM (default: XZ compression mode)')
args = parser.parse_args()

binary_object1 = open(args.input, 'rb').read()

if args.lzma1 is True:
    props = lzma._encode_filter_properties({'id': lzma.FILTER_LZMA1})
    lzma_comp = lzma.LZMACompressor(lzma.FORMAT_ALONE, filters=[
        lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)
    ], preset=args.preset)
    binary_object2 = lzma_comp.compress(binary_object1)
    lzma_comp.flush()
elif args.lzma2 is True:
    props = lzma._encode_filter_properties({'id': lzma.FILTER_LZMA2})
    lzma_comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
        lzma._decode_filter_properties(lzma.FILTER_LZMA2, props)
    ], preset=args.preset)
    binary_object2 = lzma_comp.compress(binary_object1)
    lzma_comp.flush()
elif args.rawlzma1 is True:
    props = lzma._encode_filter_properties({'id': lzma.FILTER_LZMA1})
    lzma_comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
        lzma._decode_filter_properties(lzma.FILTER_LZMA1, props)
    ], preset=args.preset)
    binary_object2 = lzma_comp.compress(binary_object1)
    lzma_comp.flush()
elif args.rawarm is True:
    props = lzma._encode_filter_properties({'id': lzma.FILTER_ARM})
    lzma_comp = lzma.LZMACompressor(lzma.FORMAT_RAW, filters=[
        lzma._decode_filter_properties(lzma.FILTER_ARM, props)
    ],preset=args.preset)
    binary_object2 = lzma_comp.compress(binary_object1)
    lzma_comp.flush()
else:
    binary_object2 = lzma.compress(binary_object1, format=args.format, preset=args.preset)

with open(args.output, 'wb') as f:
    f.write(binary_object2)