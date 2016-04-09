Remove Curser
sudo apt-get install unclutter

Prevent sleep
sudo nano /etc/lightdm/lightdm.conf
xserver-command=X -s 0 –dpms

Chromium setup
sudo apt-get install chromium 
~/.config/chromium/Default/User StyleSheets/Custom.css

sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
@iceweasel



### Launch monitor controller at startup

> sudo crontab -e -u root

Insert 

> @reboot sh /home/pi/launcher.sh >/dev/null 2>&1 &
