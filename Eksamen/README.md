## Creating the docker container ++
```
docker create -i -t --privileged --name eksamen3 ubuntu:12.04 /bin/bash
docker cp <FILENAME.iso> eksamen:/home
docker start -i eksamen
```

## Installing dependecies
```
sed -i.bak -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

apt-get update
apt-get install nano
apt-get install squashfs-tools
apt-get install mkisofs


```

## Mounitng the iso 
```
mount /home/<FILENAME.iso> /mnt/
cd /mnt
tar cf - . | (cd /tmp/; tar xfp -)
cd /tmp
cp casper/filesystem.squashfs /root/
cd /root
unsquashfs filesystem.squashfs
```

## 1 Edit the root passwd
```
passwd
#type new password

cp /etc/passwd /root/squashfs-root/etc/passwd
cp /etc/shadow /root/squashfs-root/etc/shadow
```


## 2 Edit the boot images
```
cd /tmp/isolinux
    #EDIT THE SPLASH.PNG image 

    #use image magic or other tool to change the image in cli
        https://imagemagick.org/
        https://legacy.imagemagick.org/Usage/text/

#####################################################################
cd /tmp/isolinux
mkdir /picture
cp splash.png /picture/splash-org.png
cd /picture
identify -ping splash-org.png
    #output the atributes
convert splash.png -alpha extract -threshold 0 blank.png
    #removes the text
    #convert -size 640x480 -background red -fill black -pointsize 64 -gravity Center label:'eirikgba@stud.ntnu.no \n HACKED THIS COMPUTERl!!!!'  splash.png
convert blank.png -size 640x480 -background red -fill black -pointsize 44 -gravity Center label:'eirikgba@stud.ntnu.no \n HACKED THIS MACHINE!!!!' splash-finale.png
    #makes the new image with the correct text adn size


```


## 3 Edit the ascii
```
cd /root/squashfs-root/etc/
nano issue
    #put inn the new ascii art
```

## 4 Edit the web page
```
cd /squashfs-root/var/www/html/
nano index.php5

```

## Slå alt sammen 
```
cd /root
mksquashfs squashfs-root/ filesystem.squashfs -no-recovery -always-use-fragments -b 1M -no-duplicates -noappend

cp filesystem.squashfs /tmp/casper/filesystem.squashfs


cd /tmp/
ls
ls -l casper/
ls -l isolinux/

mkisofs -o /home/1480eirikgba@stud.ntnu.no-edit.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-info-table -J -R -V "Eksamen edited ISO" .
```

## Ta det ut og test
```
docker cp eksamen2:/tmp/Eksamen_ascii_edit2.iso .
```

Kjøre opp en nye VM med den nye iso filen
