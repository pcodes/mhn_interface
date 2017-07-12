#Instructions for Honeypot Redeployment
Due to the nature of AWS, redeploying the honeypots is relatively
simple.

## Part One- Activating the EC2 Instances
1. Navigate to the EC2 Instance dashboard
2. Check all of the instances listed, then go to Actions-> Instance
   State-> Start
3. Once all of the machines have the green "running" status in the
   "Instance State" column, you're good to go.

## Part Two- Initializing the Docker Server
1. Using the honeypots.pem file, ssh to the IP Address listed for the
   "MHN Server UI".
2. ```cd mhn_interface```
3. ```docker-compose up -d```
4. Assuming this command does not produce any errors, the custom team UI
   should be running at the IP address used for SSH
