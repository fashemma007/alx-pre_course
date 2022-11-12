#include <unistd.h>/*to call the sleep function*/
#include <stdio.h> /*to call the printf function*/
#include <stdlib.h>/*to call the exit function*/

/**
 * infini_tea - creates an infinite loop
 * Return: 0
 */

int infini_tea(void)
{
	while (1) /*since we don't have bool by default, we use 1 as true*/
	{
		/* sleep fot a second */
		sleep(1);
	}
	return (0);
}
/**
 * main - creates 5 zombie processes
 * Return: infini_tea zombies
 */
int main(void)
{
	pid_t zombiePID; /*create a pid type variable*/
	unsigned int i;

	for (i = 0; i < 5; i++) /*a loop that runs 5 times*/
	{
		zombiePID = fork(); /*for each loop, fork the process*/
		/*forking it creates a child process*/
		if (zombiePID == 0) /*if the PID is 0, exit*/
			exit(0);
		else
		{
			printf("Zombie Process created, PID: %d\n", zombiePID);
		}
	}
	return (infini_tea());
}
