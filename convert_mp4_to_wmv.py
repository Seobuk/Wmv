import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def select_file():
    path = filedialog.askopenfilename(
        filetypes=[('MP4 files', '*.mp4')])
    if path:
        file_var.set(path)


def convert_video():
    src = file_var.get()
    if not src:
        messagebox.showerror('Error', 'Please select an MP4 file')
        return

    dst = os.path.splitext(src)[0] + '.wmv'
    cmd = ['ffmpeg', '-i', src, dst]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        messagebox.showinfo('Done', f'Created {dst}')
    else:
        messagebox.showerror('Error', f'Failed to convert {src}\n{result.stderr.decode()}')


def build_gui(root):
    root.title('MP4 to WMV Converter')

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text='MP4 File:').grid(row=0, column=0, sticky=tk.W)
    entry = tk.Entry(frame, textvariable=file_var, width=40)
    entry.grid(row=0, column=1, padx=5)
    tk.Button(frame, text='Browse', command=select_file).grid(row=0, column=2)

    tk.Button(frame, text='Convert', command=convert_video).grid(row=1, column=1, pady=10)

    root.mainloop()


def main():
    root = tk.Tk()
    global file_var
    file_var = tk.StringVar(master=root)
    build_gui(root)


if __name__ == '__main__':
    main()
