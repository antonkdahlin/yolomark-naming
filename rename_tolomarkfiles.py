import os
import shutil


CLASSNAME = ['black', 'pink', 'green', 'bag', 'red', 'chips']
singles = {}

def main():
    fix_ym("/home/ad/Yolo_mark/x64/Release/data/img/", "/home/ad/Documents/output/")
    print("done")



def fix_ym(src, dst):
    for file in filter(lambda x: x[-3:] == "txt", os.listdir(src)):
        fname = file[:-4]
        classes = []

        with open(src + file) as f:
            for line in f:
                classnum = int(line[0])
                classes.append(CLASSNAME[classnum])
        

        name = generate_filename(classes)
        #shutil.copyfile(original, target)
        shutil.copyfile("{}{}.txt".format(src, fname), "{}{}.txt".format(dst, name))
        shutil.copyfile("{}{}.jpg".format(src, fname), "{}{}.jpg".format(dst, name))
        


            


def generate_filename(classes):
    name = ""
    if len(classes) > 1:
        name = "-".join(classes)
        name = "{}{}".format(name, getCount(name))
    elif len(classes) == 1:
        name = "{}{}".format(classes[0], getCount(classes[0]))

    return(name)

def getCount(name):
    if name in singles:
        singles[name] += 1
    else:
        singles[name] = 0
    
    return singles[name]






if __name__ == "__main__":
    main()
