<h1 style="text-align: center;">
	<a href='https://intranet.alxswe.com/projects/287'>
		0x12. Web stack debugging #2
	</a>
</h1>
The user `root` is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the `root` user, as if you fat finger a command and for example run `rm -rf /`, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the `root` user can do, just need to use a specific command that you need to discover.
* Sudo privileges
* Running commands as other users

## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. Run software as another user](0-iamsomeoneelse)
	- [1. Run Nginx as Nginx](1-run_nginx_as_nginx)
- [**Advanced Task**](#advanced-task)
	- [2. 7 lines or less](100-fix_in_7_lines_or_less)


---

<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. Run software as another user

**Problem:** For the containers that you are given in this project as well as the checker, everything is run under the `root` user, which has the ability to run anything as another user.

**Requirements:**
* write a Bash script that accepts one argument
* the script should run the `whoami` command under the user passed as an argument
* make sure to try your script by passing different users
```
root@7a9ac7c35d28:/home/nginx# ./0-iamsomeoneelse nginx
nginx
root@7a9ac7c35d28:/home/nginx# ./0-iamsomeoneelse www-data
www-data
root@7a9ac7c35d28:/home/nginx# ./0-iamsomeoneelse www     
sudo: unknown user: www
sudo: unable to initialize policy plugin
root@7a9ac7c35d28:/home/nginx# ./0-iamsomeoneelse root
root
root@7a9ac7c35d28:/home/nginx# 
```
- [x] *File:* [0-iamsomeoneelse](0-iamsomeoneelse)

---

#### 1. Run Nginx as Nginx

**Problem:** The `root` user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as `root`. With this in mind, it’s a good practice not to run your web servers as `root` (which is the default for most configurations) and instead run the process as the less privileged `nginx` user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the `nginx` user.

Fix this container so that Nginx is running as the `nginx` user.

**Requirements:**
* `nginx` must be running as `nginx` user
* `nginx` must be listening on all active IPs on port `8080`
* You cannot use `apt-get remove`
* Write a Bash script that configures the container to fit the above requirements

- [x] *File:* [1-run_nginx_as_nginx](1-run_nginx_as_nginx)

---

### Advanced Task

---
#### 2. 7 lines or less
**Problem:** Using what you did for task #1, make your fix short and sweet.

**Requirements:**
* Your Bash script must be 7 lines long or less
* There must be a new line at the end of the file
* You respect Bash script requirements
* You cannot use `;`, `&&` or `wget`
* You cannot execute your previous answer file (Do not include the name of the previous script in this one)

- [ ] *File:* [100-fix_in_7_lines_or_less](100-fix_in_7_lines_or_less)

---


<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
