#!/bin/bash

# Color variables
Green='\033[0;32m'
Cyan='\033[0;36m'
Yellow='\033[0;33m'
Reset='\033[0m'

# Function to calculate elapsed time
function timer() {
    if [[ $# -eq 0 ]]; then
        echo $(date '+%s')
    else
        local stime=$1
        etime=$(date '+%s')

        if [[ -z "$stime" ]]; then stime=$etime; fi

        dt=$((etime - stime))
        ds=$((dt % 60))
        dm=$(((dt / 60) % 60))
        dh=$((dt / 3600))
        printf "\033[0;33mTotal time: %d:%02d:%02d\033[0m\n" $dh $dm $ds
    fi
}

start=$(timer)

# Update and Upgrade
echo -e "${Cyan}Updating and upgrading your system...${Reset}"
sudo apt-get update && sudo apt-get upgrade -y
echo -e "${Green}Update and upgrade completed!${Reset}"
timer $start

# Function to check installation status
function check_install() {
    package=$1
    if ! dpkg -s "$package" &> /dev/null; then
        echo -e "${Yellow}$package is not installed. Installing now...${Reset}"
        sudo apt-get install -y $package
    else
        echo -e "${Green}$package is already installed.${Reset}"
    fi
}

# Install web browsers
echo -e "${Cyan}Checking and installing web browsers...${Reset}"
segment_start=$(timer)
check_install firefox

# Install Google Chrome
if ! dpkg -s google-chrome-stable &> /dev/null; then
    echo -e "${Yellow}Google Chrome is not installed. Installing now...${Reset}"
    wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install -y ./chrome.deb
    rm chrome.deb
    # Add Google Chrome to the dock
    gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed -e "s/]/, 'google-chrome.desktop']/")"
else
    echo -e "${Green}Google Chrome is already installed.${Reset}"
fi
timer $segment_start

# Install office suite
echo -e "${Cyan}Checking and installing LibreOffice...${Reset}"
segment_start=$(timer)
check_install libreoffice
timer $segment_start

# Install media players
echo -e "${Cyan}Checking and installing VLC and Spotify...${Reset}"
segment_start=$(timer)
check_install vlc
sudo snap install spotify --classic
timer $segment_start

# Install programming languages
echo -e "${Cyan}Checking and installing Java, Python, and Dart...${Reset}"
segment_start=$(timer)
check_install default-jdk
check_install python3
sudo apt-get install dart
# Dart may require additional setup, depending on Ubuntu version
timer $segment_start

# Install development tools
echo -e "${Cyan}Checking and installing build essentials, Git, and PyCharm Community Edition...${Reset}"
segment_start=$(timer)
check_install build-essential
check_install git
sudo snap install pycharm-community --classic
timer $segment_start

# Install text editors
echo -e "${Cyan}Checking and installing Vim and Visual Studio Code...${Reset}"
segment_start=$(timer)
check_install vim
sudo snap install code --classic
timer $segment_start

# Install IDEs
echo -e "${Cyan}Checking and installing IntelliJ IDEA Ultimate and Android Studio...${Reset}"
segment_start=$(timer)
sudo snap install intellij-idea-ultimate --classic
sudo snap install android-studio --classic
timer $segment_start

# Install communication tools
echo -e "${Cyan}Checking and installing Slack, Zoom, Thunderbird, Microsoft Teams, and Discord...${Reset}"
segment_start=$(timer)
sudo snap install slack --classic
sudo snap install zoom-client
check_install thunderbird
sudo snap install teams
sudo snap install discord
timer $segment_start

# Install remote support tools
echo -e "${Cyan}Checking and installing TeamViewer and Chrome Remote Desktop...${Reset}"
segment_start=$(timer)
# Specific checks for .deb packages
wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
sudo apt install -y ./teamviewer_amd64.deb
rm teamviewer_amd64.deb
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
sudo apt install -y ./chrome-remote-desktop_current_amd64.deb
rm chrome-remote-desktop_current_amd64.deb
timer $segment_start

# Install system monitoring tools
echo -e "${Cyan}Checking and installing htop, net-tools, and nload...${Reset}"
segment_start=$(timer)
check_install htop
check_install net-tools
check_install nload
timer $segment_start

# Install backup tools
echo -e "${Cyan}Checking and installing Timeshift...${Reset}"
segment_start=$(timer)
check_install timeshift
timer $segment_start

# Install Virtualization tools
echo -e "${Cyan}Checking and installing Oracle VirtualBox...${Reset}"
segment_start=$(timer)
echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
sudo apt-get update
check_install virtualbox-6.1
timer $segment_start

# Additional utilities
echo -e "${Cyan}Checking and installing curl, wget, and unzip...${Reset}"
segment_start=$(timer)
check_install curl
check_install wget
check_install unzip
timer $segment_start

# Cleaning up
echo -e "${Cyan}Cleaning up...${Reset}"
segment_start=$(timer)
sudo apt-get autoremove -y
echo -e "${Green}Clean up completed!${Reset}"
timer $segment_start

# Finish
total_time=$(timer $start)
echo -e "${Green}Installation complete! Total elapsed time: $total_time${Reset}"
