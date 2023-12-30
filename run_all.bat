@echo off

REM Check if the .venv directory exists
if not exist .venv (
    REM Create a virtual environment
    python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate

REM Check if the first command line argument is "reinstall"
if "%~1"=="reinstall" (
    REM Install the build module
    python -m pip install build

    REM Install the required packages
    python -m pip install -r rdna3emu.egg-info\requires.txt

    REM Remove the old package
    del /Q dist\*.whl

    REM Build the package
    python -m build

    REM Uninstall the old package if any
    python -m pip uninstall -y rdna3emu

    REM Install the package using installer
    python -m pip install installer
    for %%f in (dist\*.whl) do (
        python -m installer %%f
    )
)

REM Run all the tests
python -m unittest rdna3emu\test_all.py

REM Deactivate the virtual environment
deactivate