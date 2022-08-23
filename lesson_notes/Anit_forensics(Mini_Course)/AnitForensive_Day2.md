# Anti-Forensive Day-2

## Securing Your Credential

1. Never store password on Browser
2. Use Password Manager

## Securing your message (encryption continue)

Cyberchef download lin
`https://github.com/gchq/CyberChef/releases/download/v9.46.0/CyberChef_v9.46.0.zip`

## Overwriting Metadata

- The Windows registry key
`HKLM\SYSTEM\CurrentControlSet\Control\FileSystem\NtfsDisableLastAccessUpdate` can be set to “1” to
disable updating of the last-accessed timestamp; 

## Data Wiping

- scure data deletion

```
Bleach-Bit 	(window)
Shradder 	(Linux)
iShradder 	(andorid)
```

## In linux

`sudo apt install bleachbit`

<b> US DOD (Department of Defense) standard Wiping </b>

- Overwrit Drive with 0
- Overwirt Drive with 1
- Overwerit Drive with Random Data

Elliot use this standard in Mr. Robot Series


`shred -f -n 3 test.txt`



```
f  = Forces the change of permission

n  = overwirte times
```