The example is a PNG used in the previous thread (the one showing "QUICKBMS") and attached to this thread.

#zlib#
It starts with 0x78 (rarely also with 0x58).
Use offzip to test if it's really zlib.
```
78 da ed 8f 6b 48 53 61 1c c6 df 65 35 ed 32 8d   x...kHSa...e5.2.
4a 49 9d 65 20 88 93 2d 13 ba a0 53 ab 85 5a b9   JI.e ..-...S..Z.
96 49 a2 76 d0 32 d7 cd a8 b9 72 a9 1d 2d fd 60   .I.v.2....r..-.`
65 84 a5 cd 4a 26 eb 2a 76 d9 64 5e 32 87 a7 bc   e...J&.*v.d^2...
```

#deflate#
Usually starts with 0xe*.
Use "offzip -z -15" to test if it's really deflate.
```
ed 8f 6b 48 53 61 1c c6 df 65 35 ed 32 8d 4a 49   ..kHSa...e5.2.JI
9d 65 20 88 93 2d 13 ba a0 53 ab 85 5a b9 96 49   .e ..-...S..Z..I
a2 76 d0 32 d7 cd a8 b9 72 a9 1d 2d fd 60 65 84   .v.2....r..-.`e.
a5 cd 4a 26 eb 2a 76 d9 64 5e 32 87 a7 bc 2c 69   ..J&.*v.d^2...,i
```

#lzo1x#
Parts of the original data are uncompressed.
```
25 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44   %.PNG........IHD
52 00 00 01 f4 6e 00 08 02 44 02 01 44 b4 48 dd   R....n...D..D.H.
58 00 06 09 70 48 59 73 00 00 0e c4 6c 00 00 32   X...pHYs....l..2
01 95 2b 0e 1b 00 00 07 81 49 44 41 54 78 da ed   ..+......IDATx..
```

#lzss#
Parts of the original data uncompressed.
```
ff 89 50 4e 47 0d 0a 1a 0a ff 00 00 00 0d 49 48   ..PNG.........IH
44 52 6f 00 00 01 f4 fe f1 08 02 f6 f0 ef 44 b4   DRo...........D.
48 dd f6 f0 09 70 48 bf 59 73 00 00 0e c4 17 01   H....pH.Ys......
01 ff 95 2b 0e 1b 00 00 07 81 ff 49 44 41 54 78   ...+.......IDATx
```

#Xmemcompress / LZX#
Usually it starts with 0xff.
There are also some file formats created with the xbcompress tool, they start with 0x0F 0xF5 0x12 0xEE (lzx native) or 0x0F 0xF5 0x12 0xED (lzx decode).
```
ff 07 cf 03 4a 00 10 f3 7c 00 00 42 00 50 22 00   ....J...|..B.P".
00 5f 00 c1 41 0c 02 bb bd 70 b9 29 b3 1b db 8c   ._..A....p.)....
38 f3 dc 0e b0 54 59 32 67 c5 9c 1b cf 8f 9c 2f   8....TY2g....../
7b cc 73 26 2a 81 59 4f 89 2e 4a 11 da 90 31 03   {.s&*.YO..J...1.
```

#Bzip2#
Fixed signature, BZh91.
```
42 5a 68 39 31 41 59 26 53 59 c3 87 b9 ea 00 02   BZh91AY&SY......
9e ff ff ff ff ef bf f2 5d f9 ef fe ff fd be ff   ........].......
fe ff ff f8 fd 7f fb 7f bf df fb ff b5 f7 bf 9f   ................
ff ff ff c0 02 9c 1a cc db 02 2a 90 d0 d0 1a 03   ..........*.....
```

#gzip#
0x1f 0x8b, note that usually it contains deflate data, rarely lzma and some rare games use also other types of compressions (quickbms automatically handles all of them).
```
1f 8b 08 00 00 00 00 00 00 00 eb 0c f0 73 e7 e5   .............s..
92 e2 62 60 60 e0 f5 f4 70 09 62 60 60 fc 02 c2   ..b``...p.b``...
1c 4c 40 11 97 2d 1e 77 81 14 67 81 47 64 31 03   .L@..-.w..g.Gd1.
03 df 11 10 66 9c aa cd 27 cd c0 c0 de e8 e9 e2   ....f...'.......
```

