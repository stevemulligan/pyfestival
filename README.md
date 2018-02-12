# Py-festival

A Python wrapper around the [Festival Speech Synthesis System](http://www.cstr.ed.ac.uk/projects/festival/).

#### Installation

First install the Python, Festival and their headers    
On Debian:

```
sudo apt-get install python python-dev festival festival-dev
```

Then install using either pip or directly from github:

```
pip install pyfestival
```
or    
```
pip install git+https://github.com/techiaith/pyfestival#festival
```    

**Environment Variables**

If your festival/speechtools headers and libs aren't in the standard place, you may need to set the following variables before installing with pip:

* `FESTIVAL_INCLUDE` - festival header directory. Default is `/usr/include/festival`
* `SPEECH_INCLUDE` - speech tools header directory. Default is `/usr/include/speech_tools`
* `FESTIVAL_LIB` - lib directory for festival `/usr/lib`
* `SPEECH_LIB` - lib directory for speech tools `/usr/lib`
