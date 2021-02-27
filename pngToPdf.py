import os
from PIL import Image
from pathlib import Path

number = len(os.listdir('./recordedSS'))

cDir = Path.cwd()
fDir=cDir / "pdfSS"

if not os.path.exists(fDir):
    os.mkdir(fDir)

cDir=cDir/"recordedSS"
imgAdd=cDir/"img0.png"


img1=Image.open(imgAdd)
img1=img1.convert('RGB')

imgList =[]

a=1

for i in range(number-1):
    imgAdd=cDir/f"img{a}.png"
    img=Image.open(imgAdd)
    img = img.convert('RGB')
    imgList.append(img)
    a+=1

cDir = Path.cwd()
fDir=cDir / "pdfSS"

number2 = len(os.listdir('./pdfSS'))

fDir=fDir / f"pdfNo.{number2}.pdf"

img1.save(fDir,save_all=True,append_images=imgList)

mydir = cDir/'recordedSS'
for f in os.listdir(mydir):
    os.remove(os.path.join(mydir, f))