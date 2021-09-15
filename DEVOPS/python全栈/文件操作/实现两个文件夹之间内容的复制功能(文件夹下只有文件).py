import os
def copy(srcdir,targedir):
    filelist = os.listdir(srcdir)
    for file in filelist:
        path = os.path.join(srcdir, file)
        with open(path, 'r+') as f1:
            data = f1.read()
            path1 = os.path.join(targedir,file)
            with open(path1, 'w+') as f2:
                f2.write(data)