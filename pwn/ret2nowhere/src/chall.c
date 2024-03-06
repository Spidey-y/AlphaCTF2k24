#include<stdio.h>


size_t vuln(){
    char input[64];
    return read(0,input,200);
}

int main(int argc, char const *argv[])
{
    vuln();
    return 0;
}
