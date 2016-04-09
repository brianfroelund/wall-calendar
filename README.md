Remove Curser
sudo apt-get install unclutter

Prevent sleep
sudo nano /etc/lightdm/lightdm.conf
xserver-command=X -s 0 –dpms

Chromium setup
sudo apt-get install chromium 
~/.config/chromium/Default/User StyleSheets/Custom.css

sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
@chromium --noerrdialogs --kiosk --homepage 'https://www.google.com/calendar/render#h%7Cmonth'
@sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium/Default/Preferences