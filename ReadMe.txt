Still a very much work in progress

Been developing this script to help us copy the general attributes of the transform 
and shape node in lights on the assembly MA files to output to a text file and then the user can import 
it back into the database.  

Also the script works with maya files that have name spaces in the light objects and removes them 


1.  First create directory on the c drive with the name C:\LIGHTING folder for all the text files to go to

2.  Then select the lights whose attributes you want to copy into a text, name the file.

3.  Select which of the attributes you want to copy and hit enter.

4.  Open up the text file, to copy/paste the mel into mel script editor. 

Known Bugs

First function does not work at th moment and needs to be rewritten to have the option of detecting color with no ramp and with a ramp
