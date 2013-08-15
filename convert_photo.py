import glob,os,wand.image

def convertPhoto(AbsPath,TargetName):
    with wand.image.Image(filename=AbsPath) as img:
	WantedHeight = 500.
        factor = WantedHeight/img.height
        NewWidth = factor*img.width
        NewHeight = factor*img.height
        c =  img.clone()
        c.transform("","%d%%"%int(factor*100))
        c.save(filename=TargetName)
        pass
    pass

OriginalList = glob.glob('portfolio/img/originals/*jpg')

    
OriginalList = glob.glob('portfolio/img/originals/*jpg')
for AbsPath in OriginalList:
    Name = os.path.basename(AbsPath)
    TargetDir = os.path.join('portfolio','img')
    TargetName = os.path.join(TargetDir,Name)
    if not os.path.exists(TargetName):
        print TargetName
        convertPhoto(AbsPath,TargetName)
        pass
    pass

