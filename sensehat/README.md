## Display IP Address on Startup
Run this command to set sensehat at startup.

```bash
(crontab -l 2>/dev/null; echo "@reboot sleep 30 && curl -s https://raw.githubusercontent.com/binodmx/learn-raspberrypi/refs/heads/main/sensehat/display-ip.py | python") | crontab -u user -
```
