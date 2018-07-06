import os

def storage_choice(d,movie_name):
    print("Press 1 if you want the file to be downloaded on Desktop!" +'\n'+
              'Press 2 if you want the file to be downloaded in testing_downloads directory'+'\n'+
              'Press 3 to feed your own custom download path')
    print("....waiting for user input....."+'\n')
    a = input()
    if a == '2':
        path = os.path.abspath("C:\\Users\\vipul\\Desktop\\Movie_Automations\\testing_downloads")
        dir = os.chdir(path)
        filename = movie_name + '.zip'
        with open(filename, "wb") as f:
            f.write(d.content)
        f.close()
    elif a=='1':
        path = os.path.abspath(os.path.expanduser('~/Desktop'))
        dir = os.chdir(path)
        filename = movie_name + '.zip'
        with open(filename, "wb") as f:
            f.write(d.content)
        f.close()

    elif a=='3':
        path = input("Enter the path you want the file to be downloaded at : ")
        dir = os.chdir(path)
        filename = movie_name + '.zip'
        with open(filename, "wb") as f:
            f.write(d.content)
        f.close()





