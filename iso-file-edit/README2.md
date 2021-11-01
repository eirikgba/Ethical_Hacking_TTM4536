
## Starte og kjøre docker container
```
#bare første gang
docker run -i -t ubuntu:12.04 /bin/bash

#Kopiere over filer til container
docker cp <filnavn> <docker_container_navn:/Path/to/file>


#starte og kjøre kommandoer i container
docker start -i <containerNavn>

#Kopiere filer fra container til maskin
docker cp <docker_container_navn:/Path/to/file> </path/for/file/filnavn>
```

## Kjøre inne i container for installer dependecies
``` 
#sette norsk/us keyboard
loadkeys no/us
setxkbmap no

#install ting som trengs
#trenger bare en av disse for å få instalert på (gammelt) ubuntu 12.04
sed -i.bak -r 's/(archive|security).ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list
sed -i -e 's/archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

apt-get update
apt-get install squashfs-tool
apt-get install mkisofs

```

## Gjøre klar ISO for endringer inne i container
```
#Mounte iso filer
sudo su
mount /path/to/file.iso /Path/to/mounted/files     #(/tmp or /mnt)
#mulig forbedring:  mount -t iso9660 -o loop /path/to/file.iso /Path/to/mounted/files     #(/tmp or /mnt)

#Må gjøres siden iso mount er skrive beskyttet
#gå til dir hvor iso er mounted
tar cf - . | (cd /tmp/custom; tar xfp -)       #
# mulig forbedring: tar cf – * | tar xfp – -C /target

#gå inn dit hvor kopien ligger
cd /tmp/custom
#find the squashfs file 
find */*.squashfs                                       #tror det skal fungere evt sjekke manuelt

unsquashfs filesystem.squashfs                          #evt annet navn
#får en dir fra commando som heter squashfs-root - gå inn i den
```
## Endre på ISO filen
```
####################################################################################################
#################               Nå kan en begyne å gjøre endinger                  #################
####################################################################################################


####################################################################################################
#################                       Endre root passord                         #################
####################################################################################################
#endre root passord
passwd
#skriv inn passord

#oppdater passordet inn til iso
cp /etc/passwd /path/for/kopi/av/mount/etc/passwd             #root/etc/passwd   
cp /etc/shadow /path/for/kopi/av/mount/etc/shadow             #root/etc/shadow
#hvis dette ikke fungerer må en kopiere alle mountede filer til en annen dir fordi de er skrive beskyttet 

####################################################################################################
#################                       Endre *                                    #################
####################################################################################################
```

## Create new ISO file
```
#Oppdatert filsystem lagres tilbake som squashfs file
#mksquashfs <navn på output from unsquashfs> <navn på fil som ble kjørt unsquashfs> -no-recovery -always-use-fragments -b 1M -no-duplicates -noappend
mksquashfs squashfs-root filesystem.squashfs -no-recovery -always-use-fragments -b 1M -no-duplicates -noappend

#pass på å stå i mappe hvor kopi av mounted iso ligger
mkisofs -o Darkly_i386.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-info-table -J -R -V "Darkly custom ISO" .

#kopiere filen fra docker tilbake til maskin
#gå ut av maskin
docker cp <docker_container_navn:/Path/to/file> </path/for/file/filnavn>
#da kan denne iso bli kjørt som en VM
```

Da kan en kjøre en ny VM basert på den nye oppdaterte iso filen
