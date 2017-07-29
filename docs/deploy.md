# Deploying the Entire Setup
This guide assumes that you want to completely reset the honeypot
network, and start fresh. This is NOT for reactivating the camp setup,
this is for completely resetting everything.

## Part One: Setting up the MHN Mangement Server
1. In the EC2 management dashboard, create a new EC2 instance running
   Ubuntu 14.04- MHN will *only* run on Ubuntu 14.04.- 
- When asked about networking settings, select "Allow all traffic". This
  allows for SSH and webserver connections
- When asked for the SSH key, select "honeypots". You should already
  have the honeypots.pem file required for SSH connections

2. Install the MHN server by following the [MHN Install
   Guide](https://github.com/threatstream/mhn)

## Part Two: Adding Sensors to MHN
1. Begin by creating as many EC2 instances as necessary. Ubuntu 16.04
   can be used here, in addition to 14.04
- As before, ensure that "Allow all traffic" is the selected security
  setting, and honeypots.pem is the chosen ssh key file

2. On the MHN management website, go to the "deploy" tab, and select the
   appropriate honeypot. To recreate the original setup, select "snort"
as the chosen honeypot

3. Copy the script to the clipboard, then SSH into the chosen honeypot
   EC2 instance. This will act as one of the MHN sensors. Run the script

4. The script should automatically register the sensor with MHN. Head to
   the "Sensors" tab in the MHN interface to verify that it was added

5. Repeat for as many as sensors as necessary

## Part Three: Deploy Camp UI
NOTE: The Camp UI is not flexible enough to work right outside of the
box- some configuration is required. At the time of writing, manually
editing several files in the project is necessary

1. Clone the github repo at github.com/pcodes/mhn_inerface

2. Edit the file honeypots/views.py
- In the MHN sensors tab of the management site, take note of the UUID
  of each sensor
- Modify the UUID list in team_attacks() and
  team_stats() to contain the UUIDs of all of your sensors- index 0 in
this list represents team 1, index 1 is team 2, etc.

3. Edit the file mhn_interface/templates/base.html
- Unfortunately the team links for the tabs of the interface are
  hard-coded
- This means that in the "navbar links" section of the html file, you
  need as many sections as there are teams- copy the style of the
default tabs

4. Copy the .env file into the root directory of the github repo
- This file contains secrets for the entire project- do *not* let this
  into version control at any time

5. Edit the .env file to fit your setup
- You need to obtain your MHN API by going to the "account" tab in the
  MHN management interface

6. Edit the file config/settings/base.py
- At the bottom of the file, change the IP address to match the one of
  your MHN management server (but *keep* the rest of the URL)

7. Install Docker by following the [Docker Install Guide for
   Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository)

8. Run ```sudo apt-get install docker-compose -y```

9. Finally, to launch the django server, run ```docker-compose up -d```

