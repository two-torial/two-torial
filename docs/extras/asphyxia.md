--8<-- "docs/snippets/common/old_guide.md"

!!! danger "If this isn't your first time setting up Asphyxia, make sure to ^^*backup your `savedata` folder*^^ and place it somewhere safe."

## What is Asphyxia CORE?

!!! tip ""

    Asphyxia CORE is a ^^local^^ e-amuse emulator which includes score saving and customization. The software itself does not support any game out of the box. For this, you need `plugins`.

## Configuring Asphyxia

!!! tip ""

    First, grab the latest release [here.](https://github.com/asphyxia-core/asphyxia-core.github.io/releases) In ^^almost^^ all cases, you will use the `asphyxia-core-win-x64.zip`. Next, open the `.zip` file and extract the `plugins` folder and `asphyxia-core-x64.exe` into the `contents` folder of your desired game. We will use SDVX EG for this example.

<img src="/img/extras/asphyxia/1.webp">

!!! tip ""

    Your `contents` folder should look like this then:

<img src="/img/extras/asphyxia/2.webp">

!!! tip ""

    For Asphyxia to run properly, you will need a plugin for each game you want to use it with.

    - Join our Discord server by clicking the Discord logo at the bottom right of the page
    - Look for your game's channel, then the pinned `Resources` post.
    - Download the plugin archive and open it
    - It should contain a folder such as `sdvx@asphyxia` or `iidx@asphyxia`
    - Put that folder in your Asphyxia `plugins` folder

    Note: We can't provide links to plugins for every game, only the ones that have known good plugins.

!!! tip ""

    Run `asphyxia-core-x64.exe` to start the server. It will automatically open a browser tab. This is your `WebUI`. 

## Changing Service URL

!!! tip ""

    Run `spicecfg.exe`, head over to the `Options` tab and look for `EA Service URL`. In there, you need to input what is displayed on the Asphyxia WebUI on the `Dashboard` at the right side.

<img src="/img/extras/asphyxia/3.webp">

!!! tip ""

    Here it's `localhost:8083`.

<img src="/img/extras/asphyxia/4.webp">
    
## Setting up SDVX

!!! tip ""

    On the `WebUI`, click on `SDVX` on the left-hand bar and on the right side under `Plugin Settings`, you should see an option named `Exceed Gear Data Directory`. In here, paste the path of your `contents` folder and press enter. ^^In my case^^, it looks like this:
    
<img src="/img/extras/asphyxia/5.webp">

!!! tip ""

    Next, click on `Update Webui Assets` on the left-hand bar. Make sure you're using the correct path as it won't work otherwise. When you've done that, click on `Update` and confirm that you've updated the datacode in your `ea3-config.xml` file. After a few seconds, the text console should say `Done` and say `Successfully extracted textures` if you input your path correctly.

<img src="/img/extras/asphyxia/6.webp">

!!! tip ""

    Next, launch the game and card in. Go through the process of creating a profile, then close the game. After that, go to `SDVX` on the left-hand bar, then `Profiles` and click on the green `Detail` button on your preferred profile. Click on `Setting` on the top bar and try changing some customization settings at the bottom. If they are working, you're done and everything should function as intended if you set everything correctly.

    If they appear broken, completely close Asphyxia and head to the `contents` folder of your game again. If you have inserted the correct path when Importing and everything worked without any errors, you will have a folder called `webui`. Copy this folder and paste it into `plugins\sdvx@asphyxia`. Overwrite any files if prompted to. Now close then re-run `asphyxia-core-x64.exe` and everything should function as intended.

## Setting up IIDX

!!! tip ""

    You have already done all the step required to have it working. Simply create a profile and it will be visible on the `WebUI`.