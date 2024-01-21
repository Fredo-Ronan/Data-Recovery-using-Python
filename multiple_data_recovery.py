drive = "\\\\.\\F:"     # Open drive as raw bytes
fileD = open(drive, "rb")
size = 512              # Size of bytes to read
byte = fileD.read(size) # Read 'size' bytes
offs = 0                # Offset location
drec = False            # Recovery mode
rcvd = 0                # Recovered file ID

def foundJPG():
    found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
    if found >= 0:
        drec = True
        print('==== Found JPG at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open(str(rcvd) + '.jpg', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\xff\xd9')
            fileN.write(byte)
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((offs+1)*size)
                print('==== Wrote JPG to location: ' + str(rcvd) + '.jpg ====\n')
                drec = False
                rcvd += 1
                fileN.close()
            else: fileN.write(byte)

def foundPNG():
    found = byte.find(b'\x89\x50\x4E\x47')
    if found >= 0:
        drec = True
        print('==== Found PNG at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open(str(rcvd) + '.png', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x49\x45\x4E\x44\xAE\x42\x60\x82')
            fileN.write(byte)
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((offs+1)*size)
                print('==== Wrote PNG to location: ' + str(rcvd) + '.png ====\n')
                drec = False
                rcvd += 1
                fileN.close()
            else: fileN.write(byte)

def foundPDF():
    found = byte.find(b'\x25\x50\x44\x46\x2D\x31\x2E\x37')
    if found >= 0:
        drec = True
        print('==== Found PDF at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open(str(rcvd) + '.pdf', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x4F\x46')
            fileN.write(byte)
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((offs+1)*size)
                print('==== Wrote PDF to location: ' + str(rcvd) + '.pdf ====\n')
                drec = False
                rcvd += 1
                fileN.close()
            else: fileN.write(byte)

def foundDOC():
    found = byte.find(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1')
    if found >= 0:
        drec = True
        print('==== Found DOC at location: ' + str(hex(found+(size*offs))) + ' ====')
        # Now lets create recovered file and search for ending signature
        fileN = open(str(rcvd) + '.doc', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x20\x57\x6F\x72\x64\x20\x39\x37\x2D\x32\x30\x30\x33')
            fileN.write(byte)
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((offs+1)*size)
                print('==== Wrote DOC to location: ' + str(rcvd) + '.doc ====\n')
                drec = False
                rcvd += 1
                fileN.close()
            else: fileN.write(byte)

def foundDOCX():
    pass

def foundMP4():
    pass

def findAllSupportedFiles():
    foundJPG()
    foundPNG()
    foundPDF()
    foundDOC()
    foundDOCX()
    foundMP4()

while byte:
    findAllSupportedFiles()
    byte = fileD.read(size)
    offs += 1

fileD.close()