# Check Notepad Files for the Number 13

import os
import win32gui
import win32process

def get_open_notepad_files():
    notepad_files = []
    def enum_windows(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            if win32gui.GetWindowText(hwnd) and 'Notepad' in win32gui.GetWindowText(hwnd):
                notepad_files.append(hwnd)
    win32gui.EnumWindows(enum_windows, None)
    return notepad_files

def check_number_in_notepad():
    notepad_files = get_open_notepad_files()
    for hwnd in notepad_files:
        win32gui.ShowWindow(hwnd, 5)  # Restore the window if minimized
        win32gui.SetForegroundWindow(hwnd)
        text = win32gui.GetWindowText(hwnd)
        if '13' in text:
            print("Yes, it is equal to 13")
        else:
            print("No, it is not equal to 13")

if __name__ == "__main__":
    check_number_in_notepad()
