import os


def recursion(scr, target):
    filelist = os.listdir(scr)
    for file in filelist:
        if os.path.isdir(file):
            path = os.path.join(scr, file)
            newpath = os.path.join(target, file)
            os.mksdir(newpath)
            recursion(path, newpath)
        else:
            path1 = os.path.join(scr, file)
            with open(path1, 'r+') as f1:
                data = f1.read()
                path2 = os.path.join(target, file)
                with open(path2, 'w+') as f2:
                    f2.write(data)
recursion(r'a1', r'a2')