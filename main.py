# # ! F:\软件\WPy64-31140\python-3.11.4.amd64\python.exe
# -*- encoding: utf-8 -*-
from os import path, mkdir, rmdir
from keyboard import is_pressed
import pystray
from PIL import Image
from threading import Thread
from time import time, sleep
from tkinter import Tk
from tkinter.messagebox import showerror, showinfo, showwarning, ERROR, INFO, WARNING
# from func_timeout import func_set_timeout
from subprocess import run, PIPE
from screen import *

# 删除enable文件夹
if path.isdir(".\\enable") == True:
    rmdir(".\\enable")
# 建立disable文件夹
if path.isdir(".\\disable") == False:
    mkdir(".\\disable")

enable_touch()  # 防止禁用触摸屏后程序异常退出导致无法启用触摸屏,在程序开始运行时先启用触摸屏

img = Image.open("img.png")  # 托盘图标
# 托盘菜单
menu = (
    pystray.MenuItem("结束希沃软件", lambda: kill()),
    pystray.MenuItem("暂停/恢复", lambda: hang_on_or_continue()),
    pystray.MenuItem("Exit", lambda: run(
        "taskkill>nul 2>nul /T /F /IM XWToolkit.exe", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE))
)
icon = pystray.Icon("name", img, "XWToolkit\n运行中", menu)


# 要结束的进程列表
kill_list = ["EasiNote.exe", "EasiCamera.exe", "PhotosApp.exe",
             "wps.exe", "wpp.exe", "wpsoffice.exe", "msedge.exe"]


def kill():
    '''结束进程'''
    for i in kill_list:
        run("taskkill>nul 2>nul /T /F /IM "+i, shell=True, stdin=PIPE,
            stdout=PIPE, stderr=PIPE)


def showMessageBox(message, type, timeout):
    '''
    显示弹窗
    message:要展示的信息
    type:弹窗类型(提示,警告或错误)
    timeout:显示时间(单位:毫秒)
    '''
    root = Tk()
    root.withdraw()
    try:
        root.after(timeout, root.destroy)
        if type == "info":
            showinfo(
                '提示', message, master=root, icon=INFO)
        elif type == "warning":
            showwarning(
                '警告', message, master=root, icon=WARNING)
        elif type == "error":
            showerror(
                '错误', message, master=root, icon=ERROR)
    except:
        pass


def execute():
    '''获取按键并执行对应操作'''
    # 结束进程
    if is_pressed("up") == True:
        kill()
        showMessageBox("操作已完成", "info", 1000)
        return True
    # 结束进程并息屏
    elif is_pressed("down") == True:
        kill()
        screenOff()
        showMessageBox("操作已完成", "info", 1000)
        return True
    # 关机
    elif is_pressed("b") == True:
        run("shutdown -p", shell=True, stdin=PIPE,
            stdout=PIPE, stderr=PIPE)  # 关机
        showMessageBox("操作已完成", "info", 1000)
        return True
    # 禁用/启用触摸屏
    elif is_pressed("esc") == True:
        # 判断目前触摸屏状态
        if path.isdir("enable") == True:
            disable_touch()  # 禁用触摸屏
            return "disable"
        elif path.isdir("disable") == True:
            enable_touch()  # 启用触摸屏
            return "enable"
    else:
        pass


def main():
    while True:
        if is_pressed('esc') == True:
            showMessageBox("已进入Esc监听模式\n请在2秒后按下操作按键", "info", 2000)
            start_time = time()  # 获取开始监听时的时间
            returns = []
            target_time = start_time + 6  # 设置停止时间为开始时间的6秒后
            while True:
                current_time = time()  # 获取现在时间
                # 如果现在时间大于等于结束时间,跳出循环并提示
                if current_time >= target_time:
                    showMessageBox("未在指定时间内按下控制键", "warning", 1000)
                    break
                returns.append(execute())
                # 判断所执行的操作,并提示
                if "disable" in returns:
                    showMessageBox("已成功禁用触摸屏", "info", 1000)
                    break
                elif "enable" in returns:
                    showMessageBox("已成功启用触摸屏", "info", 1000)
                    break
                elif True in returns:
                    break
            if "disable" or "enable" in returns:
                pass
                continue


def hang_on_or_continue():
    pass


t_tray = Thread(target=icon.run)  # 托盘线程
t_main = Thread(target=main)  # 主线程

if __name__ == "__main__":
    try:
        t_tray.start()  # 启动托盘线程
        t_main.start()  # 启动主线程
    except AttributeError:
        pass
