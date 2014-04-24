##Hacking productivity with cron jobs

+ Clone this repo.
+ Copy your current /etc/hosts file into template.txt. This is the file which will periodically be restored as your /etc/hosts by crontab.
+ Add the following line in sodo's crontab '*/5 * * * python /path/to/repo/main.py' , choose the cron tab time to suit your needs.
+ Now every 5 minutes, the crontab is going to restore your /etc/hosts file as your specified in the template.txt file, so everytime you get the itch, you will have to edit your hosts file every 5 minutes, which should be enough to discourage you to atttend to it.


###TODO
+ Save template.txt in unreadable format.