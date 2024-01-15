import os
import time
ENV_NAME = ".env"
# 'nt' is windows and everything else is mac/unix/linux and they have all the same paths (thank god)
PIP_ENV_PATH = f".\{ENV_NAME}\Scripts\pip.exe" if os.name == "nt" else f"./{ENV_NAME}/bin/pip3"
PYTHON_ENV_PATH = f".\{ENV_NAME}\Scripts\python.exe" if os.name == "nt" else f"./{ENV_NAME}/bin/python3"
CREATE_ENV_COMMAND = f"virtualenv {ENV_NAME}" if os.name == "nt" else f"python3 -m venv {ENV_NAME}"

requirements = ["pynput"]

def main():
    if ENV_NAME not in os.listdir():
        print("installing virtualenvirement...")
        os.system(CREATE_ENV_COMMAND)
        print("virtualenevirement installed!")
        os.system(f"{PIP_ENV_PATH} install {''.join(requirements)}")
        print("installed dependencies!")
        print("running macro.py")
        os.system(f"{PYTHON_ENV_PATH} macro.py")
        return
    else:
        print("env found!")
    for requirement in requirements:
        if requirement not in os.popen(f"{PIP_ENV_PATH} list").read():
            print(f"found missing requirement: {requirement}")
            print(f"installing {requirement}..")
            os.system(f"{PIP_ENV_PATH} install {requirement}")
            print(f"installed {requirement}!")

    print("running macro.py!")
    os.system(f"{PYTHON_ENV_PATH} macro.py")

if __name__ == "__main__":
    main()