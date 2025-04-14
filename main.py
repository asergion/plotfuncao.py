# plotfuncao.py
# main.py

import subprocess
import os
import sys

def main():
    caminho_app = os.path.join("View", "app_streamlit.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", caminho_app])

if __name__ == "__main__":
    main()