#JCalg#
It starts with JC.
```
4a 43 cf 07 00 00 84 a9 56 bb 14 6a e2 20 15 36   JC......V..j. .6
3c ea 03 45 26 1a 12 45 9a 14 1f 90 03 a4 20 42   <..E&..E...... B
09 a0 da 44 93 40 3b a0 3b 52 ac 18 b8 09 71 87   ...D.@;.;R....q.
d0 dc 95 03 4a 00 81 8d 96 95 49 03 1f 24 97 6a   ....J.....I..$.j
```

#LZMA#
0x5d at the beginning (it's a flag), a 32bit field (size of the dictionary) and the lzma data.
The raw lzma stream usually starts with a 0x00 (offset 0x5)
Note: if you use "comptype lzma_compress" in QuickBMS to compress data, your output will start with 0x2c instead of 0x5d, I modified the dump to make everything easier for you.
```
5d 00 00 00 08 00 44 94 a6 b1 a9 14 37 65 03 e8   ].....D.....7e..
61 4e b5 0a 29 f7 bc f4 0a 39 10 76 ec 9c fe 41   aN..)....9.v...A
1a 6a 07 81 ce e1 e0 58 3f 2f a1 6a c9 03 2d 24   .j.....X?/.j..-$
38 74 b0 3d 19 ab 33 0c 73 57 75 94 da 8a ac 7e   8t.=..3.sWu....~
```

#lzma 86 head#
As before with a 64bit uncompressed size field before the compressed data.
```
5d 00 00 00 08 cf 07 00 00 00 00 00 00 00 44 94   ].............D.
a6 b1 a9 14 37 65 03 e8 61 4e b5 0a 29 f7 bc f4   ....7e..aN..)...
0a 39 10 76 ec 9c fe 41 1a 6a 07 81 ce e1 e0 58   .9.v...A.j.....X
3f 2f a1 6a c9 03 2d 24 38 74 b0 3d 19 ab 33 0c   ?/.j..-$8t.=..3.
```

#lzma 86 dec#
One byte more than lzma.
```
5d 00 00 00 08 00 00 44 94 a6 b1 a9 14 37 65 03   ]......D.....7e.
e8 61 4e b5 0a 29 f7 bc f4 0a 39 10 76 ec 9c fe   .aN..)....9.v...
41 1a 6a 07 81 ce e1 e0 58 3f 2f a1 6a c9 03 2d   A.j.....X?/.j..-
24 38 74 b0 3d 19 ab 33 0c 73 57 75 94 da 8a ac   $8t.=..3.sWu....
```

#lzma 86 dec head#
All the fields seen before.
```
5d 00 00 00 08 00 cf 07 00 00 00 00 00 00 00 44   ]..............D
94 a6 b1 a9 14 37 65 03 e8 61 4e b5 0a 29 f7 bc   .....7e..aN..)..
f4 0a 39 10 76 ec 9c fe 41 1a 6a 07 81 ce e1 e0   ..9.v...A.j.....
58 3f 2f a1 6a c9 03 2d 24 38 74 b0 3d 19 ab 33   X?/.j..-$8t.=..3
```

#lzma efs#
Used by the ZIP file format.
```
5d 00 00 00 08 00 00 05 00 00 44 94 a6 b1 a9 14   ].........D.....
37 65 03 e8 61 4e b5 0a 29 f7 bc f4 0a 39 10 76   7e..aN..)....9.v
ec 9c fe 41 1a 6a 07 81 ce e1 e0 58 3f 2f a1 6a   ...A.j.....X?/.j
c9 03 2d 24 38 74 b0 3d 19 ab 33 0c 73 57 75 94   ..-$8t.=..3.sWu.
```

#lzma without prop / headerless#
```
00 44 94 a6 b1 a9 14 37 65 03 e8 61 4e b5 0a 29   .D.....7e..aN..)
f7 bc f4 0a 39 10 76 ec 9c fe 41 1a 6a 07 81 ce   ....9.v...A.j...
e1 e0 58 3f 2f a1 6a c9 03 2d 24 38 74 b0 3d 19   ..X?/.j..-$8t.=.
ab 33 0c 73 57 75 94 da 8a ac 7e 5d 55 f3 19 4d   .3.sWu....~]U..M
```

#RNC#
"RNC" magic, version (1 and 2), uncompressed size.
```
52 4e 43 01 00 00 07 cf 00 00 03 06 d5 26 b5 99   RNC..........&..
00 00 20 21 12 9a 21 06 60 45 22 32 00 a6 40 64   .. !..!.`E"2..@d
04 80 80 64 00 42 89 50 4e 47 0d 0a 1a 0a 00 00   ...d.B.PNG......
00 0d 49 48 44 52 00 00 01 f4 5f 2d 08 02 02 01   ..IHDR...._-....
```

#Zpaq#
"zPQ" magic, currently I have never seen this compression used in games.
```
7a 50 51 01 01 c4 00 05 09 00 00 16 01 a0 03 05   zPQ.............
08 0d 01 08 10 02 08 12 03 08 13 04 08 13 05 08   ................
14 06 04 16 18 03 11 08 13 09 03 0d 03 0d 03 0d   ................
03 0e 07 10 00 0f 18 ff 07 08 00 10 0a ff 06 00   ................
```

#Snappy#
Uncompressed size before the data.
```
cf 0f 4c 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49   ..L.PNG........I
48 44 52 00 00 01 f4 01 04 50 08 02 00 00 00 44   HDR......P.....D
b4 48 dd 00 00 00 09 70 48 59 73 00 00 0e c4 01   .H.....pHYs.....
04 f0 46 01 95 2b 0e 1b 00 00 07 81 49 44 41 54   ..F..+......IDAT
```

#Gipfeli#
Small header with 32bit uncompressed size.
```
02 cf 07 60 00 35 da 0c 80 28 06 40 13 03 75 00   ...`.5...(.@..u.
2a 01 02 38 00 d2 01 a8 04 ea 00 34 40 05 54 0d   *..8.......4@.T.
6a 0b 40 73 0d 35 50 07 a0 2d a4 03 50 cc 35 48   j.@s.5P..-..P.5H
45 48 2d 00 cc ff 16 80 e6 1a b4 2d 00 07 c0 df   EH-........-....
```

#LZG#
"LZG" magic and uncompressed size.
```
4c 5a 47 00 00 07 cf 00 00 03 26 94 ed 70 6b 01   LZG.......&..pk.
12 18 23 24 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d   ..#$.PNG........
49 48 44 52 00 00 01 f4 24 62 08 02 23 0a 44 b4   IHDR....$b..#.D.
48 dd 24 c1 09 70 48 59 73 00 00 0e c4 24 62 01   H.$..pHYs....$b.
```

#Doboz#
Small header with uncompressed size.
```
08 cf 07 5a 03 00 00 90 90 89 50 4e 47 0d 0a 1a   ...Z......PNG...
0a 00 00 00 0d 49 48 44 52 00 00 01 f4 06 01 08   .....IHDR.......
02 48 44 b4 48 dd 1c 09 70 80 00 00 80 48 59 73   .HD.H...p....HYs
00 00 0e c4 06 01 01 95 2b 0e 1b 00 00 07 81 49   ........+......I
```

#SFL block#
```
40 00 00 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49   @...PNG........I
48 44 52 09 08 00 00 01 f4 00 41 08 02 01 20 44   HDR.......A... D
b4 48 dd 00 70 09 70 48 02 00 59 73 00 00 0e c4   .H..p.pH..Ys....
00 41 01 95 2b 0e 1b 00 00 07 81 00 00 49 44 41   .A..+........IDA
```

#SFL bits#
```
0f 89 50 4e 47 0d 0a 1a 0a 84 0c 0d 49 48 44 52   ..PNG.......IHDR
83 00 08 f4 83 00 08 f4 03 01 84 0b 44 b4 48 dd   ............D.H.
84 0c 09 70 48 59 73 83 09 0e c4 83 09 0e c4 00   ...pHYs.........
0b 95 2b 0e 1b 83 15 07 81 49 44 41 54 78 da ed   ..+......IDATx..
```

#LZF#
```
13 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44   ..PNG........IHD
52 00 00 01 f4 40 03 01 08 02 20 11 03 44 b4 48   R....@.... ..D.H
dd 20 06 08 09 70 48 59 73 00 00 0e c4 40 03 1f   . ...pHYs....@..
01 95 2b 0e 1b 00 00 07 81 49 44 41 54 78 da ed   ..+......IDATx..
```

#Brieflz#
```
89 00 00 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48   ...PNG........IH
44 52 00 00 10 00 01 f4 03 08 02 00 00 00 44 b4   DR............D.
48 04 00 dd 00 00 00 09 70 48 59 73 00 00 0e c4   H.......pHYs....
00 00 03 01 95 2b 0e 1b 00 00 07 81 49 44 41 54   .....+......IDAT
```

#Falcom (used in the Ys series)#
32bit compressed size at the beginning.
```
3d 03 00 00 89 50 4e 47 0d 0a 1a 0a 0a 4a 00 01   =....PNG.....J..
0d 49 48 44 52 07 01 f4 04 24 21 08 02 12 44 b4   .IHDR....$!...D.
48 dd 07 41 89 09 70 48 59 73 07 0e c4 04 a0 00   H..A..pHYs......
01 95 2b 0e 1b 09 07 81 49 44 41 54 78 da 00 00   ..+.....IDATx...
```

#LZ4#
Usually it starts with a 0xf* byte.
```
f0 05 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48   ...PNG........IH
44 52 00 00 01 f4 04 00 f0 06 08 02 00 00 00 44   DR.............D
b4 48 dd 00 00 00 09 70 48 59 73 00 00 0e c4 04   .H.....pHYs.....
00 f5 37 01 95 2b 0e 1b 00 00 07 81 49 44 41 54   ..7..+......IDAT
```

#Yappy#
```
1f 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44   ..PNG........IHD
52 00 00 01 f4 00 00 01 f4 08 02 00 00 00 44 b4   R.............D.
48 1f dd 00 00 00 09 70 48 59 73 00 00 0e c4 00   H......pHYs.....
00 0e c4 01 95 2b 0e 1b 00 00 07 81 49 44 41 54   .....+......IDAT
```

#NitroSDK (Nintendo)#
The first byte is the type of compression: 0x00, 0x10, 0x11, 0x20, 0x40.
```
10 cf 07 00 00 89 50 4e 47 0d 0a 1a 0a 00 00 00   ......PNG.......
00 0d 49 48 44 52 09 00 00 01 f4 10 03 08 02 00   ..IHDR..........
11 08 44 b4 48 dd 00 18 09 70 48 02 59 73 00 00   ..D.H....pH.Ys..
0e c4 10 03 01 00 95 2b 0e 1b 00 00 07 81 00 49   .......+.......I
```

#LZMA2#
```
18 e0 07 ce 02 fa 5d 00 44 94 05 c4 7a 27 f6 f7   ......].D...z'..
ee 89 8e 50 90 88 b3 aa cc 1b 2e 9b 5a d1 1a 08   ...P........Z...
c2 69 96 f7 ad ab 24 88 1f 78 89 db 47 9f ab 1e   .i....$..x..G...
d5 ee e0 c1 8b b2 c9 82 e1 c5 12 78 20 65 03 85   ...........x e..
```

#LZMA2 headerless#
```
e0 07 ce 02 fa 5d 00 44 94 05 c4 7a 27 f6 f7 ee   .....].D...z'...
89 8e 50 90 88 b3 aa cc 1b 2e 9b 5a d1 1a 08 c2   ..P........Z....
69 96 f7 ad ab 24 88 1f 78 89 db 47 9f ab 1e d5   i....$..x..G....
ee e0 c1 8b b2 c9 82 e1 c5 12 78 20 65 03 85 04   ..........x e...
```

#Oodle#
Usually it starts with the byte 0x8c.
```
8c 0b 43 03 61 df 01 00 12 19 83 e0 b4 78 4b e0   ..C.a........xK.
ab 74 91 77 97 86 13 9d 40 07 b7 d4 0d 76 5c 7d   .t.w....@....v\}
56 81 8f 7c f0 33 c0 1a 9a fc 0d ad 47 80 4b fc   V..|.3......G.K.
49 93 f9 fc 4c a6 b7 80 17 a4 bc 8c 07 f9 8d 31   I...L..........1
```

#zstd#
It starts with a little endian 32bit magic number, when seen with a hex editor only the first byte (the low 8bit) is different because it depends by the version of the algorithm:
```
1e b5 2f fd    v0.1
22 b5 2f fd    v0.2
23 b5 2f fd    v0.3
24 b5 2f fd    v0.4
25 b5 2f fd    v0.5
26 b5 2f fd    v0.6
27 b5 2f fd    v0.7
28 b5 2f fd    v0.8, current version
```

This terrific information came from the following thread on Zenhax.com:
http://zenhax.com/viewtopic.php?t=27



