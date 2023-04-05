import os
#print(os.listdir())
print("Op. system is: ", os.name)
if os.name == "posix": separ = "/"
else: separ = "\\"



def cur_dirs_list(cdir_content=['dirname'], dirname=['dirname'], path = os.getcwd()):

    directories = []
    for name in cdir_content:

        if "." not in name:
            directories.append(name)

    #print(directories)
    return directories


def find(path = os.getcwd(), dirname = "dirname"):
    #print(os.getcwd(), 'cwd')
    #print(os.listdir(path))
    cdir_content = os.listdir(path)
    #print(cdir_content)

    cur_dirs = cur_dirs_list(cdir_content, dirname, path)

    for name in cur_dirs:
        if name == dirname:
            print (path+separ+name)

        tofind = find(path+separ+name, dirname)

    #return path

result = find("c:\\Users\\User\\Documents\\IT", "dirname")