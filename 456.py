import os
import binascii
import struct

misc = open("C:/Users/Kevin/Desktop/r2s/encoded.png","rb").read()

for i in range(650):
    for j in range(650):
        data = misc[12:16] + struct.pack('>i',i) + struct.pack('>i', j) + misc[24:29]  #misc[]為二進位制第12到16bytes的位置
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == 0xF8FFF17E: #符合pngcheck算出來的數字
            print(hex(i))
            print(hex(j))