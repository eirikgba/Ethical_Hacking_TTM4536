## Starte og kjøre docker container
```
#bare første gang (--privileged = for å kunne mount)
docker run --privileged -i -t ubuntu:12.04 /bin/bash

####################################################################
https://stackoverflow.com/questions/22028795/is-it-possible-to-mount-an-iso-inside-a-docker-container
mulig løsning for å må mountet inne i docker container
docker run --privileged -i -t ubuntu:12.04 /bin/bash
#ELLER
    mknod /dev/loop0 -m0660 b 7 0
    mknod /dev/loop1 -m0660 b 7 1
    ...
    mknod /dev/loop9 -m0660 b 7 9
####################################################################

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
#sed -i -e 's/archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

apt-get update
apt-get install nano
apt-get install squashfs-tools
apt-get install mkisofs

apt-get install mysql-server php5-mysql
mysql_install_db
/usr/bin/mysql_secure_installation

```

## Gjøre klar ISO for endringer inne i container
```
#Mounte iso filer
sudo su
mount /path/to/file.iso /Path/to/mounted/files     #(/tmp or /mnt)
#mulig forbedring:  mount -t iso9660 -o loop /path/to/file.iso /Path/to/mounted/files     #(/tmp or /mnt)

#Må gjøres siden iso mount er skrive beskyttet
#gå til dir hvor iso er mounted
tar cf - . | (cd /tmp/; tar xfp -)
# mulig forbedring: tar cf – * | tar xfp – -C /tmp

#gå inn dit hvor kopien ligger
cd /tmp/
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
#################                       Endre MySQL / LEMP                         #################
####################################################################################################
apt-get update
apt-get install mysql-server php5-mysql
mysql_install_db
mysqld_safe --skip-grant-tables &
/usr/bin/mysql_secure_installation

???

mysqld_safe --skip-grant-tables &
####################    Ved Problemer ? ######################
                #killall mysqld mysqld_safe
        #mysqld_safe --skip-grant-tables --skip-networking &
##############################################################

mysql -u root

    SHOW DATABASES;
    SHOW SCHEMAS;
    
    use mysql;
    update user set password=PASSWORD("passord1") where User='root';
    flush privileges;
    quit

stop mysql
start mysql

mysql -u root -p
    use mysql;
    update user set password=PASSWORD("passord123") where User='borntosec';

    SELECT host,user,password FROM mysql.user;
    quit

mysqladmin -u root -p shutdown
start mysql


#shadow - 3bf1114a986ba87ed28fc1b5884fc2f8
# ? - 58902b59f415f6522b8faad73040ca163ea0acc1


#Dummy data for mysql - http://filldb.info/

LEMP - https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-12-04
```
#### Install SQL tools
```
apt-get install mysql-server php5-mysql
    #input password
mysql_install_db
            #output:
                    To start mysqld at boot time you have to copy
                    support-files/mysql.server to the right place for your system

                    PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
                    To do so, start the server, then issue the following commands:

                    /usr/bin/mysqladmin -u root password 'new-password'
                    /usr/bin/mysqladmin -u root -h 3e2468028e8c password 'new-password'

                    Alternatively you can run:
                    /usr/bin/mysql_secure_installation

                    which will also give you the option of removing the test
                    databases and anonymous user created by default.  This is
                    strongly recommended for production servers.

                    See the manual for more instructions.

                    You can start the MySQL daemon with:
                    cd /usr ; /usr/bin/mysqld_safe &

                    You can test the MySQL daemon with mysql-test-run.pl
                    cd /usr/mysql-test ; perl mysql-test-run.pl

                    Please report any problems at http://bugs.mysql.com/
    #Kjøre en av disse?   
    mysqld_safe --skip-grant-table &
    /usr/sbin/mysqld &
/usr/bin/mysql_secure_installation
```

