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
`curl -A "61c08546b939" -e "https://www.nsa.gov/" http://129.241.200.165:19680/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`

