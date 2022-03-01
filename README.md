# zoomstarter
Python programm to start your zoom meetings

## More about
Initially this was a bash script for starting zoom meetings, but as i started developing it more it became a python program. You can use it for starting, scheduling and maintaining your zoom meetings. 

## Requirements
Only required program for starting this is python latest version.

## Guide
* Nix and Windows system </br>
First you need to run `python setup.py install` and python will handle everything for you. After that you sucessfully installed zoomstarter!
If you want to run it open your favorite terminal and type:
* Windows only<br/>
You can run just install.exe and everything will work as charm.
## Starting app
For gui:<br>
`zoomstartergui`<br>
For cli:<br>
`zoomstarter [options]`<br>
* If you use install.exe you will have exe file on desktop which start<br>
### Options
*-s [name]* for starting meeting<br />
*-a [name] [value]* for adding link <br />
*-d [name]* for deleting link <br /> 
*-r* for reading all links<br />
*-h*  for help <br />
*-c [name] [time]*  for adding cron to start you meeting<br />
*-sw [name] "[value]"* for writting your value in zoom chat<br>
*-df* add as last parameter to load default config which you can change in data folder before install

## Support
Zoomstarter is still in developing and only full supported  and tested system for now is Windows. You can still use some functionalities on Linux.
If you have problem with starting script on nix sistems, try to install tkinter library with your default package manager.


