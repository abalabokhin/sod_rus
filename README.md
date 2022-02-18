# sod_rus

The repo contains the current Russian translation for Baldur's Gate: Siege of Dragonspear (SOD).

It also contain the script to convert one \*.tra file (a localization file for infinity engine modding) into two \*.csv file (one
for male and another one for female).

The script should be used like this:
```
python3 tra2csv.py infile.tra outfile_male.csv outfile_femaile.csv
```
See usage (--help) for details.

The format of csv file is 
```
id,text,comment,timestamp,translate
"1","Зачем ты тревожишь меня? Тебя плохо воспитали? Убирайся!","","1431616436","1"
```
where:
* id - line #
* text - translated text
* comment - always empty string
* timestamp - linux epoch
* translate - always "1"
