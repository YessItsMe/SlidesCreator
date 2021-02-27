# SlidesCreator
This can be used to create slides while watching videos

By default it will capture whole screen and you can change that by giving bBox argument in image grab function with your requirements

Steps:
1)run main file and start watching video
2)it will create a folder named recordedSS
3)recordedSS will contain all the different SS taken during video
4)after that you can have a look at them in recordedSS folder and you can delete unnecessary ss
5)Finaly run pngToPdf and it will create a folder named pdfss which will contain your latest pdf andit will empty your recordedSS folder

Base value: higher the base value more precision will be there(small changes will be catched) and lower value will have lower precision

youtube video link explaining working: 

required libraries:  ImageGrab,imagehash,numpy,os,pathlib,time

