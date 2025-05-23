# How to setup Asphyxia CORE

!!! danger "If this isn't your first time setting up Asphyxia, make sure to ^^*backup your ```savedata``` folder*^^ and place it somewhere safe."

### What is Asphyxia CORE?

!!! tip ""

	Asphyxia CORE is a ^^local^^ e-amuse emulator which includes score saving and customization. The software itself does not support any game out of the box. For this, you need ```plugins```.

### Configuring Asphyxia

!!! tip ""

	First, grab the latest release [here.](https://github.com/asphyxia-core/asphyxia-core.github.io/releases) In ^^almost^^ all cases, you will use the ```asphyxia-core-win-x64.zip```. Next, open the ```.zip``` file and extract the ```plugins``` folder and ```asphyxia-core-x64.exe``` into the ```contents``` folder of your desired game. We will use SDVX EG for this example.

<img src="/img/extras/asphyxia/1.png">

!!! tip ""

	Your ```contents``` folder should look like this then:

<img src="/img/extras/asphyxia/2.png">

!!! tip ""

	For Asphyxia to run properly, you will need a plugin for each game you want to use it with.

	- Join our [Discord server](https://discord.gg/cZRUmEPK78).
	- Look for your game's channel, then the pinned ```Resources``` post. 
	- Download the plugin archive and open it.
	- It should contain a folder such as `sdvx@asphyxia` or `iidx@asphyxia`.
	- Put that folder in your Asphyxia `plugins` folder, typically `contents\plugins\` and overwrite files if needed.

	Note: We do NOT provide plugins for every game.

!!! tip ""

	Run ```asphyxia-core-x64.exe``` to start the server. It will automatically open a browser tab. This is your ```WebUI```. 

### Changing Service URL

!!! tip ""

	Run ```spicecfg.exe```, head over to the ```Options``` tab and look for ```EA Service URL```. In there, you need to input what is displayed on the Asphyxia WebUI on the ```Dashboard``` at the right side.

<img src="/img/extras/asphyxia/3.png">

!!! tip ""

	For me, it's ```localhost:8083``` and should look like this:

<img src="/img/extras/asphyxia/4.png">
	
### Setting up SDVX

!!! tip ""

	On the ```WebUI```, click on ```SDVX``` on the left-hand bar and on the right side under ```Plugin Settings```, you should see an option named ```Exceed Gear Data Directory```. In here, paste the path of your ```contents``` folder and press enter. ^^In my case^^, it looks like this:
	
<img src="/img/extras/asphyxia/5.png">

!!! tip ""

	Next, click on ```Update Webui Assets``` on the left-hand bar. Make sure you're using the correct path as it won't work otherwise. When you've done that, click on ```Update``` and confirm that you've updated the datacode in your ```ea3-config.xml``` file. After a few seconds, the text console should say ```Done``` and say ```Successfully extracted textures``` if you input your path correctly.

<img src="/img/extras/asphyxia/6.png">

!!! tip ""

	Next, launch the game and card in. Go through the process of creating a profile, then close the game. After that, go to ```SDVX``` on the left-hand bar, then ```Profiles``` and click on the green ```Detail``` button on your preferred profile. Click on ```Setting``` on the top bar and try changing some customization settings at the bottom. If they are working, you're done and everything should function as intended if you set everything correctly.

	If they appear broken, completely close Asphyxia and head to the ```contents``` folder of your game again. If you have inserted the correct path when Importing and everything worked without any errors, you will have a folder called ```webui```. Copy this folder and paste it into ```plugins\sdvx@asphyxia```. Overwrite any files if prompted to. Now close then re-run ```asphyxia-core-x64.exe``` and everything should function as intended.

### Setting up IIDX

!!! tip ""

	You have already done all the step required to have it working. Simply create a profile and it will be visible on the ```WebUI```.
	
!!! tip "You're all done! Enjoy your game!"
