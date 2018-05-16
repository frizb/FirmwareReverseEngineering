# FirmwareReverseEngineering
I am by no means an expert at Firmware Reverse engineering. In fact, what I don’t know about Firmware development and reverse engineering could probably fill a library.  However, things that I learn and know I try to keep here for future reference. 

# Firmware Analysis Steps
## Step 1 – Collect the firmware
Firmware updates from a vendors website is often the easiest place to get a hold of the firmware of a device.
Alternatively, you can try to pull the firmware off the device.  Here is a list of some common ways to pull firmware off a device (note that capabilities on a device will vary)
1. SCP/SFTP/FTP/TFTP – If you are lucky the device will implement some kind of file transfer protocol interface which can be enabled and used to upload and download firmware and files from a device.
2.  JTAG implementations typically allow you to read/write memory, and flash chips are typically "mapped" into memory at some pre-defined address (finding that address is usually a matter of Googling, experience, and trial and error); thus, you can use tools like UrJTAG and OpenOCD to read the contents of flash.
3. Serial / UART -  These provide you with a command line interface either to a Linux console or a limited CLI (Command Line Interface) environment. Some bootloaders (e.g., U-Boot) do allow you to read/write flash/memory, and will dump the ASCII hex to your terminal window. You then would need to parse the hexdump and convert it into actual binary values.
 
4. SPI – Using a tool like the BusPirate / The Shikra, you can connect to the EEPROM firmware chip and pull the image directly from the chip.
5.  Snarfing - Extracting the content of a hardware chip is known as "snarf"ing. To snarf the contents of a chip, you need a ROM reader/programmer.  This is a destructive method of pulling the data as often you need to desolder the chip from the board and chances are the device will no longer work after you are done with it.

## Step 2 – Identify the firmware image
If you are lucky, Binwalk can provide insights into the contents of the firmware image.
```
root@kali:~# binwalk -B dd-wrt.v24-13064_VINT_mini.bin 

DECIMAL     HEX         DESCRIPTION
-------------------------------------------------------------------------------------------------------------------
0           0x0         TRX firmware header, little endian, header size: 28 bytes, image size: 2945024 bytes, CRC32: 0x4D27FDC4 flags: 0x0, version: 1
28          0x1C        gzip compressed data, from Unix, NULL date: Wed Dec 31 19:00:00 1969, max compression
2472        0x9A8       LZMA compressed data, properties: 0x6E, dictionary size: 2097152 bytes, uncompressed size: 2084864 bytes
622592      0x98000     Squashfs filesystem, little endian, DD-WRT signature, version 3.0, size: 2320835 bytes,  547 inodes, blocksize: 131072 bytes, created: Mon Nov  2 07:24:06 2009
```
However, if you find binwalk does not provide you with any feedback, it is time to rollup your sleeves and dig deeper.
```
root@kali:~# binwalk firmware.bin
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
```
We can use the binwalk Entropy analysis tool to check and see if the binary looks to be Encrypted or Compressed
```
root@kali:~/Desktop/1# binwalk -E firmware.bin

DECIMAL       HEXADECIMAL     ENTROPY
--------------------------------------------------------------------------------
0             0x0             Rising entropy edge (0.993183)
```
The results display an entropy graph that has a line along the 1 value, which is telling us there is lots of randomness to the file and it is likely encrypted or compressed.
If we are lucky the Linux file command will recognize the compression format:
```
root@kali:~/Desktop/1# file firmware.bin
firmware.bin: data
```
In this case, the format is not recognized by the file command and we need to take a look at the binary contents to better understand it.
## Step 3 – Decrypt the firmware
Often we find that the firmware is encrypted  with a simply XOR algorithm and the XOR encryption key can usually be reverse engineered out of the boot loader.


## Step 4 – Decompress the firmware
If the firmware appears to be compressed, we will need to identify the method of compression.
We can do this by examining the file header:
```
root@kali:~/Desktop/1# xxd -l 64 firmware.bin 
00000000: 5d00 0080 00ff ffff ffff ffff ff00 2e80  ]...............
00000010: 2c02 0065 b59b b60c 226d 652c b122 d769  ,..e...."me,.".i
00000020: 18e6 8bf4 5bac cc71 1ed1 62cd 1623 ae7c  ....[..q..b..#.|
00000030: a3f3 7df1 7dd7 38e5 e1f1 7d04 3002 bdfc  ..}.}.8...}.0...```
If we compare this header to the headers listed in the Identifying Compression Algorithms, we can see  this is an LZMA.
If the file conforms to a standard LZMA file format, it is easy to extract the data from it:
```
root@kali:~/ # lzma -d firmware.bin
root@kali:~/ #
```
Sadly, this is rarely the case.  Often we will see a customized implementation of various compression algorithms. 
```
root@kali:~/Desktop/1# lzma -d firmware.bin
lzma: firmware.bin: File format not recognized
```
In this case we need to take a good look at the binary content of the firmware image. 

## Step 5 – Reverse Engineer the firmware
Getting the correct offset value for the firmware can be tricky.



