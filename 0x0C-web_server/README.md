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
	- [1. Install nginx web server](1-install_nginx_web_server)
	- [2. Setup a domain name](2-setup_a_domain_name)
	- [3. Redirection](3-redirection)
	- [4. Not found page 404](4-not_found_page_404)
- [Advanced Task](#advanced-task)
	- [5. Install Nginx web server (w/ Puppet)](7-puppet_install_nginx_web_server.pp)

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

#### 1. Install nginx web server

**Problem:** lorem ipsum

**Requirements:**
* Install `nginx` on your `web-01`
* server
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
* You can’t use `systemctl` for restarting `nginx`
```
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ ./0-transfer_file 1-install_nginx_web_server 54.89.25.106 ubuntu ~/.ssh/school 
1-install_nginx_web_server                                                                                100% 1266     4.1KB/s   00:00    
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ ssh ubuntu@54.89.25.106 -i ~/.ssh/school './1-install_nginx_web_server'

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:3 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Get:4 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Get:5 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [2303 kB]
Get:6 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 c-n-f Metadata [16.2 kB]
Get:7 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1013 kB]
Get:8 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/universe Translation-en [235 kB]
Get:9 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [1928 kB]
Get:10 http://security.ubuntu.com/ubuntu focal-security/main Translation-en [316 kB]
Get:11 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [782 kB]
Get:12 http://security.ubuntu.com/ubuntu focal-security/universe Translation-en [151 kB]
Fetched 7081 kB in 3s (2793 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
70 packages can be upgraded. Run 'apt list --upgradable' to see them.
Skipping adding existing rule
Skipping adding existing rule (v6)
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜        
```
- [x] [1-install_nginx_web_server](1-install_nginx_web_server)

#### 2. Setup a domain name

**Problem:** lorem ipsum

**Requirements:**
* provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
* configure your DNS records with an A entry so that your root domain points to your `web-01` IP address Warning: the propagation of your records can take time (~1-2 hours)
* go to your profile and enter your domain in the `Project website url` field

```
imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ dig imitor.tech           (↻ 20?⇡3)

; <<>> DiG 9.18.4-2ubuntu2-Ubuntu <<>> imitor.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 32590
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;imitor.tech.                   IN      A

;; ANSWER SECTION:
imitor.tech.            7200    IN      A       54.89.25.106

;; Query time: 475 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Thu Jan 12 16:01:40 WAT 2023
;; MSG SIZE  rcvd: 56

imitor＠excalibur»alx-system_engineering-devops/0x0C-web_server(master)➜ 
```
- [x] [2-setup_a_domain_name](2-setup_a_domain_name)

#### 3. Redirection
**Problem:** Configure your Nginx server so that /redirect_me is redirecting to another page.

**Requirements:**
* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```
- [x] [3-redirection](3-redirection)

#### 4. Not found page 404
**Problem:** Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

**Requirements:**
* The page must return an HTTP 404 error code
* The page must contain the string Ceci n'est pas une page
* Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task

```
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```
- [x] [4-not_found_page_404](4-not_found_page_404)

### Advanced Task

#### 5. Install Nginx web server (w/ Puppet)
**Problem:** Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

**Requirements:**
* Nginx should be listening on port 80
* When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
* The redirection must be a “301 Moved Permanently”
* Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
```
code sample
```
- [x] [7-puppet_install_nginx_web_server.pp](7-puppet_install_nginx_web_server.pp)



## Author

[Emmanuel Fasogba](fasogbaemmanuel@gmail.com)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)

