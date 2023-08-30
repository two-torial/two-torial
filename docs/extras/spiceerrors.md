# SpiceTools Error Messages

!!! warning "Before reading:"
	This section contains common errors that users may come across when utilizing SpiceTools that DO NOT pertain to [Error Codes.](/errorcodes/) While it's virtually impossible to write on every solution for every error, there's a small handful that arise from time to time. Consider this one of the weaker sections on the site due to the infinitely varying amounts of hardware and game-specific problems that may arise. Nonetheless, this section may be helpful as a last resort or for overly specific issues. Errors are listed in potpourri fashion with game specific notes inside said sections as applicable.

### Initial Checklist

!!! tip ""
	There's always a couple quick things to check before even running SpiceTools, namely...

	- Your data comes from a clean and trusted source, ideally unmodified.
	- You are not currently seeding your data and it's not already opened.
	- You have specified within Windows that SpiceTools should be ran as an administrator.
	- You're using the latest SpiceTools
	- You've correctly followed the `First Time Setup` and `Common Problems/Tips` section of your desired game and your `.bat` file contains no errors.

### Failed to Read /dev/nvram/coin.xml.

!!! tip ""
	Copy `coin.xml` from `prop` to `dev/nvram` or alternatively, update to a SpiceTools as new as 03/04/2020 or later.

### Failed to Read /dev/nvram/eacoin.xml.

!!! tip ""
	Copy `eacoin.xml` from `prop` to `dev/nvram` or alternatively, update to a SpiceTools as new as 03/04/2020 or later.

### Cannot create property: prop/ea3-config.xml

!!! tip ""
	Firstly make sure your `ea3-config.xml` is clean and that it is not set to `Read-only`. 

	If it's been modified, common problems that might arise may be having `https` under `<services __type="str">urlhere</services>` or anywhere else a custom services URL has been added. Use `http` instead. 

	Don't use notepad when modifying any of the .xml files, it can break the encoding and cause issues.

	Ideally just use SpiceTools `-url` and `-p` parameters to avoid modifying this file in most use cases.

### XYZ Couldn't be loaded: Specified module cannot be found.

!!! tip ""
	Firstly, make sure what is attempting to load is indeed present.

	If the file is `libavs-win64.dll` then you're using 64-bit SpiceTools when the game is 32-bit, please switch to 32-bit instead. SpiceTools should also tell you do this!

	However, more often than not this error is more the user missing specific dependencies. Below are the most common ones that are missing on a fresh installation or older hardware.

	- [Microsoft Visual C++ 2010 Redistributable Package (x64)](https://www.microsoft.com/en-us/download/confirmation.aspx?id=14632)
	- [DirectX 9.0c End-User Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=34429)

### Crashing Upon Startup

!!! tip ""
	This issue has numerous reasons all pertaining to the user, most commonly the game is not able to run at its specified resolution, say a game requiring portrait mode while running in landscape for example. This might also occur if installation was not done properly, or key files are missing as well.

	SpiceTools does a good job documenting what errors are occurring, make sure to read near the bottom of `log.txt` after a crash to try and better understand what might be wrong.