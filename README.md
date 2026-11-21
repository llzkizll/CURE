<h1 align="center">
  <img src="./assets/cure-planet.gif" width="900" alt="CURE by ZKIZ">
</h1>

<p align="center">A command-line tool for packaging local Python scripts as Windows executables.</p>

<p align="center">
  <a href="https://github.com/llzkizll"><img src="./assets/github.png" height="34" alt="ZKIZ on GitHub"></a>
  &nbsp;
  <img src="./assets/windows.png" height="34" alt="Windows">
</p>

## Quick start

Open PowerShell in the repository folder on Windows. Install the dependencies and pass the path to a local Python script.

```powershell
python -m pip install -r requirements.txt
python cure.py "C:\path\to\your-script.py"
```

The executable is written to `dist/your-script.exe` under your current working directory. PyInstaller also creates a `build/` directory and a `.spec` file during packaging.

## Example

For a file called `hello.py` in the current directory, `python cure.py hello.py` builds `dist/hello.exe`.

Install any packages your input script imports in the same Python environment before building. [PyInstaller documentation](https://pyinstaller.org/en/stable/)

<p align="center">
  <img src="./assets/orbite.gif" width="900" alt="">
</p>
