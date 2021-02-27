from PIL import ImageGrab
import imagehash
import numpy as np

import os
from pathlib import Path
import time



print("Give integer value{greater than 1} for base(default 9)[MORE VALUE MEANS MORE PRECISION] OR give any other value to pass ")
base=input()
try:
    base=int(base)
except:
    base=9



cDir = Path.cwd()
print(cDir)
fDir=cDir / "recordedSS"

if not os.path.exists(fDir):
    os.mkdir(fDir)
i=0

similarity = 100
# base =8
threshold = 1-similarity/100
diff_limit = int(threshold*(base**2))

fDir=fDir / f"img{i}.png"
image = ImageGrab.grab()
image.save(fDir)
img1 = image
hashImg1=imagehash.average_hash(img1,base)
print(hashImg1)
i += 1
fDir=str(fDir)
fDir=fDir[:-8]
fDir=Path(fDir)
time.sleep(5)

fDir=fDir / f"img{i}.png"
image = ImageGrab.grab()
image.save(fDir)
img2 = image
hashImg2=imagehash.average_hash(img2,base)
print(hashImg2)
i += 1
fDir=str(fDir)
fDir=fDir[:-8]
fDir=Path(fDir)
time.sleep(5)
while(True):

    fDir=fDir / f"img{i}.png"

    image = ImageGrab.grab()
    img3=image
    hashImg3=imagehash.average_hash(img3,base)
    print(hashImg3)
    if not np.count_nonzero(hashImg3 != hashImg1) <= diff_limit:
        if not np.count_nonzero(hashImg3 != hashImg2) <= diff_limit:
            print(f"hash value 1: {hashImg1}\n")
            print(f"hash value 2: {hashImg2}\n")
            print(f"hash image 3:{hashImg3}\n")
            print(fDir)
            image.save(fDir)
            hashImg1=hashImg2
            hashImg2=hashImg3
            i += 1

    fDir=str(fDir)
    if(i<10):
        fDir=fDir[:-8]
    elif(i<100):
        fDir=fDir[:-9]
    else:
        fDir=fDir[:-10]

    fDir=Path(fDir)
    time.sleep(1)


