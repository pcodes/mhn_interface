# A Technical Overview- How do the Honeypots Work?

## Part One- AWS as a backend
- Amazon AWS allows for the rapid deployment of cloud computers, called
EC2 instances. While there are other features associated with AWS, all
that was needed for the Honeypot project was EC2 instances
- One point that came up during billing was the concept of "EBS
  Volumes". Elastic Block Storage (EBS) volumes are essentially the hard
drives used by EC2 instances, but they are also considered seperate from
EC2 instances. You could theoretically move one EBS volume from one EC2
instance to another, effectively sharing the hard drive
- IMPORTANT: Amazon will charge you for having EBS volumes in your
  account, regardless of whether the associated EC2 instance is running.
While we need them to maintain the information about the honeypots, if
future people deploy EC2 instances, then be aware that shutting off an
EC2 instance will NOT free the associated EBS volume, and the account
will continute to be charged

## Part Two- The Honeypot Software: the Modern Honey Network
- The Modern Honey Network (MHN) is a mangement tool that allows for the
  easy deployment of various honeypots across a number of devices. One
server is chosen to be the host for the MHN management server, and all
honeypots report back to this central server
- Honeypots deployed from MHN can run a variety of different honeypot
  software. The primary one used in this particular project is Snort-
while not honeypot software, it does monitor all attempts to remotely
attack the honeypots. p0F is also intalled on these, this allows for
monitoring of the various attack signatures
- Honeypots are called "sensors" by MHN, as they collect data on
  incoming attackers
- To access the MHN management site, navigate to the IP associated with
  the MHN Server, and login using the MHN Management account credentials

## Part Three- The Camp UI: Django
- In order to facilate the custom needs for the camp (multple teams,
  read-only access to the honeypot data, etc.) a custom UI was developed
using Django, a python-based web framework
- By accessing the API available from the MHN management server, the UI
  is able to grab the data and then display the information for each
team
- This UI also uses Docker for deployment, a container-based
  distribution software that allows for distributing projects inside
containers, essentially a lightweight virtual machine
- To access the UI, navigate to the IP address of the MHN Server UI
  (found in the EC2 Management Dashboard)
