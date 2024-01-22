# What is WASAPI and ASIO?

!!! tip ""
	```WASAPI``` and ```ASIO``` are audio systems that manage how your applications like games, music, and others interact with your audio hardware. Without these core systems you would ^^not^^ be able to hear anything. There are 3 types that I'll cover here with pros and cons for each one.

	I would ^^personally^^ recommend using ```WASAPI Shared``` as this has in most cases the highest chance of working and requires the least amount of work. You can enable it by using a [hex edit.](../extras/patchweb.md#how-to-use-patcher-websites)

### WASAPI Shared

!!! tip ""
	```WASAPI Shared``` mode is the standard mode that Windows uses. This allows you to hear multiple audio sources at once and allows programs to capture audio with programs like OBS and Discord. While this is nice for using windows and playing most games, this has a *negative side effect of increasing audio latency.*

	```
	Pros:
	-Multiple audio sources can be sent to one audio device.
	-Can capture audio using OBS or Discord.
	-Supports almost all audio hardware as this is the standard for Windows.
	-Easy to set up.
	
	Cons:
	-Higher Latency.
	-Poor/Hard to configure for low latency.
	-USB audio devices are not supported (DAC).
	```

### WASAPI Exclusive

!!! tip ""
	```WASAPI Exclusive``` mode is a secondary mode which allows one program to take complete control over an audio device. This allows an application to do anything to your audio device including changing settings like change volume, sample rates, and buffer size. With this in mind, this also bypasses a lot of latency that is introduced with multiple applications playing their own audio. 

	The main downside is that you can only hear ^^one^^ audio source (the program that has control). In this case for example, beatmaniaIIDX would take complete control and you would not be able to hear applications like Discord. You cannot capture audio while running this mode without special software.

	```
	Pros:
	-Low Latency (Real Time Latency)
	-Supports almost all audio hardware as this is the standard for Windows.
	
	Cons:
	-Application controls the hardware.
	-Not easily configurable.
	-Can not capture audio with OBS or Discord (Can be done, but requires a lot of configuration and can introduce latency. Switching to WASAPI Shared mode is recommended for this use case).
	-USB audio devices are not supported (DAC).
	```

### ASIO

!!! tip ""
	```ASIO``` stands for Audio Stream Input/Output. This is an audio driver designed for Audio Interfaces on Windows that is very similar to WASAPI Exclusive.

	The biggest difference between ASIO and WASAPI Exclusive is software/hardware support and age. In order to use ASIO, ^^both your hardware and the application you are using must support ASIO.^^ For example, Sound Voltex supports ASIO natively but it does take a bit to set up compared to WASAPI Exclusive. ASIO also has higher configurability.

	```
	Pros:
	-Low Latency (Real Time Latency)
	-Highly Configurable
	-Industry standard for musicians means tons of support documentation.
	
	Cons:
	-Limited Hardware Support
	-Application controls hardware.
	-Can not capture audio with OBS or Discord (Can be done, but requires a lot of configuration and can introduce latency. Switching to WASAPI Shared mode is recommended for this use case).
	-Requires a powerful CPU.
	```