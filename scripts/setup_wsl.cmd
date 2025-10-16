@echo off

REM Title: WSL Setup Script
REM Description: A script to setup Windows Subsystem for Linux (WSL) without errors.
REM Tested on: Windows 10 version 2004 and later, or Windows 11

REM Ensure the script is run as Administrator
whoami /groups | find "S-1-5-32-544" >nul || (
  echo Please run this script as Administrator.
  exit /b 1
)

REM Enable WSL feature
echo Enabling WSL...
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

REM Enable Virtual Machine Platform feature (required for WSL 2)
echo Enabling Virtual Machine Platform...
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

REM Set WSL to use version 2 as the default
wsl --set-default-version 2

REM Install a Linux distribution (default Ubuntu in this case)
REM You can replace "Ubuntu" with another distribution available in the Microsoft Store
echo Installing Ubuntu from the Microsoft Store...
start /wait explorer.exe ms-windows-store://pdp/?productid=9NBLGGH4MSV6

echo Please complete the installation of the Linux distribution from the Microsoft Store.
echo Once done, restart your system to finalize WSL setup.

echo WSL setup complete.
pause
