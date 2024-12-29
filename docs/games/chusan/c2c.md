!!! danger "You are most likely to have success with Multiplayer when all users are using the SAME data and options, from the same sources. Verify that each person can run the game normally before attempting to network them together."

!!! tip ""

	- Chunithm expects the cabinets to be using specific IP addresses, 192.168.139.**11/12/13/14**
	- To achieve this over the internet, we can use SoftEther VPN. Refer to the [Setting Up SoftEther VPN Guide](../../extras/softether.md) for more information.

---
### Configuring segatools.ini & Game Assignments

!!! tip "segatools.ini"

	```
	[netnev]
	enable=1
	addrSuffix= last 2 digits of your SoftEther IP

	[keychip]
	enable=1
	subnet=192.168.139.0
	id=(Everyone needs a seperate keychip. If you play on a remote network, chances are you already have your own keychip. If not, you can use the example keychips below.)
	;example keychips: A61E-01D02321145 ; A61E-01A30831145 ; A61E-01E38091145 ; A61E-01E46241145

	[system]
	dipsw1=1
	;This has changed since Luminous. Previously if you wish to perform cab-to-cab link, you need to set this to 1 on the Server machine, and 0 on all other client machines.
	;This change is no longer needed, just keep this set to 1 on all machines.
	```

!!! tip "GAME ASSIGNMENTS"

	- After saving your segatools.ini, launch the game and go into the Service Menu > and go to ```GAME ASSIGNMENTS```.
	<img src="/img/chunithm/sdhd/c2c/service.png">

	- Enable ```CABINET-TO-CABINET PLAY```, and make sure all machine are on the same group (Group A for example).
	<img src="/img/chunithm/sdhd/c2c/group.png">

	- Set one machine to ```STANDARD```, and all other machines to ```FOLLOW THE STANDARD``` .
	<img src="/img/chunithm/sdhd/c2c/standard.png">
	<img src="/img/chunithm/sdhd/c2c/followstandard.png">

	Exit the Service Menu and load into Attract Mode. If the game passes the Group Check then chances are you're good to go! You can now login to a credit and open a cab-to-cab link request to check if the connection is working properly!
	
---
### How to Link?

!!! Info "If you're new to Chunithm and have never tried link-play before and you have no idea how, keep reading."

	- Login to a credit.

	- If you're hosting a cab-to-cab session, choose a song first, then scroll to the far left and press Confirm. The cab-to-cab request is now open.
	<img src="/img/chunithm/sdhd/c2c/host.png">

	- If you're connecting, navigate to the "Cabinet-to-Cabinet Play" tab and wait for other players to create a session.
	<img src="/img/chunithm/sdhd/c2c/client.png">

	If you are able to see each other's session, congrats! You can now enjoy some cab-to-cab chain action!

### Troubleshooting

!!! warning "Have any other issues?"

	Check out the [Troubleshooting](troubleshooting.md) and [Error Codes](../../errorcodes/sega.md) pages.