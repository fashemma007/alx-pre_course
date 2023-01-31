<h1 style="text-align: center;">
	<a href='https://intranet.alxswe.com/projects/284#quiz-completed'>
		0x13. Firewall
	</a>
</h1>

As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with `telnet IP PORT`. For example, if you want to check if port 22 is open on `web-02`:
```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```
We can see for this example that the connection is successful: `Connected to web-02.holberton.online.`

Now let’s try connecting to port 2222:
```
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
```
We can see that the connection never succeeds, so after some time I just use `ctrl+c` to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the school’s network, bypassing the firewall.

## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. Block all incoming traffic but](0-block_all_incoming_traffic_but)
- [**Advanced Task**](#advanced-task)
	- [1. Port forwarding](100-port_forwarding)

---



<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. Block all incoming traffic but

**Problem:** Let’s install the ufw firewall and setup a few rules on web-01.

**Requirements:**
* The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
	* 22 (SSH)
	* 443 (HTTPS SSL)
	* 80 (HTTP)
* Share the ufw commands that you used in your answer file
- [x] *File:* [0-block_all_incoming_traffic_but](0-block_all_incoming_traffic_but)

---

### Advanced Task

---
#### 1. Port forwarding
**Problem:** lorem ipsum

**Requirements:**
* My web server nginx is only listening on port 80
* netstat shows that nothing is listening on 8080

```
imitor＠excalibur» curl -I web-01.imitor.tech:8080
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 31 Jan 2023 09:47:59 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Wed, 18 Jan 2023 16:30:32 GMT
Connection: keep-alive
ETag: "63c81ea8-d"
X-Served-By: 74003-web-01
Accept-Ranges: bytes

```
- [x] *File:* [100-port_forwarding](100-port_forwarding)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
