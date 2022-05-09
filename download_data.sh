#!/bin/bash

url_adress=https://www.dropbox.com/s/k23enjvr3fb40o5/corpora.zip?dl=0
data_dir_name=raw_data

wget -O AnnaKarenina.txt $url_adress
wget -O WarAndPeace.txt $url_adress
wget -O WarAndPeaceEng.txt $url_adress

rm -r $data_dir_name
mkdir $data_dir_name
mv *.txt $data_dir_name