## Edit MySQL
#### Install SQL tools
```
apt-get install mysql-server php5-mysql
    #input password
mysql_install_db

mysqld_safe --skip-grant-table &
/usr/bin/mysql_secure_installation
```

#### Edit the SQL

###### for å kjøre MySQL demon: /usr/sbin/mysqld &
```
#make backup of the mysql dir
cp -r /var/lib/mysql /var/lib/mysql-backup

#copy mysql folder 
cp /root/squashfs-root/var/lib/mysql /var/lib/mysql
cd /var/lib/mysql


mysqld_safe --skip-grant-table &
mysql -u root       #mysql -u root -p 
    show Databases;
    use mysql;

    update user set password=PASSWORD("passord1") where User='root';
    flush privileges;
    quit

stop mysql
start mysql

mysql -u root -p 
    use mysql;
    update user set password=PASSWORD("passord1") where User='borntosec';

    SELECT host,user,password FROM mysql.user;

    #flush privileges;
    quit

mysqladmin -u root -p shutdown
start mysql


mysql> SELECT host,user,password FROM mysql.user;
+-----------+------------------+-------------------------------------------+
| host      | user             | password                                  |
+-----------+------------------+-------------------------------------------+
| localhost | root             | *091D497488AE9505F0EEEB713E184724025F325B |
| localhost | borntosec        | *A0F0E5AB5C30CADDDC7D6DC7C8C41E3918531B38 |
| 127.0.0.1 | root             | *091D497488AE9505F0EEEB713E184724025F325B |
| ::1       | root             | *091D497488AE9505F0EEEB713E184724025F325B |
| localhost | debian-sys-maint | *4B2BEBBC1ECDAC2F503D76ACB9AA20CFE79C9A79 |
+-----------+------------------+-------------------------------------------+

service mysql start
cd ./squashfs-root/root/ft_root/
find ./ -type f -name "localhost.sql" -exec sed -i "s/3bf1114a986ba87ed28fc1b5884fc2f8/$qq/g" {} \;

    #add data to the images and user sql files
    #http://filldb.info/ 

mysql -u root -ppassord1 < localhost.sql
mysql -u root -pMyBlahBlahPW < clients.sql
mysql -u root -pMyBlahBlahPW < images.sql
mysql -u root -pMyBlahBlahPW < user.sql
cd ..
cd ..
cd ..

# We need to stop the mysql database in order to transfer it to the appropriate folder in ~/squashfs-root
mysqladmin -u root -pMyBlahBlahPW shutdown
# After resetting the root password of our local Docker MySql database to MyBlahBlahPW,
# It is kept in encrypted form in the file /etc/mysql/debian.cnf
# We need to transfer it also to the new hacked ISO
cp /etc/mysql/debian.cnf ./squashfs-root/etc/mysql/debian.cnf
# Now we copy back the whole /var/lib/mysql/ folder back to ~/squashfs-root/var/lib/mysql/
cp -r /var/lib/mysql/* ./squashfs-root/var/lib/mysql/
chmod -R 755 ./squashfs-root/var/lib/mysql
cd /root/
service mysql start

```



## Create new ISO file
```
#Oppdatert filsystem lagres tilbake som squashfs file
#mksquashfs <navn på output from unsquashfs> <navn på fil som ble kjørt unsquashfs> -no-recovery -always-use-fragments -b 1M -no-duplicates -noappend
mksquashfs squashfs-root filesystem.squashfs -no-recovery -always-use-fragments -b 1M -no-duplicates -noappend

#pass på å stå i mappe hvor kopi av mounted iso ligger
cd ..
mkisofs -o Darkly_i386.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-info-table -J -R -V "Darkly custom ISO" .

#kopiere filen fra docker tilbake til maskin
#gå ut av maskin
docker cp <docker_container_navn:/Path/to/file> </path/for/file/filnavn>
#da kan denne iso bli kjørt som en VM
```

Da kan en kjøre en ny VM basert på den nye oppdaterte iso filen
