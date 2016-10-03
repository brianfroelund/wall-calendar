## Wall calendar software setup

#### Remove Curser
sudo apt-get install unclutter

#### Prevent sleep

> sudo nano /etc/lightdm/lightdm.conf

find the following line:

> \#xserver-command=X

and change it into:

> xserver-command=X -s 0 –dpms

#### Chromium setup
> ~/.config/chromium/Default/User StyleSheets/Custom.css

> sudo nano ~/.config/lxsession/LXDE-pi/autostart 
> @chromium-browser --kiosk  calendar.google.com/calendar/render#main_7|custom,28

#### Launch monitor controller at startup
> crontab -e

Insert 

> @reboot sh /home/pi/launcher.sh >/dev/null 2>&1
