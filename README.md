
smart-browser.py - Open any URL in your preferred browser
=========================================================

If you are a browser-customization junkie like me, you will probably also have a bunch of firefox profiles, each one tailored to better perform a task like:

* General browsing
* Intranet browsing
* Web developing
* Social interaction
* Online banking
* ...

As the number of profiles grows, it's cumbersome to open links embedded in mail or other programs with the correct profile. I couldn't count the times that I clicked on a LinkedIn mailing to had it open in my online banking firefox window.

This is where smart-browser.py comes to help.

What's this?
------------

Smart-browser.py is a little helper script written in Python that could be used as a default handler to open any URL. 

Coupled with a simple configuration file (smart-browser.cfg), it empowers you to choose which browser/profile combination should it launch based on which text is present in the URL.

You are not limited to open URLs just in browsers. The provided example opens magnet links in deluge, my bittorrent program of choice.

Installation
------------

1. Edit smart-browser.py and set the variable CONFIGFILE to another location. This step is optional, but if undone then the configuration file must be in the same directory as smart-browser.py.

2. Mark smart-browser.py as executable

	chmod +x smart-browser.py
   
3. Copy smart-browser.py to some directory in your executable path (p.e. /usr/local/bin). Copy the configuration file (smart-browser.cfg) to your CONFIGFILE location (or just copy it to the same place as smart-browser.py if you ignored step 1).

4. Customize your OS to open url links with smart-browser.py. How to make this step depends on your operating system and tech skills, so don't hesitate to [google for it](http://www.google.com/?q=set+default+browser).


5. Edit smart-browser.cfg to suit your needs.


Configuration file syntax
-------------------------

Pretty dumb, really. Put your preferred browsers in [browsers] section and the text too look for in URLs in  [custom urls] section, followed by which browser should open it.

You could also add ":" and a profile name after a browser name to select which profile must be used to open the URL.

Note: Currently only firefox profiles are supported. In the near future chrome/chromium profiles will probably be supported, as I'm starting to use them.

Example:


	[browsers]
	chromium = /usr/bin/chromium
	firefox = /usr/bin/firefox
	deluge = /usr/bin/deluge

	[custom urls]
	"google.com" = chromium
	"localhost" = firefox:webdev
	"linkedin.com" = firefox:social
	"magnet"  = deluge

*Important note*: Only alphanumeric characters and dots are supported as the text to search, mostly because the limited functionality of the ConfigParser python module and my current lack of necessity to program something to work around it. Id sometime I need this functionality I will add it (see TODO #1).


TODO / Roadmap
--------------

There is a lot of room for improvements:

* More flexible URL definitions (like allowing regular expressions), introducing a ConfigObj dependency or programming a custom parser for the config file.
* Open URLs dinamically detecting the correct profile. Look into bookmarks, current browsing sessions or other sources to choose how to open an URL. This must be pretty easy to do, as most of this data is plain text or stored in sqlite databases.
* Windows compatibility. I didn't have tested this program in a Windows environment, but it should probably run (provided Python is installed and configured to open *.py files). Feel free to contact me if you try it :)
* Better packaging (like a deb file or a PPA).

Feel free to contact me also if you have any suggestions.
