# SNDBOX-MultiFile-Uploader
Upload multiple samples to the SNDBOX Malware analysis API. 

This uploader was created to upload samples captured by the Dionaea and Adbhoney pots installed with the TPot Framework (https://github.com/dtag-dev-sec/tpotce) This Framework deploys a range of honeypots targeted to capture and analyse traffic. The two honeypots, Dionaea and Adbhoney also capture Malware samples.

Combining this script with a cron job, all samples for each day will be checked against SNDBOX (https://app.sndbox.com) and will upload the samples if required.

To operate the Uploader, follow the instructions:

Clone this Repo: 

    git clone https://github.com/PR3R00T/SNDBOX-MultiFile-Uploader.git

You will need a Free SNDBOX account (https://app.sndbox.com/register) Once completed navigate to the User Settings -> API key and copy the key. 2.Place the key into the variable: apikey in the SNDBOXupload.py script. (nano SNDBOXupload.py)

3.Install the Requirements.txt: 

    pip3 install -r Requirements.txt

4.Give the file execute permissions: 

    chmod +x SNDBOXupload.py

5.run the script: 

    ./SNDBOXupload.py

Log files are created within: /data/ folder if any issues occur, check the SNDBOXuploaderror log.

If you would like to automate this script add a cron job:

 launch crontab with: crontab -e

 append to the end (change the times if required):

m h dom mon dow command

20 2 * * * /full/path/to/SNDBOX-MultiFile-Uploader/SNDBOXupload.py
