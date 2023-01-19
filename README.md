# ipy-mailer
*(eye - pie)*  
Python script to email yourself (or someone else) the IP address of your device.

This is just a small tangential project for SYSC 3010, Computer Systems Development Project, which is a course offered by Carleton University for 3rd year students enrolled in the Computer Systems Engineering program.

## Why did I make this?
Due to the number of devices connected to Carleton's CU-Wireless network, attempting to connect to the Raspberry Pi that was provided to students taking SYSC 3010 via ssh using the hostname of the device takes a very long time, and often times is unsuccessful. 

Connection to the RPi is much faster if the ip address is known ahead of time, however ip's are constantly being reassigned on a network as large as Carleton's.

In a previous semester, one of the TAs for the course created a script to display the ip address of the RPi on the provided Sense Hat. The problem with this approach is that I am both not that great at quickly reading scrolling numbers, I am also kind of impatient and did not want to have to slow down the scroll speed of the ip address across the Sense Hat.

And so ipy ( mailer) mailer was born 

## How to use

Start by following [this tutorial](https://bc-robotics.com/tutorials/sending-email-using-python-raspberry-pi/) up to and including step 4.

Be sure to copy down the app password that google generates for you.

Clone this repository to your Raspberry Pi (or I guess any linux device).
Paste the app password in [config.json](config.json) for the "app_pw" value.

Fill out the other values of the json file with all of your relevant information.

```
{
	"app_pw": "your app password",
	"sender": "your_sender_email@emailserver.com",
	"recipient": "your_recipient_email@emailserver.com",
	"sender_name": "<-",
	"recipient_name": "<-"
}
```

You can run this script in the terminal by running:
```
python /path-to-script/mailer.py
```

If you want this to happen every time the RPi reboots, run `crontab -e` in the terminal and add this line:
```
python /path-to-script/mailer.py &
```