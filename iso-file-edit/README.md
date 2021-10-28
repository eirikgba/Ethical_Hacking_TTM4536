# EDIT ISO FILE

### Nyttige filer
- https://www.unixmen.com/edit-iso-files-using-mkisofs-in-linux/
- https://sleeplessbeastie.eu/2012/05/27/how-to-modify-squashfs-image/
 
LEMP
- https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-12-04

## Edit Password on iso
Gjorde alt på KAli VM

```
#edit passowrd (passord1), bare midlertidig i ISO-FILE
passwd
```

montere ISO-FILE


```
#mount iso FILE
sudo mount /home/kali/Darkly_i386.iso /tmp/iso

cd tmp/iso
#finne .squashfs filen
cd casper

#kopiere til root
sudo cp filesystem.squashfs /root
cd /root

unsquashfs filesystem.squashfs


```
docker 
```
#starte docker container ubuntu:12.04
docker run -i -t ubuntu:12.04 /bin/bash

#restarte container og kjøre commandoer i container
docker start -i <containerID/navn>

docker cp <filnavn> <docker_image_navn:/Path/for/file>
docker cp squashfs-root ecstatic_lamarr:/root/

```

inne i docker container
```
dcoker start -i <container-navn>
cd root/squashfs-root

passwd
#type passord x2 (passord1)¨

# Kopier filene som tilhører Docker containeren til Filene fra ISO
cp /etc/passwd root/etc/passwd   
cp /etc/shadow root/etc/shadow   
```
PÅ VMen
```
#kopiere alt fra filsystemet tilbake på VM
docker cp ecstatic_lamarr:/root/squashfs-root /home 

#makes a ne squashfs file
mksquashfs squashfs-root filesystem.squashfs -no-recovery -always-use-fragments -b 1M -no-duplicates -noappend
#output filesystem.squashfs

#Mount(er) iso file
mount -t iso9660 -o loop Darkly_i386.iso /mnt
cd /mnt

tar cf - . | (cd /tmp/custom; tar xfp -)
cd /tmp/custom

#Oppdater til den nye squashfs file
#cp <dir/der/filen/ligger/filesystem.squashfs> <dir/der/kopi/av/mounten/ligger/casper/filesystem.squashfs> #den siste delen vill alltid være casper/filesystem.squashfs så lenge en har gjort 
cp /*/filesystem.squashfs casper/filesystem.squashfs


#Lage ny iso fil med endringene
mkisofs -o Darkly_i386.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-info-table -J -R -V "Darkly custom ISO" .

```

starte VM basert på ny ISO

```
brukernavn: root
passord: (det som ble satt)     #Pass på kan være annet keyboard layout

#logget inn:
loadkeys no     #setter norsk tastatur

#Kjøre commandoer i maskinen
```




