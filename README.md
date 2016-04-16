## Wall calendar software setup

#### Remove Curser
sudo apt-get install unclutter

#### Prevent sleep

> sudo nano /etc/lightdm/lightdm.conf

find the following line:

> \#xserver-command=X

and change it into:

> xserver-command=X -s 0 –dpms

#### Iceweasel setup
> ~/.config/chromium/Default/User StyleSheets/Custom.css

> sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
> @iceweasel

#### Launch monitor controller at startup
> crontab -e

Insert 

> @reboot sh /home/pi/launcher.sh >/dev/null 2>&1
