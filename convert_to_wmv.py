import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

SUPPORTED_EXTENSIONS = {
    '.mp4', '.avi', '.mkv', '.mov', '.flv', '.webm', '.mpg', '.mpeg'
}


def select_directory():
    path = filedialog.askdirectory()
    if path:
        directory_var.set(path)


def convert_videos():
    directory = directory_var.get()
    if not directory:
        messagebox.showerror('Error', 'Please select a directory')
        return

    for root, _, files in os.walk(directory):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                src_path = os.path.join(root, name)
                dst_name = os.path.splitext(name)[0] + '.wmv'
                dst_path = os.path.join(root, dst_name)
                cmd = ['ffmpeg', '-i', src_path, dst_path]
                result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode != 0:
                    messagebox.showerror('Error', f'Failed to convert {src_path}\n{result.stderr.decode()}')
                    return
    messagebox.showinfo('Done', 'Conversion completed')


def build_gui(root):
    root.title('WMV Converter')

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text='Directory:').grid(row=0, column=0, sticky=tk.W)
    entry = tk.Entry(frame, textvariable=directory_var, width=40)
    entry.grid(row=0, column=1, padx=5)
    tk.Button(frame, text='Browse', command=select_directory).grid(row=0, column=2)

    tk.Button(frame, text='Convert', command=convert_videos).grid(row=1, column=1, pady=10)

    root.mainloop()


def main():
    root = tk.Tk()
    global directory_var
    directory_var = tk.StringVar(master=root)
    build_gui(root)


if __name__ == '__main__':
    main()
