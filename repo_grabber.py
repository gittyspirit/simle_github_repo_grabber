#Grab github repositoris
import requests
import sys,os
while True:
    get_git = input("Did you install git on your computer?(Y/N) or quit(q):")
    if get_git == 'y' or get_git == 'Y':
        repo_name = input("Enter the github reository that you want to grab:")
        user_name = input("Enter the repository's owner's name:")
        command = "git clone https://github.com/"+"/"+ user_name + "/" + repo_name +".git"
        os.system(command)
    elif get_git == 'q' or get_git == 'Q':
        break
    elif get_git == 'N' or get_git == 'n':
        #For the portability
        if sys.platform == "linux":
            repo_name1 = input("Now Enter the github reository that you want to grab:")
            user_name1 = input("Enter the repository's owner's name:")
            linux_command = "wget "+ "https://codeload.github.com/" + user_name1 + "/" + repo_name1 + "/" + "zip/refs/heads/master"
            os.system(linux_command)
        else:
            repo_name2 = input("Then Enter the github reository that you want to grab:")
            user_name2 = input("Enter the repository's owner's name:")
            url = "https://codeload.github.com/" + user_name2 + "/" + repo_name2 + "/" + "zip/refs/heads/master"
            file = requests.get(url)
            dir_name = "python_downloads"
            os.makdir(dir_name)
            filename = dir_name+"/"+ repo_name2 + ".zip"
            with open(filename,'wb') as f:
                f.write(file.content)

