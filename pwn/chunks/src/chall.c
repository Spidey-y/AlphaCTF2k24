#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Team
{
    char *teamName;
    int voter_number;
};

struct Team *teams[4];
struct Team *initial_teams[4] = {
    &(struct Team){"", 1},
    &(struct Team){"", 2},
    &(struct Team){"", 3},
    &(struct Team){"", 4},
};

void menu(void);
void init_teams(void);

void vote_for_a_team(void);
int real_madrid_win(void);
void print_flag();
void disable_buffering(void);

int main(void)
{
    disable_buffering();
    init_teams();
    menu();
    vote_for_a_team();
    real_madrid_win();
    exit(0);
}

void menu(void)
{
    printf("Welcome to my app we are voting for the best team in the world\n");
    printf("here is a hint of the club that will win : https://www.youtube.com/watch?v=lF6wtA3TDv0 \n");
    printf("PS: I am fan of real madrid so i will never let any other team win\n");
}
void init_teams(void)
{
    printf("here is your gift:\n");
    for (int i = 0; i < 4; i++)
    {
        teams[i] = malloc(sizeof(struct Team));
        teams[i]->teamName = malloc(20);
    };

    for (int i = 0; i < 4; i++)
    {
        strcpy(teams[i]->teamName, initial_teams[i]->teamName);
        printf("%p\n", teams[i]->teamName);
        teams[i]->voter_number = initial_teams[i]->voter_number;
    }
}

void vote_for_a_team(void)
{
    printf("i will give you the honor to be the first one to vote: \n");
    scanf("%s", teams[0]->teamName);
}

int real_madrid_win(void)
{
    char *flag;
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(teams[i]->teamName, "real_madrid") != 0 || (teams[i]->voter_number != i + 1))
        {
            printf(">>> To make real madrid wins all 4 people must vot for it\n");
            return 1;
        }
    }
    print_flag();
}

void print_flag()
{

    FILE *f = fopen("flag.txt", "r");
    char buf[110];
    if (f == NULL)
    {
        printf("flag.txt not found \n");
        exit(0);
    }
    printf("GG here is your flag : \n");
    fgets(buf, 100, f);
    printf(buf);
    fclose(f);
}

void disable_buffering(void)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
