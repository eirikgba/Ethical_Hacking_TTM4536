#!/bin/bash
filename="xato-net-10-million-passwords-1000.txt"
for word1 in $(cat $filename);
do
        for word2 in $(cat $filename);
                do
                        echo $word1$word2
                done
done
