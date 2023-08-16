fhand = open('mbox_short.txt')

for lx in fhand:
    ly = lx.strip()
    ly = ly.upper()
    print(ly)
