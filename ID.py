import wx
from os import path
from sys import exit


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="设置设备实例路径")

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(panel)
        sizer.Add(self.text, 0, wx.EXPAND | wx.ALL, 10)

        button = wx.Button(panel, label="确认")
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)
        self.Show()

    def on_button_click(self, event):
        input_text = self.text.GetValue()
        write_message = '"@'+input_text+'"'
        with open("ID.txt", "w") as f:
            f.write(write_message)
        wx.MessageBox("设备实例路径已配置完毕\n现在可以正常使用本程序", "提示",
                      wx.OK | wx.ICON_INFORMATION)
        exit()


app = wx.App()
frame = MyFrame()
app.MainLoop()
