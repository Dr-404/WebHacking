# Anti-forensics

#### Credit `@dnsprincess` for all methodology

>1. Avoiding avoid detection 
>2. Disrupting the collection of information
>3. Incresing the time that examiner to spend on a case


# General Methodology

1. Encryption 
2. Misdirection
3. Changing Timestamps 
3. Secure Data Wiping
4. Stegnography

## Level of Hiding

#### 1. From Your family (security controls)
> eg. Privat content
> * Use Vaulit application or change extension
> * Low anit-forensic use
> * Tools easily found online
> 

#### 2. Local Authorithies (Obfuscate)
> eg. Small incidents
> * They may understand beginner level forensics
> * They use package like Cellebrite, Autospsy, etc...
> * Tools dependent
> * Mildly intrusive anti-forensics

> Our Tools
> * Hex editor
> * Forensic packages
> * Removal media
> * Decoy, Fasle fruit


#### 3. Special Agent (???) (unusable evidence)
> eg. Interstate Action ??
> More proficients, not tool dependent
> 
> Our Tools
> * End-to-End Enryption
> * Autopsy
> * SpiderOak
> * Bunner device
> * Soldered storage media

#### 4. Nation or State Op?? (burn)
> Espionage
> Bun all down


#### Strategy

1. Evidence Doubt - Your family , Local Auth
2. Attribution Doubt - Agents


# Specific Technique

## Your Family, Local Auth

>#### 1. Renaming file extension (Your Family, Local Auth)
>#### 2. Vault App (Forensive Tools can easily found  )
>#### 3. Changing file header - Forensics software can detect file header
>#### 4. Steganography
> Don't Leave any trace of stego application on your system
> Check against Stegdetect
> StegFS in Linux
## Special Agent && Nation State ??

#### 5. Shredding - Completely Delete and Overwirte Disk Space 
#### 6. Timestomp (To defeat timelin analysis in forensics )  


#### Thing you need to delete

1. All file fragments
2. All metadata
3. Traced item (THumbnails)


# Practical Anti-Forensive

#### 1. Misdirection

>1. Renaming File extension
>2. Changing file header
>3. Timestomping
>

#### 2. Encryption

>1. aescrypt (GUI + CLI)
>

#### 3. File Wiping (Shredding)

1. <b>Normal Data Wipe</b>
> use bleachbit

><b>In linux<b>
>
> `sudo apt install bleachbit`

2. <b> US DOD (Department of Defense) standard Wiping </b>
>1. Overwrit Drive with 0
>2. Overwirt Drive with 1
>3. Overwerit Drive with Random Data
>
>Elliot use this standard in Mr. Robot Series


>`shred -f -n 3 test.txt`


> ```
> f  = Forces the change of permission

>n  = overwirte times
> ```



