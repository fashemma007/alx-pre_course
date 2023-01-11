# 0x0A. Configuration management

project description ...

## Resources
* [name 1](https://www.1)
* [name 2](https://www.2)
* [name 3](https://www.3)

## Project Overview
- [Mandatory Task](#mandatory-task)
	- [0. Create a file](0-create_a_file.pp)
	- [1. Install a package](1-install_a_package.pp)
	- [2. Execute a command](2-execute_a_command.pp)
- [Advanced Task](#advanced-task)
	- [Task - 013](link_to_fiel)
	- [Task - 014](link_to_fiel)

## Tasks
### Mandatory Task

#### 0. Create a file

**Problem:** Using Puppet, create a file in /tmp.

**Requirements:**
* File path is `/tmp/school`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

```
imitor＠excalibur»alx-system_engineering-devops/0x0A-configuration_management(master)➜ sudo puppet apply 0-create_a_file.pp                                  (↻ 19?)
Notice: Compiled catalog for excalibur in environment production in 0.01 seconds
Notice: /Stage[main]/Main/File[/tmp/school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Applied catalog in 0.01 seconds
imitor＠excalibur»alx-system_engineering-devops/0x0A-configuration_management(master)➜                           
imitor＠excalibur»~✗ cat /tmp/school                                                                                                3.10.7
I love Puppet% 
```
- [x] [0-create_a_file.pp](0-create_a_file.pp)

#### 1. Install a package

**Problem:** Using Puppet, install `flask` from `pip3`.

**Requirements:**
* Install `flask`
* Version must be `2.1.0`

```
code sample
```
- [x] [1-install_a_package.pp](1-install_a_package.pp)

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

