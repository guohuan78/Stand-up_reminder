# 站立提醒 (Stand Up Reminder)

这是一个简单的站立提醒应用程序，每隔一段时间提醒你站起来活动一下。

## 功能

- 每隔30分钟弹出一个消息框提醒你站起来活动。
- 在系统托盘中显示一个图标，可以通过右键菜单退出程序。

## 使用

### 下载

release中下载Stand-up_reminder.exe

### 开机自启

[在 Windows 10 中添加在启动时自动运行的应用 - Microsoft 支持](https://support.microsoft.com/zh-cn/windows/%E5%9C%A8-windows-10-%E4%B8%AD%E6%B7%BB%E5%8A%A0%E5%9C%A8%E5%90%AF%E5%8A%A8%E6%97%B6%E8%87%AA%E5%8A%A8%E8%BF%90%E8%A1%8C%E7%9A%84%E5%BA%94%E7%94%A8-150da165-dcd9-7230-517b-cf3c295d89dd)

1. 按 Windows 徽标键+  **R** ，键入“ **shell:startup** ”，然后选择“ **确定** ”。这将打开“ **启动** ”文件夹。
2. 右键该应用，选择“创建快捷方式”，并粘贴到 **“启动”** 文件夹中。

## 开发

### 依赖库

- Python 3.x
- tkinter
- pystray
- Pillow (PIL)

### 打包软件

使用`pyinstaller`，可用pip安装：

```bash
pip install pyinstaller
```

```bash
pyinstaller -F -w Stand-up_reminder.py
```