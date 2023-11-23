from os import rmdir, mkdir
from ctypes import windll
from subprocess import run, PIPE

with open("ID.txt") as f:
    read = f.read()


def enable_touch():
    '''启用触摸屏'''
    run(".\devcon.exe>nul 2>nul enable "+read,
        shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    rmdir("disable")
    mkdir("enable")
    return "enable"


def disable_touch():
    '''禁用触摸屏'''
    run(".\devcon.exe>nul 2>nul disable "+read,
        shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    rmdir("enable")
    mkdir("disable")
    return "disable"


HWND_BROADCAST = 0xffff
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MonitorPowerOff = 2
SW_SHOW = 5


def screenOff():
    '''息屏'''
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                               SC_MONITORPOWER, MonitorPowerOff)
    shell32 = windll.LoadLibrary("shell32.dll")
    shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                          'USER32', '', SW_SHOW)
