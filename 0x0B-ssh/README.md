# 0x0B. SSH

project description ...
## Resources
* [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)

## Project Overview
- [Mandatory Task](#mandatory-task)
	- [0. Use a private key](0-use_a_private_key)
	- [1. Create an SSH key pair](1-create_ssh_key_pair)
	- [2. Client configuration file]()
	- [3. Let me in!]()
- [Advanced Task](#advanced-task)
	- [4. Client configuration file (w/ Puppet)](100-puppet_ssh_config.pp)


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

#### 2. Client configuration file

**Problem:** Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

**Requirements:**
* Your SSH client configuration must be configured to use the private key `~/.ssh/school`
* Your SSH client configuration must be configured to refuse to authenticate using a password

```
imitor＠excalibur»alx-system_engineering-devops/0x0B-ssh(master)➜ ssh -v ubuntu@54.167.187.57                                (↻ 20⇡4)
OpenSSH_9.0p1 Ubuntu-1ubuntu7.1, OpenSSL 3.0.5 5 Jul 2022
debug1: Reading configuration data /home/imitor/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 54.167.187.57 [54.167.187.57] port 22.
debug1: Connection established.
debug1: identity file /home/imitor/.ssh/id_rsa type 0
debug1: Local version string SSH-2.0-OpenSSH_9.0p1 Ubuntu-1ubuntu7.1
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
debug1: Host '54.167.187.57' is known and matches the ED25519 host key.
debug1: Found key in /home/imitor/.ssh/known_hosts:17
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: get_agent_identities: bound agent to hostkey
debug1: get_agent_identities: agent returned 1 keys
debug1: Will attempt key: /home/imitor/.ssh/id_rsa RSA SHA256:Vfs5rI2lUzvX32zxFysG1bhz8yDUiIeFUCDpm8AYTlE agent
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1021-aws x86_64)
ubuntu@74003-web-01:~$ 
```
- [x] [2-ssh_config](2-ssh_config)
#### 3. Let me in!
**Problem:** Now that you have successfully connected to your server, we would also like to join the party.

**Requirements:**
* Add the SSH public key below to your server so that we can connect using the `ubuntu` user.
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```
- [x] Done

### Advanced Task
#### 4. Client configuration file (w/ Puppet)

**Problem:** Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

**Requirements:**
* Your SSH client configuration must be configured to use the private key `~/.ssh/school`
* Your SSH client configuration must be configured to refuse to authenticate using a password

```
vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
vagrant@ubuntu:~$
```
- [ ] [100-puppet_ssh_config.pp](100-puppet_ssh_config.pp)


## Author

[Emmanuel Fasogba](fasogbaemmanuel@gmail.com)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
