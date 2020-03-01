// This program is almost the same as p1,
// except that parent process will wait child process to finish,
// thus it's deterministic

#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("hello world (pid:%d)\n", (int)getpid());
    int rc = fork();
    if (rc < 0)
    {
        // fork failed; exit
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
        int rc_wait = wait(NULL); // This is how parent wait for child process to finish,
                                  // the call seems weird to me, since it did not specify what to wait for
                                  // but it's just how it works... and wait(NULL) will return child process's pid
        printf("hello, I am parent of %d (rc_wait:%d) (pid:%d)\n", rc, rc_wait, (int)getpid());
    }
    return 0;
}