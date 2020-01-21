# Introduction

This repository describes how I set up my Dell XPS 13 9370 using the Awesome WM 4.3-4. However this should also run on any 4.x version of Awesome.

I run Linux via Debian 10 bullseye (testing). You can still use this if you run a different distribution. However many commands will only work on Debian (and probably Ubuntu).

# Setup

## Prerequisites

I will quickly go through every additional tool and describe how I made it run and what I used it for.

### Basis installation (Debian & Gnome & gdm3)

I installed Debian 10 from the ISO which comes with Gnome. I used the unofficial unfree version (https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/10.2.0+nonfree/amd64/iso-cd/) because these include the required WIFI drivers for the XPS 13. Luckily Gnome includes gdm3 as login manager so I just sticked with it. 

I recommend keeping Gnome (or an other big window manager) installed as a backup even if you don't use it. This is because the Awesome community isn't as big and therefore you might run into compability problems (i.e. using software that is made for a specific WM, holding a presentation with exotic hardware etc.). Theoretically everything can  be done with Awesome, but sadly some things are not plug and play.

### Sudo

Don't do too many things as root. Use sudo instead! You can add your user to the sudo group like this (quisl is my username):
```
# adduser quisl sudo
```

### Sources list
Since we want Debian testing delete the default entries in /etc/apt/sources.list and copypaste the following:

```
#------------------------------------------------------------------------------#
#                   OFFICIAL DEBIAN REPOS                    
#------------------------------------------------------------------------------#

###### Debian Main Repos
deb http://deb.debian.org/debian/ testing main contrib non-free
deb-src http://deb.debian.org/debian/ testing main contrib non-free

deb http://deb.debian.org/debian/ testing-updates main contrib non-free
deb-src http://deb.debian.org/debian/ testing-updates main contrib non-free

deb http://deb.debian.org/debian-security testing-security main
deb-src http://deb.debian.org/debian-security testing-security main

#-------------------------------------------------------------------------------#
#                      UNOFFICIAL  REPOS                       
#------------------------------------------------------------------------------#

###### 3rd Party Binary Repos
###Visual Studio Code
deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main
```

If you do not need Visual Studio Code or you don't trust Microsoft you can remove unofficial repos part in the end. If you keep it you will need to tell Debian to trust it:

```
sudo apt-get install curl
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
```

Make sure you update and upgrade apt after this in order to complete the switch to the testing branch of Debian:
```
sudo apt-get update && sudo apt-get dist-upgrade
```

### Graphical text editor: Visual studio code

This is the code editor that I use, it also functions as an IDE. To install it type this:

```
sudo apt-get install apt-transport-https
sudo apt-get install code # or code-insiders
```

### Terminal text editor: vim

Vim is awesome. Thats why I use Vim in Awesome. Install it like this:
```
sudo apt-get install vim
```

### Power Manager Widget: xfce4-power-manager
I used to use a battery widget that was made for Awesome. However nowadays I found that the xfce4-power-manager just gives me more features. It can also control brightness and other power saving tricks.


```
sudo apt-get install xfce4-power-manager
```
TODO: Appears not to work completly?

### Bluetooth applet: blueman

Allows to handle bluetooth devices:
```
sudo apt-get install blueman
```

### Korean language support

Feel free to skip this step. ;)
```
sudo apt-get install ibus-hangul
sudo apt-get install korean*
```

### Screen locker: xsecurelock
I use xsecurelock to lock my screen. It will be bound to [ctrl]+[l].

```
sudo apt-get install xsecurelock
```

### Network Manager: nm-applet

We do not need to install this, it comes with Debian.

### Audio

I use pasystray as audio manager.

sudo apt-get install pasystray
sudo apt-get install pavucontrol

### Terminal misc...

```
sudo apt-get install screenfetch
sudo apt-get install lolcat
```

### Fix resolution scaling

If you use the HDTV (resolution 1920 x 1080) version of the XPS 13 you can skip this step. However if you have the 4k/Ultra HD display (resolution 3840x2160) you will need to tell the Xserver to scale things. Otherwise text might be very small. Edit the file ~/.Xresources and add a "Xft.dpi" setting. I found 330 is a good value. Feel free to experiment:
```
Xft.dpi:330
```

Now since some tools prefer the GDK settings over the X settings we also need to setup these. We do that with the GDK_SCALE environment variable. For this kind of software we should also set the GDK_DPI_SCALE to undo the dpi setting that we set earlier.
Edit the file ~/.profile
```
export GDK_SCALE=3
export GDK_DPI_SCALE=0.333333
```

# How to use this

To check all available hotkeys press [Windows Key] + [s]

# Pre setup

