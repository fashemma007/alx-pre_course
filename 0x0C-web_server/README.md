# 0x0C-web_server
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
## Resources
* [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* [Nginx](https://en.wikipedia.org/wiki/Nginx)
* [Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
* [Root and Sub-domain](https://landingi.com/help/domains-vs-subdomains/)
* [HTTP Requests](https://www.tutorialspoint.com/http/http_methods.htm)
* [HTTP Redirects](https://moz.com/learn/seo/redirection)
* [Linux Log files](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
## Project Overview
- [Mandatory Task](#mandatory-task)
	- [0. Transfer a file to your server](0-transfer_file)
	- [Task - 1](link_to_fiel)
- [Advanced Task](#advanced-task)
	- [Task - 013](link_to_fiel)
	- [Task - 014](link_to_fiel)

## Tasks
### Mandatory Task

#### 0. Transfer a file to your server

**Problem:** Write a Bash script that transfers a file from our client to a server:

**Requirements:**
* Accepts 4 parameters
	- The path to the file to be transferred
	- The IP of the server we want to transfer the file to
	- The username `scp` connects with
	- The path to the SSH private key that `scp` uses
* Display Usage: `0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
* `scp` must transfer the file to the user home directory `~/`
* Strict host key checking must be disabled when using `scp`
```
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ ./0-transfer_file 0-transfer_file 54.89.25.106          (↻ 19?⇡1)
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ ./0-transfer_file 0-transfer_file 54.89.25.106 ubuntu ~/.ssh/school
0-transfer_file                                                                                           100%  707     2.2KB/s   00:00    
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ ssh ubuntu@54.89.25.106 -i ~/.ssh/school 'ls -lah ~/'   (↻ 19?⇡1)
total 40K
drwxr-xr-x 6 ubuntu ubuntu 4.0K Jan 12 03:06 .
drwxr-xr-x 3 root   root   4.0K Jan 11 17:19 ..
-rw------- 1 ubuntu ubuntu 1.1K Jan 12 03:05 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3.7K Feb 25  2020 .bashrc
drwx------ 2 ubuntu ubuntu 4.0K Jan 11 17:19 .cache
drwxrwxr-x 3 ubuntu ubuntu 4.0K Jan 11 17:30 .local
-rw-r--r-- 1 ubuntu ubuntu  807 Feb 25  2020 .profile
drwx------ 2 ubuntu ubuntu 4.0K Jan 11 17:19 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Jan 11 17:20 .sudo_as_admin_successful
drwxrwxr-x 2 ubuntu ubuntu 4.0K Jan 12 03:08 web_server
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ ssh ubuntu@54.89.25.106 -i ~/.ssh/school 'ls -lah ~/web_server'
total 12K
drwxrwxr-x 2 ubuntu ubuntu 4.0K Jan 12 03:08 .
drwxr-xr-x 6 ubuntu ubuntu 4.0K Jan 12 03:06 ..
-rwxrwxr-x 1 ubuntu ubuntu  707 Jan 12 03:08 0-transfer_file
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ 
```
- [x] [0-transfer_file](0-transfer_file)

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [x] [Task 1](link_to_file)


### Advanced Task

#### Task - 013
**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [x] [Task 1](link_to_file)

#### Task - 014

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [x] [Task 1](link_to_file)


## Author

[Emmanuel Fasogba](fasogbaemmanuel@gmail.com)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)

