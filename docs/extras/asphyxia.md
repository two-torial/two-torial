# How to setup Asphyxia CORE

!!! danger "If this isn't your first time setting up Asphyxia, make sure to ^^*backup your ```savedata``` folder*^^ and place it somewhere safe."

!!! tip ""
	First, grab the latest release [here.](https://github.com/asphyxia-core/asphyxia-core.github.io/releases) In ^^almost^^ all cases, you will use the ```asphyxia-core-win-x64.zip```. Next, open the ```.zip``` file and extract the ```plugins``` folder and ```asphyxia-core-x64.exe``` into the ```contents``` folder of your desired game. I will use SDVX EG for this example.

<img src="/img/asphyxia/1.png">

!!! tip ""
	Your ```contents``` folder should look like this then:

<img src="/img/asphyxia/2.png">

!!! tip ""
	For Asphyxia to run properly, you will need a plugin for each game you want to use it with. For this, we will provide them on our [Discord server.](https://discord.gg/cZRUmEPK78)

	Now look for the ```Asphyxia``` category on the [Discord server](https://discord.gg/cZRUmEPK78) and choose your game. Download the ```.zip``` file and open it. Extract the ```plugins``` folder into the ```contents``` folder like we did before. Overwrite any files if prompted to.

!!! tip ""
	Open ```asphyxia-core-x64.exe``` to start the server. It will automatically open a browser tab. This is your ```WebUI```. Next, click on the game you want to use, in my case, it's ```SDVX``` on the left-hand bar and click on ```Import Assets```. In here, paste the path of your ```contents``` folder.
	
!!! tip ""
	^^In my case^^, it's ```D:\BEMANI\SDVX\guide\KFC-2021083100\contents```. Make sure you're using the correct path as it won't work otherwise. When you've done that, click on ```Submit```. After a few seconds, a pop-up should appear saying ```Imported successfully!```

!!! tip ""
	Go to your desired game on the left-hand bar, which is in my case ```SDVX``` then ```Profiles``` and click on the green ```Detail``` button on your preferred profile. Click on ```Setting``` on the top bar and try changing some customization settings at the bottom. If they are working, head over to [Changing Service URL.](#changing-service-url) If they appear broken, completely close Asphyxia and continue reading.

	Head to the ```contents``` folder of your game again. If you have inserted the correct path when Importing and everything worked without any errors, you will have a folder called ```webui```. Copy this folder and paste it into ```plugins\sdvx@asphyxia```. Overwrite any files if prompted to. Now re-open ```asphyxia-core-x64.exe``` and everything should function as intended.

### Changing Service URL

!!! tip ""
	Lasty, open your ```spicecfg.exe```, head over to the ```Options``` tab and look for ```EA Service URL```. In there, you need to input what is displayed on the Asphyxia WebUI on the ```Dashboard``` at the right side.

<img src="/img/asphyxia/3.png">

!!! tip ""
	For me, it's ```localhost:8083``` and should look like this:

<img src="/img/asphyxia/4.png">

!!! tip "You're all done! Enjoy your game!"
