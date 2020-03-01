// This is an example of fork, fork creates a child process, 
// which is (almost) the same as the parent proces,
// but instead of strat running at the very beginning,
// it will start where the fork has done.
// the return value of fork() will be 0 for child process,
// but for parent process, it's the pid of the child process.

// This program is not deterministic, because either parent or
// child process can be scheduled first.
// For a deterministic program, look at p2.c

#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>

int main(int argc, char *argv[])
{
	printf("hello world (pid:%d)\n", (int)getpid());
	int rc = fork(); // rc stand for return code, for child it's 0, 
					 // for parent it's the pid of the child
					 // child process will start running from below
	if (rc < 0)
	{
		// fork failed
		fprintf(stderr, "fork failed\n");
		exit(1);
	}
	else if (rc == 0)
	{ // child (new process)
		printf("hello, I am child (pid:%d)\n", (int)getpid());
	}
	else
	{
		// parent goes down this path (main)
		printf("hello, I am parent of %d (pid:%d)\n", rc, (int)getpid());
	}
	return 0;
}
