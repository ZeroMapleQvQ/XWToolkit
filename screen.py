from os import rmdir, mkdir, path
from subprocess import run, PIPE

# 删除enable文件夹
if path.isdir(".\\enable") == True:
    rmdir(".\\enable")
# 建立disable文件夹
if path.isdir(".\\disable") == False:
    mkdir(".\\disable")


def enable_touch(ID):
    '''启用触摸屏'''
    run(".\devcon.exe>nul 2>nul enable "+ID,
        shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    rmdir("disable")
    mkdir("enable")
    return "enable"


def disable_touch(ID):
    '''禁用触摸屏'''
    run(".\devcon.exe>nul 2>nul disable "+ID,
        shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    rmdir("enable")
    mkdir("disable")
    return "disable"
