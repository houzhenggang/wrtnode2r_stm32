
## Working Environment

This project can cross-compiled on Ubuntu, MacOS, Windows. For more infomation about how to compile and build mdk project, you can go though [RT-Thread user Manual](http://www.rt-thread.org/download/manual/rtthread_manual.zh.pdf).

## Build tools

### Install python and scons

##### Ubuntu

	sudo apt-get install python2.7 scons

##### MacOS
	
	brew install python scons

##### Windows

Download & install [python2.7](https://www.python.org/downloads/) and [scons](http://www.scons.org/)

### Install gcc-arm-none-eabi 4.9

##### Ubuntu

	sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded
	sudo apt-get update
	sudo apt-get install gcc-arm-none-eabi

##### MacOS

	brew install arm-none-eabi-gcc

##### Windows

Download & install [arm-none-eabi-gcc](https://launchpad.net/gcc-arm-embedded/)

### Clone rt-thread and WRTnode-stm32 source code

	git clone https://github.com/RT-Thread/rt-thread.git
	git clone https://github.com/WRTnode/wrtnode2r_stm32.git

### Configure the WRTnode-stm32

- Change **EXEC_PATH** in rtconfig.py as your cross compile tool path.
- Change **RTT_ROOT** in SConstruct as your RT-thread root path.

### Compile and Clean
##### complie

	scons

##### clean

	scons -c

### Work in MDK5

If you want to use scons to build MDK project, make sure you **did not** open *template.uvprojx* file.

- Open CMD window and run

	scons --target=mdk5 -s

- After that, you will find new mdk project file *project.uvprojx*.

- Open it, start compile and debug.

