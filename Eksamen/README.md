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

## Edit the root passwd
```
passwd
#type new password

cp /etc/passwd /root/squashfs-root/etc/passwd
cp /etc/shadow /root/squashfs-root/etc/shadow
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

mkisofs -o 1480eirikgba@stud.ntnu.no-edit.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-info-table -J -R -V "Eksamen edited ISO" .
```

## Ta det ut og test
```
docker cp eksamen2:/tmp/Eksamen_ascii_edit2.iso .
```

Kjøre opp en nye VM med den nye iso filen
