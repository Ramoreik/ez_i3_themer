#!/bin/env bash

sudo pacman -Syy
sudo pacman -S git nitrogen rofi python-pip ttf-font-awesome adobe-source-code-pro-fonts binutils gcc make pkg-config fakeroot python-yaml --noconfirm

if [ -x "$(command -v yay)" ]; then
    yay -S polybar-git ttf-nerd-fonts-symbols termite-git
elif [ -x "$(command -v trizen)" ]; then
    trizen -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v pikaur)" ]; then
    pikaur -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v pakku)" ]; then
    pakku -S polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v aura)" ]; then
    aura -SA polybar-git ttf-nerd-fonts-symbols
elif [ -x "$(command -v pacaur)" ]; then
    pacaur -S polybar-git ttf-nerd-fonts-symbols
else
    echo "No common AUR Helpers found!"
    echo "This script requires an AUR Helper to install the following packages: polybar-git ttf-nerd-fonts-symbols"
    echo "Please install an AUR helper and try again"
    exit 1
fi


if [ -e $HOME/.config/termite/config ]
then
        echo "... .termite config found."
else
        mkdir -p $HOME/.config/termite
        touch $HOME/.config/termite/config
fi

if [ -e $HOME/.Xresources ]
then
        echo "... .Xresources found."
else
        touch $HOME/.Xresources
fi

if [ -e $HOME/.config/nitrogen/bg-saved.cfg ]
then
        echo "... .bg-saved.cfg found."
else
        mkdir -p $HOME/.config/nitrogen
        touch $HOME/.config/nitrogen/bg-saved.cfg
fi

if [ -e $HOME/.config/polybar/config ]
then
        echo "... polybar/config found."
else
        mkdir -p $HOME/.config/polybar
        touch $HOME/.config/polybar/config
fi

if [ -e $HOME/.config/i3/config ]
then
        echo "... i3/config found."
else
        mkdir -p $HOME/.config/i3
        touch $HOME/.config/i3/config
fi
