#!/bin/bash
# an install file that:
# 1. creates a terminal alias
# 2. installs python dependencies
# 3. sets app as a start-up process

# 1. Create a terminal alias in .bashrc
echo "alias zoom-lens='python3 ~/zoom-lens/main.py &'" >> ~/.bashrc

# 2. Install python dependencies
sudo apt install libgirepository1.0-dev
pip install -r requirements.txt

# 3. set up as start-up process
# get username 
name=$(whoami)
#build the .desktop file
cd ~/.config/autostart/
cat <<EOT >> zoom-lens.desktop
[Desktop Entry]
Type=Application
Path=/home/$name/zoom-lens/
Exec=python3 main.py
Terminal=false
Icon=htop
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=zoom-lens
Comment[en_US]=runs zoom-lens
EOT

