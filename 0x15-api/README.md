<h1 style="text-align: center;">
	<a href='https://intranet.alxswe.com/projects/269'>
		0x15. API
	</a>
</h1>

## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. Gather data from an API](0-gather_data_from_an_API.py)
	- [Task_1](link_to_file)
- [**Advanced Task**](#advanced-task)
	- [Task_013](link_to_file)
	- [Task_014](link_to_file)

---


<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. Gather data from an API

**Problem:** Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

**Requirements:**
* You must use `urllib` or `requests` module
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
	* First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
		* `EMPLOYEE_NAME`: name of the employee
		* `NUMBER_OF_DONE_TASKS`: number of completed tasks
		* `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
	* Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)
```
imitor＠excalibur»/0x15-api(master)➜ ./0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
         odit optio omnis qui sunt
         doloremque aut dolores quidem fuga qui nulla
         sint amet quia totam corporis qui exercitationem commodi
         sequi dolorem sed
         eum ipsa maxime ut
         tempore molestias dolores rerum sequi voluptates ipsum consequatur

imitor＠excalibur»/0x15-api(master)➜ ./0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T"
EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
TSoditSoptioSomnisSquiSsunt
TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TSsequiSdoloremSsed
TSeumSipsaSmaximeSut
TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
```
- [x] *File:* [0-gather_data_from_an_API.py](0-gather_data_from_an_API.py)

---

#### Task_1

**Problem:** 

**Requirements:**
* lorem_ipso
* lorem_ipso

```
code sample
```
- [ ] *File:* [Task_1](link_to_file)


---

#### Task_1

**Problem:** 

**Requirements:**
* lorem_ipso
* lorem_ipso

```
code sample
```
- [ ] *File:* [Task_1](link_to_file)


---

### Advanced Task

---
#### Task_013
**Problem:** 

**Requirements:**
* lorem_ipso

```
code sample
```
- [ ] *File:* [Task_13](link_to_file)

---

#### Task_014

**Problem:** 

**Requirements:**
* lorem_ipso

```
code sample
```
- [ ] *File:* [Task_14](link_to_file)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
