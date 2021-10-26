# EDIT ISO FILE

### Password

```
#edit passowrd (passord1), bare midlertidig i ISO-FILE
passwd
```

montere ISO-FILE


```
#starte docker container ubuntu:12.04
docker run -i -t ubuntu:12.04 /bin/bash

#restarte container
docker start -i <containerID/navn>

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
