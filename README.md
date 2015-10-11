# Network Dependent Network Drive Mount (Windows)

When using a portable computer running windows, it is often the case that 
different network shares need to be mounted for each network connected.

For example, when using a laptop at work and at home, each network has 
its own network drives.

Although it is possible to map all drives, in some cases having a drive that
cannot be connected to, causes problems.  For example, when dragging a file
over such a drive, Windows will try to query the drive, even if there is no
chance of it succeeding.  This causes irritating delays.

The python script in this project takes a list of drives to be mounted,
and a network IP pattern to be checked.
If the IP pattern matches the machine's address, the drive is mapped.
The script polls the address every 5 seconds (change to whatever suits you),
but mapping only occurs when an IP change is detected.

# Requirements:

  * Python 2.7
  * PyQt4
  
  
# Installation:

Extract anywhere, edit the configuration file to your needs
and run at startup.

Create a shortcut at:
C:\Users\<your user name here>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

# Configuration

Each drive has one line composed of:

&lt;IP Pattern&gt;  &lt;Drive&gt;  &lt;Path&gt;  [User] [PasswordName]


If the current IP has a substring that matches the pattern, the drive will be mounted.
The first 3 fields are mandatory, and the user and password are optional.
Passwords are not stored in the file.  Instead the password is given a symbolic name
so that it can be shared for multiple drives.
During runtime, the script will prompt for the password.