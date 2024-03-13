#include<stdio.h>
#include<string.h>

char l1v3_sp3ll[200] = "Expelliarmus\x00\x00\x00\x00";
char d34th_sp3ll[200] = "Avada Kedavra\x00\x00\x00\x00";

void init() {                                                                         
    setvbuf(stdout, 0, 2, 0);                                                         
    setvbuf(stdin, 0, 2, 0);                                                          
}   

void swp(char **str1, char **str2) {
    char *temp = *str1;
    *str1 = *str2;
    *str2 = temp;
}


void swapStrings(char *str1, char *str2) {
    // Assuming both strings have the same length
    while (*str1 != '\0' && *str2 != '\0') {
        // Swap characters
        char temp = *str1;
        *str1 = *str2;
        *str2 = temp;

        // Move to the next characters in each string
        str1++;
        str2++;
    }
}

void main(int argc, char const *argv[])
{   
    char defend[32];
    init();
    printf("you know the sp3ll!!\n");
    
    if(!strcmp(l1v3_sp3ll,"voldemort")){
        printf("you've got to mean it");
        fgets(l1v3_sp3ll,200,stdin);
        
    }
    printf("What's your name, brave wizard?\n");
    swapStrings(l1v3_sp3ll,d34th_sp3ll);
    fgets(defend,0x32,stdin);
    printf(d34th_sp3ll);
    return 0;
}