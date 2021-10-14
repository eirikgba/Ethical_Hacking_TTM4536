# Assigment 4

run communicationXX.pcap i WireShark
search for eirikgba

select/mark pakker som tilhører mine pakker

ekporter packene 

binwalk -e "exportert fil"

gå inn i mappen som ble lagd, og sjekk at det ligger hva som ligger der skal være en .txt og en zip


### Get Passord
Protocol FTP-data
lette etter filer som ikke var .zip eller ikke tilhørte en person

ftp-data: chat.log - filen
høyreklikk -> follow -> TCP stream
"
Danilo: How dificult password should we put for the zip passwords?
TA: We can put random 10 digits numbers bigger than 7890000000. 
Danilo: OK. With fcrackzip they can crack those passwords either in 1 week or in few minutes (if they know where to start the search) :-) 
"

brukte fcrackzip for å finne passordet:
```
fcrackzip -b -c '1' -l  10-11 -p 7890000000 -u 1EC.zip

output: PASSWORD FOUND!!!!: pw == 7890844459
```

bruker passordet til å åpne filen
Hallo. Your f1a9 is: 54861a8388dc84c4ed764da014cddc58

