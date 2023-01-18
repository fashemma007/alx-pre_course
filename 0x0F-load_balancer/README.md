<h1 style="text-align: center;">0x0F. Load balancer</h1>

You have been given 2 additional servers:
	* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
	* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.


## Resources
* [HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
* [HTTP Header](https://www.techopedia.com/definition/27178/http-header)
* [Install HAProxy](https://haproxy.debian.net/)


## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. Double the number of webservers](link_to_file)
	- [Task - 1](link_to_file)
- [**Advanced Task**](#advanced-task)
	- [Task - 013](link_to_file)
	- [Task - 014](link_to_file)

---



<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. Double the number of webservers

**Problem:** In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.



**Requirements:**
* lorem ipsum
* lorem ipsum

```
imitor＠excalibur»~➜ curl -I 54.89.25.106
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Wed, 18 Jan 2023 16:21:31 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Wed, 18 Jan 2023 16:18:00 GMT
Connection: keep-alive
ETag: "63c81bb8-d"
X-Served-By: 74003-web-01
Accept-Ranges: bytes

imitor＠excalibur»~➜ curl -I 52.3.241.66
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Wed, 18 Jan 2023 16:21:42 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Wed, 18 Jan 2023 16:16:03 GMT
Connection: keep-alive
ETag: "63c81b43-d"
X-Served-By: 74003-web-02
Accept-Ranges: bytes

```
- [ ] *File:* [Task 0](link_to_file)

---

#### Task

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)


---

### Advanced Task

---
#### Task - 013
**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)

---

#### Task - 014

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task 1](link_to_file)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
