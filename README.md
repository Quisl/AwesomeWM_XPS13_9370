# Introduction

This repository describes how I set up my Dell XPS 13 9370 using the Awesome WM 4.3-4. However this should also run on any 4.x version of Awesome.

I run Linux via Debian 10 bullseye (testing). You can still use this if you run a different distribution. However I will only 

# Setup

## Prerequisites

I will quickly go through every additional tool and describe how I made it run and what I used it for.

### Gnome & gdm3

I installed Debian 10 from the ISO which comes with Gnome. I used the unofficial unfree version (https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/10.2.0+nonfree/amd64/iso-cd/) because these include the required WIFI drivers for the XPS 13. Luckily Gnome includes the login manager gdm3 so I just sticked with this. 

I recommend keeping Gnome (or an other big window manager) installed as a backup even if you don't use it. This is because the Awesome community isn't as big and therefore you might run into compability problems (i.e. using software that is made for a specific WM, holding a presentation with exotic hardware etc.). Theoretically everything can  be done with Awesome, but sadly some things are not plug and play.

### Sudo

Don't do too many things as root. Use sudo instead. You can add your user to the sudo group like this (quisl is my username):
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
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
```

Make sure you update and upgrade apt after this in order to switch to the testing branch of Debian:
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

TODO: Appears not to work completly?

```
sudo apt-get install xfce4-power-manager
```
# How to use this

To check all available hotkeys press [Windows Key] + [s]

# Pre setup

