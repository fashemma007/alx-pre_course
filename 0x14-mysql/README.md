<h1 style="text-align: center;">
	<a href='https://intranet.alxswe.com/projects/280'>
		0x14. MySQL
	</a>
</h1>

Setting Up MYSQL servers on web servers

For ease, I simply copied the files where I already had the commands written in
to both webservers and executed them.

## Resources
* [What is a Database](https://www.techtarget.com/searchdatamanagement/definition/database)
* [MYSQL Replication](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [Set Up Replication in MySQL](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Robust Backup Strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)


## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. Install MySQL](install_mysql_5_7)
	- [1. Let us in!](create_users)
	- [2. If only you could see what I've seen with your eyes](prepare_for_repl)
	- [3. Quite an experience to live in fear, isn't it?](user_replica)
	- [4. Setup a Primary-Replica infrastructure using MySQL](4-mysql_configuration_replica)
	- [_file_](link_to_file)
	- [_file_](link_to_file)
- [**Advanced Task**](#advanced-task)
	- [Task_013](link_to_file)
	- [Task_014](link_to_file)

---

<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. Install MySQL

**Problem:** First things first, let’s get MySQL installed on both your web-01 and web-02 servers.

**Requirements:**
* MySQL distribution must be 5.7.x

- [x] *File:* [install_mysql_5_7](install_mysql_5_7)

---

#### 1. Let us in!

**Problem:** In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

**Requirements:**
* Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to localhost and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
* Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
* In addition to that, make sure that `task #3` of your `SSH project` is completed for `web-01` and `web-02`. You will likely need to add the public key to `web-02` as you only added it to `web-01` for this project. The checker will connect to your servers to check MySQL status
```
ubuntu@74003-web-02:~$ ./create_user 
Enter password: 
ubuntu@74003-web-02:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password: 
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@74003-web-02:~$ 

```
- [x] *File:* [create_users](create_users)

---

#### 2. If only you could see what I've seen with your eyes

**Problem:** In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

**Requirements:**
* Create a database named `tyrell_corp`.
* Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
* Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.

```
ubuntu@74003-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password: 
+------+----------+
| id   | name     |
+------+----------+
|    1 | Emmanuel |
+------+----------+
ubuntu@74003-web-01:~$ 
```
- [x] *File:* [prepare_for_repl](prepare_for_repl)

---

#### 3. Quite an experience to live in fear, isn't it?

**Problem:** Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.

**Requirements:**
* The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
* `replica_user` must have the appropriate permissions to replicate your primary MySQL server.
* `holberton_user` will need SELECT privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.

```
ubuntu@74003-web-01:~$ ./user_replica 
Enter password: 
ubuntu@74003-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
Enter password: 
+----------------+-----------------+
| user           | Repl_slave_priv |
+----------------+-----------------+
| root           | Y               |
| mysql.session  | N               |
| mysql.sys      | N               |
| holberton_user | N               |
| replica_user   | Y               |
+----------------+-----------------+
ubuntu@74003-web-01:~$ 
```
- [x] *File:* [user_replica](user_replica)

---
#### 4. Setup a Primary-Replica infrastructure using MySQL

- [x] *Files:* [4-mysql_configuration_primary](4-mysql_configuration_primary),[4-mysql_configuration_replica](4-mysql_configuration_replica)

---
#### task_

**Problem:** 

**Requirements:**
* 

```
```
- [x] *File:* [file](file)

---

### Advanced Task

---
#### Task_013
**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task_13](link_to_file)

---

#### Task_014

**Problem:** lorem ipsum

**Requirements:**
* lorem ipsum
* lorem ipsum

```
code sample
```
- [ ] *File:* [Task_14](link_to_file)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
