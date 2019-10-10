#!/usr/bin/env sh

if [ -e /bin/env ]
then
	echo "... /bin/env found."
else
	sudo ln -s /usr/bin/env /bin/env
fi

sudo apt update

sudo apt-get install libxcb1-dev libxcb-keysyms1-dev libpango1.0-dev libxcb-composite0-dev libxcb-util0-dev libxcb-icccm4-dev libyajl-dev libstartup-notification0-dev libxcb-randr0-dev libev-dev libxcb-cursor-dev libxcb-xinerama0-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev autoconf xutils-dev dh-autoreconf unzip git -y

git clone --recursive https://github.com/Airblader/xcb-util-xrm.git
cd xcb-util-xrm/
./autogen.sh
make
sudo make install
cd ..
rm -fr xcb-util-xrm


sudo ldconfig
sudo ldconfig -p

git clone https://www.github.com/Airblader/i3 i3-gaps
cd i3-gaps
autoreconf --force --install
rm -Rf build/
mkdir build
cd build/
 ../configure --prefix=/usr --sysconfdir=/etc --disable-sanitizers
 make
 sudo make install
# which i3
# ls -l /usr/bin/i3
cd ../..
rm -fr i3-gaps


sudo apt install git nitrogen rofi python-pip binutils gcc make pkg-config fakeroot cmake python-xcbgen xcb-proto libxcb-ewmh-dev wireless-tools libiw-dev libasound2-dev libpulse-dev libcurl4-openssl-dev libmpdclient-dev -y

export PYTHONDONTWRITEBYTECODE=1
sudo -H pip install -r requirements.txt

[ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
mkdir fonts
cd fonts
wget https://use.fontawesome.com/releases/v5.0.13/fontawesome-free-5.0.13.zip
unzip fontawesome-free-5.0.13.zip
cd fontawesome-free-5.0.13
sudo cp use-on-desktop/* /usr/share/fonts
sudo fc-cache -f -v
cd ../..
rm -fr fonts

git clone https://github.com/jaagr/polybar
cd polybar
USE_GCC=ON ENABLE_I3=ON ENABLE_ALSA=ON ENABLE_PULSEAUDIO=ON ENABLE_NETWORK=ON ENABLE_MPD=ON ENABLE_CURL=ON ENABLE_IPC_MSG=ON INSTALL=OFF INSTALL_CONF=OFF ./build.sh -f
cd build
sudo make install
make userconfig
cd ../..
rm -fr polybar

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
				mkdir $HOME/.config/nitrogen
        touch $HOME/.config/nitrogen/bg-saved.cfg
fi

if [ -e $HOME/.config/polybar/config ]
then
        echo "... polybar/config found."
else
				mkdir $HOME/.config/polybar
        touch $HOME/.config/polybar/config
fi

if [ -e $HOME/.config/i3/config ]
then
        echo "... i3/config found."
else
				mkdir $HOME/.config/i3
        touch $HOME/.config/i3/config
fi
