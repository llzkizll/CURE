import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog='cure.py',
        description='Package a local Python script as a Windows executable.',
    )
    parser.add_argument('script', type=Path, help='Path to the Python script to package')
    args = parser.parse_args()

    script = args.script.resolve()
    if script.suffix.lower() != '.py' or not script.is_file():
        parser.error(f'Expected an existing .py file: {args.script}')
    if sys.platform != 'win32':
        parser.error('Build the Windows executable on Windows.')

    build = subprocess.run(
        [sys.executable, '-m', 'PyInstaller', '--onefile', str(script)],
        check=False,
    )
    return build.returncode


if __name__ == '__main__':
    sys.exit(main())
