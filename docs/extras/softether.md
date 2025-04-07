# Setting Up SoftEther VPN for Cabinet-to-Cabinet Play

### What is SoftEther VPN?

!!! tip ""

	SoftEther VPN is a free tool we use to create Virtual Hubs and connect multiple machines to the same virtual network, allowing the ability to perform Cabinet-to-Cabinet link even when the machines are on physically different networks.

---
### Configuring SoftEther Server

!!! danger "This part of the guide is for hosting a hub! If you only wish to connect to a hub, refer to [Connecting to a SoftEther Hub](#connecting-to-a-softether-hub)."

!!! info "While this guide is mainly focused on setting up link-play for arcade games, theoretically this should also work with other PC games that supports link-playing over LAN."

#### Setting up the Server, and Creating a Hub

!!! tip ""

	First, go to the [SoftEther VPN Download Center](https://www.softether-download.com/en.aspx?product=softether). In the ```Select Component``` section, choose ```SoftEther VPN Server```. Choose the Operating System and CPU based on your own machine, and grab the latest ```rtm``` build. This guide will be using Windows as an example, the layout for other OS might vary.

<img src="/img/extras/softether/softetherserverdownload.png">

!!! tip ""

	Run the installer and choose to install ```SoftEther VPN Server```. Press Next to finish the installation, and start the Server Manager.

<img src="/img/extras/softether/serverinstall.png">

!!! tip ""

	When running the Server Manager for the first time, you should be greeted with the window below. Click on the ```Connect``` button.

<img src="/img/extras/softether/serverfirstboot.png">

!!! tip ""

	If prompted to setup a root password, set a password that you will remember. If prompted with the Easy Setup wizard, click ```Close``` on the bottom right of the window.

<img src="/img/extras/softether/easysetup.png">

!!! tip ""

	Click on ```Create a Virtual Hub``` on the window below.

<img src="/img/extras/softether/createhub.png">

!!! tip ""

	Give your hub a name, and set an admin password. In this example, we will use Two-Torial.

!!! Info "If you wish to limit the maximum amount of sessions that can be connected to your hub at a time, you can enable ```Limit Max VPN Sessions```. Most arcade games support up to 4-way link, so we will set the limit to 4 in this example."

<img src="/img/extras/softether/hubcreation.png">

!!! tip ""

	Your hub is now created! You should see the hub show up on your Virtual Hub list. Click on the hub to highlight it, and click ```Manage Virtual Hub```.

<img src="/img/extras/softether/managehub.png">

---
#### Adding Users to your Virtual Hub

!!! tip ""

	You will need to add User Accounts into the Virtual Hub before anyone can connect. Click on ```Manage Users```, then click ```New``` at the bottom left of the window.

<img src="/img/extras/softether/manageuser.png">

!!! tip ""

	Set a Username and Password for the user account, then check the ```Set Security Policy``` box on the top right, and click ```Security Policy```. 

<img src="/img/extras/softether/createnewuser.png">

!!! tip ""

	Scroll down and find ```Unlimited Number of Broadcasts``` and ```Filter all IPv6 Packets```, then enable the 2 options. Leave everything else as defaults and click ```OK```.

<img src="/img/extras/softether/unlimitedbroadcast.png">
<img src="/img/extras/softether/filteripv6.png">

!!! tip ""

	Click on ```OK```, and your user account should be created. Click on ```Exit``` to go back to the Hub Management page.

!!! Info "You can either create one user account and give everyone the same credentials to connect to your hub under the same user, or you can also create individual user accounts for all the players that wish to connect to your hub. I recommend creating an user account for each player so you can have an easier time to manage the hub if needed."

<img src="/img/extras/softether/usercreated.png">
<img src="/img/extras/softether/usercreated2.png">

---
#### Configuring SecureNAT

!!! tip ""

	We will use the SecureNAT option to assign a custom subnet to each connected machines. Some games like Chunithm requires you to be on a specific subnet or cab-to-cab link will not work.
	Click on ```Virtual NAT and Virtual DHCP Server (SecureNAT)```, then enable SecureNAT, and click on ```SecureNAT Configuration```.

<img src="/img/extras/softether/securenat.png">
<img src="/img/extras/softether/enablesecurenat.png">

!!! tip ""

	- In the SecureNAT Configration window, set the IP Address under ```Virtual Host Network Interface Settings``` to the subnet you wish to use. In this exmaple, we will be using ```192.168.139.x``` as this is the subnet required by Chunithm for cab-to-cab play.
	- Under ```Virtual DHCP Server Settings```, set the IP Address range you wish to distribute to the connected machines. We will use a suffix of ```11``` to ```14``` in this example.
	- **IMPORTANT: LEAVE THE ```Options Applied to Clients``` SECTION BLANK!!!**
	Once everything is set, click on ```OK``` and ```Exit```.

<img src="/img/extras/softether/configsecurenat.png">

---
#### Setting a Dynamic DNS for your SoftEther Server

!!! info "You can set a custom DDNS Hostname for your SoftEther Server to allow people to remember your Server Hostname more easily. You can also just leave the hostname as default if you wish."

	Click ```Dynamic DNS Setting``` on the bottom left.

<img src="/img/extras/softether/ddns.png">

!!! tip ""
	
	- Under ```Change the Dynamic DNS Hostname``` section, set your preferred hostname. In this example, we will use ```twotorial```.
	- Click ```Set to Above Hostname``` when done, and click ```Exit```.

<img src="/img/extras/softether/configddns.png">

!!! info "If a prompt shows up and ask if you want to regenerate a new Server Certificate, click on No."

<img src="/img/extras/softether/ddnscert.png">

!!! tip ""
	
	If done correctly, the bottom left of your Virtual Hub management window should show your updated Hostname.

<img src="/img/extras/softether/hostname.png">

!!! tip ""
	
	The server setup is done! User(s) should be able to connect to your hub now.

---
### Connecting to a SoftEther Hub

#### Setting up the VPN Client

!!! info "If you already have a hub created / you have a hub ready to connect, keep reading."

	Go to the [SoftEther VPN Download Center](https://www.softether-download.com/en.aspx?product=softether). In the ```Select Component``` section, choose ```SoftEther VPN Client```. Choose the Operating System and CPU based on your own machine, and grab the latest ```rtm``` build. This guide will be using Windows as an example, the layout for other OS might vary.

<img src="/img/extras/softether/softetherclient.png">

!!! tip ""

	Run the installer and choose to install ```SoftEther VPN Client```. Press Next to finish the installation, and start the VPN Client.

<img src="/img/extras/softether/clientinstall.png">

!!! tip ""
	
	In the VPN Client window, click on ```Add VPN Connection```.

<img src="/img/extras/softether/addvpn.png">

!!! info "If a prompt shows up saying that you need to create a Virtual Network Adapter first, click Yes."

<img src="/img/extras/softether/createadapter.png">

!!! tip ""

	Leave the adapter name as default, and press ```OK```. Wait for the creation process to finish.

<img src="/img/extras/softether/createadapter2.png">

<img src="/img/extras/softether/createadapter3.png">

---
#### Connecting to a Virtual Hub

!!! tip ""

	After you have created a Virtual Network Adapter, you should be able to add a VPN Hub. Click on ```Add VPN Connection``` again.

<img src="/img/extras/softether/addvpn.png">

!!! tip ""

	- Name the Hub whatever you prefer. In this example, we will use ```Twotorial```.
	- In the ```Destination VPN Server``` section, input the server Hostname and port. The hostname should usually be ```[your_hostname].softether.net```
	- If the Hostname is correct and the client is able to establish a connection, the Virtual Hub Name should auto-fill when you click on the dropdown box.

!!! info "If the Virtual Hub Name shows a blank list even after clicking the dropdown box multiple times, it usually means your client is unable to establish a connection. Double check if the hostname, and your hub config is correct."

<img src="/img/extras/softether/hubname.png">

!!! tip ""

	- Under ```User Authentication Setting```, input your username and password.
	- If you are connecting to another person's hub, ask the person for your login credentials.

<img src="/img/extras/softether/hublogin.png">

!!! tip ""

	- Under ```Advanced Setting of Communication```, **UNCHECK THE ```RECONNECTS AUTOMATICALLY AFTER DISCONNECTED``` BOX.** If this option is enabled, your VPN Client will always try to reconnect to the hub when it is running, taking up a spot in the hub. Please do not do this, it's just annoying when you're AFK in someone's hub and hogging up a spot.
	- Click ```Advanced Settings...```.

<img src="/img/extras/softether/autoreconnect.png">

!!! tip ""
	
	- In the Advanced Settings window, you can set the ```Number of TCP Connections``` you wish to use. The higher you set, the more connections will be used, resulting in a potentially better link-play experience especially for real-time PVP games like Wangan Midnight Maximum Tune or Initial D: The Arcade.
	!!! Info "If you set this to a very high value and your connection speed is unable to keep up with the requests, your connection quality may be negatively impacted. I recommend setting this to 8 for a good balance."
	- If you find yourself desyncing a lot when in game, you can also enable ```Use Data Compression``` to improve the connection stability.
	- Click on ```OK``` once everything is set.

<img src="/img/extras/softether/advancedclientconfig.png">

!!! tip ""
	
	Double click on the VPN hub to connect. If it shows you your assigned IP address, congratulations! You are now connected to the Virtual Hub and is ready for some cab-to-cab action!

<img src="/img/extras/softether/connected.png">

---
### Tips

!!! tip ""

	- If you need to fetch your assigned IP address because the notification window disappeared too fast or if you forgot your IP, you can do so with the ```ipconfig``` command in CMD.
	- The Virtual Adapter name will usually be ```Unknown adapter VPN - VPN Client```. 

	<img src="/img/extras/softether/ipconfig.png">

!!! tip ""
	
	- If you already have your hub setup and want to share the config with other users, you can ```Export``` your VPN profile and send it to them. Right click on the VPN Hub you wish to share and click ```Export VPN Connection Setting...```.

	<img src="/img/extras/softether/export.png">

!!! tip ""	

	- If you wish to include your username and password in the exported config, click on No. If the hub you are connecting to have different accounts setup for individual users, click on Yes to remove all sensitive information from the config.

	<img src="/img/extras/softether/exportpassword.png">