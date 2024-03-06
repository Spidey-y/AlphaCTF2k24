#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win(long int param1, char *param2);
void disable_buffering(void);

int main(void)
{
    char buf[60];
    disable_buffering();
    printf("hi pwner can you get the flag ?");
    gets(buf);
}

void win(long int param1, char *param2)
{
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL)
    {
        printf("flag.txt not found \n");
        exit(0);
    }
    char buf[110];
    if (param1 == 0x13371337 && strncmp("Alphabit", param2, 7) == 0)
    {
        printf("GG here is your flag :\n");
        fgets(buf, 100, f);
        puts(buf);
        fclose(f);
    }
    else
    {
        puts("You failed !!");
        exit(0);
    }
    __asm__("pop %rdi ; ret");
    __asm__("pop %rsi ; ret");
}

void disable_buffering(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
