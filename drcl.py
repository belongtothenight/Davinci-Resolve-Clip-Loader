# Import Pypl Library
from multiprocessing import Value
from tkinter import DISABLED
import pyautogui as ag
import keyboard as kb
import PySimpleGUI as sg
import webbrowser as wb
import sys
import time
import os
import subprocess
# Import Custom Library
import gui_layout as gl
import gui_event_handler as geh

global mf, vdp, adp, awp, cp, drpdp, lsp, lef, pn
mf = "drcl_1.py" # Main Filename
vdp = 'D:/Note_Database/YouTube/YT Database/YTD File Video/YTDFV Recording-Minecraft' # Video Directory Path
adp = 'D:/Note_Database/YouTube/YT Database/YTD File Audio/YTDFA YT Audio Library'
awp = 'https://studio.youtube.com/channel/UCwHILYLxBpkE5NbuoPO8Rcw/music' # Audio Website Path
cp = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s &' # Chrome Path 
drpdp = 'C:/Users/dachu/AppData/Roaming/Blackmagic Design/DaVinci Resolve/Support/Resolve Disk Database/Resolve Projects/Users/guest/Projects' # DaVinci Resolve Directory Path
drps1ec = 'exec(open("D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Davinci Resolve Clip Loader/script_1.py", encoding="utf-8").read())' # DaVinci Resolve Python Script 1 Execute Command
lsp = 0.1 # Loop Sleep Parameter
lef = False # Loop Execution Flag
pn = 1000 # Project Number

def make_window_1():
    layout = [
        [sg.Text("Start executing " + mf + "!")],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True, use_default_focus=False)
    return window

def make_window_2():
    layout = [
        [sg.Text("Choose a video file in local folder.")],
        [sg.Text("Video Directory: "), sg.Input(enable_events=True, key='FOLDER01', default_text=vdp), sg.FileBrowse(initial_folder=vdp)],
        [sg.Text(key='TEXT01')],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True)
    return window

def make_window_3():
    layout = [
        [sg.Text("Choose a audio file from Google Audio Library and download it.")],
        #[sg.Text("Opening " + awp + "...")],
        [sg.Text("Download Directory: " + adp)],
        [sg.Text("Audio Directory: "), sg.Input(enable_events=True, key='FOLDER02', default_text=adp), sg.FileBrowse(initial_folder=adp)],
        [sg.Text(key='TEXT02')],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True)
    return window

def make_window_4():
    layout = [
        [sg.Text("Type the DDMS Project Number like \'01\'")],
        [sg.Text("Check privous project at: "), sg.Input(drpdp, disabled=True, text_color='gray')],
        [sg.Input(key='INPUT01'), sg.Button('Confirm', key='BUTTON01')],
        [sg.Text(key='TEXT03')],
        [sg.HSeparator()],
        [sg.Text("Type 'n': Next")],
        [sg.Text("Type 'q': Quit")]
    ]
    window = sg.Window('DrCL Startup', layout, grab_anywhere=True, resizable=True, margins=(0,0), keep_on_top=True)
    return window

if __name__ == '__main__':
    os.system('cls')
    print("\n[LOG] Start executing " + mf + "......")

    # 0 Startup Window
    print("[LOG] Startup Window")
    window = make_window_1()
    while True:
        event, values = window.read(timeout=100)
        # GUI Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=975, y=567)
        lef = True
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False
    
    # 1.1 Choosing Video
    print("[LOG] Choosing Video")
    window = make_window_2()
    while True:
        event, values = window.read(timeout=100)
        # GUI Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=975, y=567)
        lef = True
        # Custom GUI Event Handling
        if event == 'FOLDER01':
            window['FOLDER01'].update(disabled=True)
            vdp = values['FOLDER01']
            print("[LOG] Selected Path: " + vdp)
            window['TEXT01'].update(value='Selected Path: ' + vdp)
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False

    # 1.2 Choosing Audio
    print("[LOG] Choosing Audio")
    wb.get(cp).open(awp)
    time.sleep(lsp * 10)
    
    # wb.register("wb", None, wb.BackgroundBrowser(cp))
    # wb.get("wb").open(awp)

    window = make_window_3()
    while True:
        event, values = window.read(timeout=100)
        # General Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=975, y=567)
            ag.dragTo(x=320, y= 186, duration=0.3, button='left')
        lef = True
        # Custom GUI Event Handling
        if event == 'FOLDER02':
            window['FOLDER02'].update(disabled=True)
            adp = values['FOLDER02']
            print("[LOG] Selected Path: " + adp)
            window['TEXT02'].update(value='Selected Path: ' + adp)
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End ennxecuting " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False
    for i in range(0, 2):
        os.system("TASKKILL /F /IM chrome.exe")

    # 2.1 Launch Davinci Resolve
    print("[LOG] Launch Davinci Resolve")
    kb.send('win+s')
    time.sleep(lsp*5)
    kb.write("Davinci")
    time.sleep(lsp*5)
    kb.send('enter')
    time.sleep(lsp*5)
    subprocess.Popen('explorer')
    window = make_window_4()
    while True:
        event, values = window.read(timeout=100)
        # General Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Focus on GUI
        if lef == False:
            ag.click(x=975, y=567)
        lef = True
        # Custom GUI Event Handling
        if event == 'BUTTON01':
            window['INPUT01'].update(disabled=True)
            pn = "DDMS" + values['INPUT01']
            print("[LOG] Clicked Confirm! New project name: " + pn)
            window['TEXT03'].update(value='New project name: ' + pn)
        # Keyboard Event Handling
        if kb.is_pressed('q'):
            print("[LOG] End ennxecuting " + mf + "......")
            sys.exit()
        if kb.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
    lef = False
    for i in range(0, 2):
        # os.system("TASKKILL /F /IM explorer.exe && start explorer.exe")
        pass
    while True:
        if ag.locateOnScreen('Untitled_Project.png') != None:
            ag.click(x=897, y=323, clicks=2)
            break
    while True:
        if ag.locateOnScreen('DaVinci_Resolve_Menu.png') != None:
            break
    time.sleep(lsp*5)
    ag.click(x=679, y=30)
    time.sleep(lsp)
    ag.click(x=687, y=527)
    time.sleep(lsp)
    ag.click(x=911, y=326)
    time.sleep(lsp)
    ag.typewrite(drps1ec)
    kb.send('enter')


    # End executing
    print("[LOG] End executing " + mf + "......\n")
    sys.exit(0)

'''
while True:
        event, values = window.read(timeout=100)
        # General Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            # print('============ Event = ', event, ' ==============')
            # print('-------- Values Dictionary (key=value) --------')
            # for key in values:
            #     print(key, ' = ',
            #     values[key])
            pass
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Custom GUI Event Handling
        # Keyboard Event Handling
        if keyboard.is_pressed('q'):
            print("[LOG] End executing " + mf + "......")
            sys.exit()
        if keyboard.is_pressed('n'):
            print("[LOG] next......")
            break
    window.close()
'''