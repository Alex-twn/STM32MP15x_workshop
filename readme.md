# Setup the development workspace on your host computer

1. Open a terminal and setup your workspace

> ```bash
> PC $> mkdir $HOME/STM32MPU_workspace
> PC $> cd $HOME/STM32MPU_workspace
> ```
>

2. Check host internet access

> ```bash
> PC $> wget -q www.google.com && echo "Internet access over HTTP/HTTPS is OK !" || echo "No internet access over HTTP/HTTPS ! You may need to set up a proxy.“
> ```
>

* *Should provide you the following terminal output if your internet connection is ok*

![](/Pictures/2_Screenshot.png)



------

# Install STM32CubeProgrammer on your host computer

1. STM32CubeProgrammer requires version 1.8 of the Java platform

> ```bash
> PC $> sudo apt-get install openjdk-8-jre-headless
> PC $> sudo update-alternatives --config java
> ```
>

* *Select the java-8-openjdk configuration*

2. Install OpenJFX for Ubuntu® 18.04

> ```bash
> PC $> sudo apt purge openjfx
> PC $> sudo apt install openjfx=8u161-b12-1ubuntu2 libopenjfx-jni=8u161-b12-1ubuntu2 libopenjfx-java=8u161-b12-1ubuntu2
> PC $> sudo apt-mark hold openjfx libopenjfx-jni libopenjfx-java
> ```
>

3. Create your STM32MPU tools directory

> ```bash
> PC $> mkdir $HOME/STM32MPU_workspace/STM32MPU_tools
> PC $> mkdir $HOME/STM32MPU_workspace/STM32MPU_tools/STM32CubeProgrammer-2.5.0
> ```
>

4. Create a temporary directory in your STM32MPU workspace

> ```bash
> PC $> mkdir $HOME/STM32MPU_workspace/tmp
> ```
>

5. Download the latest [STM32CubeProgrammer][id0] in **$HOME/STM32MPU_workspace/tmp**

[id0]: https://www.st.com/en/development-tools/stm32cubeprog.html#getsoftware-scroll

* Note : if you have copied the STM32CubeProgrammer installation file from the USB dongle, please copy this installation file in **$HOME/STM32MPU_workspace/tmp***

6. Decompress the archive file to get the STM32CubeProgrammer installers

> ```bash
> PC $> cd $HOME/STM32MPU_workspace/tmp
> PC $> unzip SetupSTM32CubeProgrammer.zip
> ```
>

7. Execute the Linux installer which guides you through the installation process

> ```bash
> PC $> ./SetupSTM32CubeProgrammer-2.5.0.linux
> ```
>

- Select **$HOME/STM32MPU_workspace/STM32MPU_tools/STM32CubeProgrammer-2.5.0** as the installation directory, when it's requested by the installer*

8. Add the STM32CubeProgrammer binary path to your PATH environment variable (or .bashrc)

> ```bash
> PC $> export PATH=$HOME/STM32MPU_workspace/STM32MPU_tools/STM32CubeProgrammer-2.5.0/bin:$PATH
> ```
>

9. Check that the STM32CubeProgrammer tool is properly installed and accessible

> ```bash
> PC $> STM32_Programmer_CLI –h
> ```
>

* *Should provide you the following terminal output*

![](/Pictures/3_Screenshot.png)



------

# Install USB serial link on your host computer

1. Install the libusb

> ```bash
> PC $> sudo apt-get install libusb-1.0-0
> ```
>

2. Then allow STM32CubeProgrammer to access to the USB port through low-level commands

> ```bash
> PC $> cd $HOME/STM32MPU_workspace/STM32MPU_tools/STM32CubeProgrammer-2.5.0/Drivers/rules
> PC $> sudo cp *.* /etc/udev/rules.d/
> ```
>



------

# Install the starter package on your host computer

1. Create your STM32MP15x Starter Package directory

> ```bash
> PC $> mkdir $HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.0.0
> PC $> mkdir $HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.0.0/Starter-Package
> PC $> cd $HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.0.0/Starter-Package
> ```
>

2. Download the [STM32MP15-Ecosystem-v2.0.0][id1] Starter Package in **$HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.0.0/Starter-Package**

   [id1]: https://www.st.com/content/ccc/resource/technical/software/firmware/group0/6a/12/67/7d/22/19/43/d4/STM32MP15_OpenSTLinux_Starter_Package/files/FLASH-stm32mp1-openstlinux-5-4-dunfell-mp1-20-06-24.tar.xz/_jcr_content/translations/en.FLASH-stm32mp1-openstlinux-5-4-dunfell-mp1-20-06-24.tar.xz

    in **$HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.0.0/Starter-Package**

3. Decompress the tarball file to get the binaries for the different partitions of the image and the Flash layout files

```bash
PC $> tar xvf en.FLASH-stm32mp1-openstlinux-5-4-dunfell-mp1-20-06-24.tar.x
```



------

# Program the SDCard for STM32MP157A-DK1 board

1. Set the boot switches (located at the back of the board) to the off position

![](/Pictures/STM32MP157C-DK2_jumper_flash.jpg)

2. Connect an USB Type A to Type C cable between your PC and CN7 (USB) connector to program the SDCard

3. Connect an USB Type A to Type C cable between your PC and CN6 (PWR_IN) connector to power the board

4. Press the reset button to reset the board

5. Launch STM32CubeProgrammer to get the GUI

   ```bash
   PC $> STM32CubeProgrammer
   ```


![](/Pictures/4_Screenshot.png)

6. On the right, select USB (not STLINK, set by default) in the connection picklist and click on "Refresh" button. Serial Number is displayed if USB is detected. Click on "Connect"

![](/Pictures/5_Screenshot.png)

![](/Pictures/6_Screenshot.png)

7. Select "Open File" tab and select the "FlashLayout_sdcard_stm32mp157a-dk1-trusted.tsv" file in **$HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.5.0/Starter-Package/stm32mp1-openstlinux-5.4-dunfell-mp1-20-06-24/images/stm32mp1/flashlayout_st-image-weston/trusted** installation folder

![](/Pictures/7_Screenshot.jpg)

![](/Pictures/8_Screenshot.jpg)

8. Fill the "Binaries Path" by browsing up to folder **$HOME/STM32MPU_workspace/STM32MP15-Ecosystem-v2.5.0/Starter-Package/stm32mp1-openstlinux-5.4-dunfell-mp1-20-06-24/images/stm32mp1**

![](/Pictures/9_Screenshot.png)

9. Click on "Download" to start the flashing process

![](/Pictures/10_Screenshot.png)

10. Progress is displayed with progress bar till completion popup message

![](/Pictures/11_Screenshot.png)

![](/Pictures/12_Screenshot.png)



------

# Program the SDCard for STM32MP157A-DK1 board

The serial terminal allows to communicate with the board trough a UART serial interface.

- Install minicom

```bash
PC $> sudo apt-get install minicom
```

- Get the ttyACM device instance that need to be used to access the ST-LINK/V2-1

```bash
PC $> ls /dev/ttyACM*
/dev/ttyACM0
```

- Connect the minicom to the /dev/ttyACM0 device

```bash
PC $> minicom -D /dev/ttyACM0
Welcome to minicom 2.7

OPTIONS: I18n 
Compiled on Nov 15 2018, 20:18:47.
Port /dev/ttyACM0, 15:56:03

Press CTRL-A Z for help on special keys
```

- Press the reset button to reset the board. You should see boot log displayed in the minicom window