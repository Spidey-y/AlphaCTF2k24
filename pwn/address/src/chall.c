#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void play(void);
void disable_buffering(void);

long members[36];
char *msg = "Thanks for helping have a good day";

int main()
{
    disable_buffering();
    puts("Welcome to my app you can add some members!");
    printf("%p\n", printf);
    play();
    play();
    puts(msg);
}

void play(void)
{
    int member = 0;
    char value[28];
    long val;
    puts("Enter the index: ");
    scanf("%d", &member);
    puts("Enter the member id: ");
    read(0, value, 16);
    members[member] = strtoul(value, NULL, 10);
    printf("the new member is %p\n", members[member]);
}

void disable_buffering(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}