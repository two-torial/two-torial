# Taiko no Tatsujin Nijiiro Controller Setup

<img src="/img/taikonijiiro/taikonijiiro.png">

## I/O Settings
!!! tip ""
    Enter the I/O setup screen by pressing `F1` on the attract screen then using `arrow keys` and `ENTER` navigate to `I/O TEST` -> `TAIKO TEST`. For the best settings copy the image below. If you wish you can adjust these settings to your liking.

<img src="/img/taikonijiiro/io.png">

***

!!! note "Controllers:"
    Below is a quick introduction and setup guide for the commonly used input methods.

***

## Keyboard

!!! tip ""
    Keyboard is the default input method.  
    The default layout uses `DF JK` for the drum input, `P` to insert card, and `ENTER` to add coins.  
    If you wish to view or change all the default keybinds, you can do so in `keyconfig.toml`.

!!! danger "Warning:"
    If you use a jp layout keyboard you may need to enable `jp_layout =`, `auto_ime =` in `config.toml`.

***

## Controller

!!! tip ""
    The setup for both drum and normal controllers is the same.                                                        
    In `config.toml` set `wait_period =` to `0`.               
    
    If you are using a controller that does not use keyboard inputs then you need to
    set SDL keybinds in `keyconfig.toml`, a list of valid SDL inputs can be found at the bottom of `keyconfig.toml`

!!! danger "Warning:"
    If you use an analog input for the drums you may need to enable `analog_input =` in `config.toml`.

!!! danger "Warning:"
    If you using 2 controllers use [JoyToKey](https://joytokey.net/en/) and remove SDL inputs from `keyconfig.toml`.

***

## Card Reader

!!! tip ""
    The setup for aic pico and acr122u are different.                                                        
    In `config.toml` set `[card_reader]` to `true`.               
    
    If you are using an aic pico update to the latest [firmware](https://github.com/whowechina/aic_pico).                                           
    Inside `AMFWConfig.ini` change com4 to the port of your aic pico                  
    
    If you are using an acr122u or similar.                                                                    
    Use AkaiiKitsune's [tal-cardreader plugin](https://gitea.farewell.dev/AkaiiKitsune/tal-cardreader)

***

## Arcade Drums and other Controllers

!!! tip ""
    If you're interested in connecting a real cabinet Drum, or possibly even DIYing your own controller, the [Cons&Stuff](https://consandstuff.github.io/) website and Discord community is a great place to start!