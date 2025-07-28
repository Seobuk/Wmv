# WMV Converter

A simple Tkinter-based GUI application to convert video files to WMV format.

## Requirements

- Python 3
- `ffmpeg` command line tool (must be accessible in your PATH)
- [Optional] `pyinstaller` if you want to build a Windows executable.

## Usage

1. Install ffmpeg on your system.
2. Run the application:
   ```bash
   python convert_to_wmv.py
   ```
3. Choose the directory containing video files and click **Convert**. All
   supported videos in the directory (and its subdirectories) will be converted
   to `.wmv` files using ffmpeg.

Supported input extensions include `mp4`, `avi`, `mkv`, `mov`, `flv`, `webm`,
`mpg`, and `mpeg`.

## Building an EXE (Windows)

If you want to distribute the program as a standalone executable on Windows,
install `pyinstaller` and run:

```bash
pyinstaller --onefile convert_to_wmv.py
```

The generated executable will appear in the `dist` directory.
