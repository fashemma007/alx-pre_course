# 0x0B. SSH

project description ...
## Resources
* [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)

## Project Overview
- [Mandatory Task](#mandatory-task)
	- [0. Use a private key](0-use_a_private_key)
	- [1. Create an SSH key pair](1-create_ssh_key_pair)
	- [2. Client configuration file]()
- [Advanced Task](#advanced-task)
	- Task - 013
	- Task - 014


## Tasks
### Mandatory Task

#### 0. Use a private key

**Problem:** Write a Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user ubuntu.

**Requirements:**
* Only use ssh single-character flags
* You cannot use -l
* You do not need to handle the case of a private key protected by a passphrase
```
imitor＠excalibur»alx-system_engineering-devops/0x0B-ssh(master)➜ ./0-use_a_private_key 
ubuntu@74003-web-01:~$ exit
logout
Connection to 54.167.187.57 closed.
imitor＠excalibur»alx-system_engineering-devops/0x0B-ssh(master)➜  
```

- [x] [0-use_a_private_key](0-use_a_private_key)

#### 1. Create an SSH key pair
**Problem:** Write a Bash script that creates an RSA key pair.

**Requirements:**
* Name of the created private key must be school
* Number of bits in the created key to be created 4096
* The created key must be protected by the passphrase betty
```
imitor＠excalibur»alx-system_engineering-devops/0x0B-ssh(master)➜ ./1-create_ssh_key_pair                                   (↻ 20?⇡2)
Generating public/private rsa key pair.
Your identification has been saved in school
Your public key has been saved in school.pub
The key fingerprint is:
SHA256:eFRogXlABwvGWENv05rEy6LCtOoLIMzgWVE2TVk9Hdo imitor@excalibur
The key's randomart image is:
+---[RSA 4096]----+
|   *B=**=+o ...  |
|  ..+=+*+. oo.   |
|.  .  Boo  ..E   |
|= o  + B         |
|o*  . * S        |
|= .. . .         |
|oo.              |
|o.               |
|oo.              |
+----[SHA256]-----+
imitor＠excalibur»alx-system_engineering-devops/0x0B-ssh(master)➜   
```
- [x] [1-create_ssh_key_pair](1-create_ssh_key_pair)

#### Task - 1

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] [File]()

### Advanced Task

#### [Task - 013](./filename)
**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] [File]()

#### [Task - 014](./filename)

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] [File]()


## Author

[Emmanuel Fasogba](fasogbaemmanuel@gmail.com)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)

