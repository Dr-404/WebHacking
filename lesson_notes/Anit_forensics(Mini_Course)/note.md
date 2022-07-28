# Anit-forensics

## BleachBIt

BleachBit is a free and open-source software that rather than just delete files, actually shreds the files and any slack space making it virtually impossible to recover affected  files. Not only that, but BleachBit is smart enough to remove other traces of files and applications that forensic investigators can find such as Most Recently Used (MRU), PreFetech files, clipboard contents, cookies, history files, temp files, memory dump, uninstallers and more. 

####Belachbit download links

`http://www.bleachbit.org/download`

#### For Kali-Linux

`sudo apt install bleachbit`

#### BleachBit usage in Linux

`shred -f -n 3 test.txt`

```
f  = Forces the change of permission

n  = overwirte times

Elliot use these command in Mr. Robot series
```

## Linux Bash shell Anit-Forensics
#### 1. Diabling History

`export HISTSIZE=0`

#### 2. Clearing History

`history -c`

#### 3. Clearing User Complete History

`cat /dev/null > ~.bash_history && history -c && exit`

# ****USED WITH CAUTION****

#### 4. Shreadding the history (use with caution)

`shred ~/.bash_history`

#### 5. Automating the Clearing of Command History

```
crontab -e

*  * *  shred ~/.bash_history && cat /dev/null > .bash_history
```
This command will execute each morning at 1am, first shredding the bash_history and then erasing the bash_history. Note, that I did not include the history  -c command as it is an internal BASH shell command and can not be used in crontab.


# Hax Editor

#### Window HexEditor

`WinHex`

#### stegno in windwo

`Quick stegno`
`stool`

# Encryption

`aescrypt`

`veracyrpt`
`kleopatra`