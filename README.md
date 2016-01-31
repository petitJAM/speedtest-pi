# Speedtest on Pi

Run a speed test for my home network and log to file

## Crontab

Every 30 minutes, run the speed test:

    0,30 * * * * /home/pi/speedtest/speedtest.py

Some credit goes to: [/u/AlekseyP](https://www.reddit.com/r/technology/comments/43fi39/i_set_up_my_raspberry_pi_to_automatically_tweet/) and [Thomas Ahle](http://stackoverflow.com/a/22348885/1388245)
