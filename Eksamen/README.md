

## Creating the docker container ++
```
docker create -i -t --privileged --name eksamen ubuntu:12.04 /bin/bash
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




