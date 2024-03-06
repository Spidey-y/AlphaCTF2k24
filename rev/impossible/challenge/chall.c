#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void wrong()
{
    puts("WRONG!");
    exit(-1);
}

int main(int argc, char const *argv[])
{
    char buf[60];
    puts("What's the passcode");

    if (read(0, buf, sizeof(buf)) < 0)
    {
        wrong();
    }

    if ((((*(buf + 23)) | 0x100) != 368))
    {
        wrong();
    }
    if (((*(buf + 4)) | 0xe) != 111)
    {
        wrong();
    }
    if (((*(buf + 5)) ^ 'e') != 23)
    {
        wrong();
    }
    if (((*(buf + 6)) | 'G') != 103)
    {
        wrong();
    }
    if (((*(buf + 7)) & 'a') != 32)
    {
        wrong();
    }
    if (((((*(buf + 8)) + (*(buf + 10))) * (*(buf + 15)))) != 4384)
    {
        wrong();
    }
    if (((((*(buf + 11)) << 3) + (*(buf + 16))) - (*(buf + 54))) != 985)
    {

        printf("aaaaaaa\n");
        wrong();
    }
    if (((*(buf + 8)) | 'R') != 123)
    {

        wrong();
    }
    if (((*(buf + 9)) ^ 'W') != 36)
    {

        wrong();
    }
    if (((*(buf + 10)) | 'i') != 105)
    {

        wrong();
    }
    if (((*(buf + 11)) & 'd') != 96)
    {

        wrong();
    }
    if (((*(buf + 17)) ^ 'K') != 39)
    {

        wrong();
    }
    if (((*(buf + 18)) | 's') != 115)
    {

        wrong();
    }
    if (((*(buf + 19)) & 'e') != 101)
    {

        wrong();
    }
    if ((((*(buf + 58)) << 0xa) * (*(buf + 1))) != 5670912)
    {

        wrong();
    }
    if (((*(buf + 59)) & '}') != 125)
    {

        wrong();
    }

    if (((((*(buf + 4)) - (*(buf + 7))) * (*(buf + 12))) + (*(buf + 52))) != 7728)
    {

        wrong();
    }
    if (((*(buf + 20)) | 'u') != 127)
    {

        wrong();
    }
    if (((*(buf + 21)) ^ 'p') != 49)
    {

        wrong();
    }

    if (((((*(buf + 4)) - (*(buf + 7))) * (*(buf + 12))) + (*(buf + 52))) != 7728)
    {

        wrong();
    }

    if (((*(buf + 3)) & 0x13) != 0)
    {

        wrong();
    }
    if (((((*(buf + 18)) << 3) + (*(buf + 24))) - (*(buf + 30))) != 803)
    {

        wrong();
    }
    if (((((*(buf + 32)) << 6) - (*(buf + 35))) * (*(buf + 40))) != 422655)
    {

        wrong();
    }
    if (((((*(buf + 26)) ^ (*(buf + 27))) - (*(buf + 51))) + (*(buf + 36))) != 22)
    {

        wrong();
    }
    if (((((*(buf + 19)) ^ (*(buf + 23))) - (*(buf + 26))) + (*(buf + 38))) != 11)
    {

        wrong();
    }
    if (((((*(buf + 43)) + (*(buf + 36))))) != 164)
    {

        wrong();
    }
    if (((((*(buf + 18)) + (*(buf + 55))) ^ (*(buf + 46))) ^ (*(buf + 36))) != 174)
    {

        wrong();
    }

    if (((((*(buf + 43)) + (*(buf + 36))))) != 164)
    {

        wrong();
    }
    if (((((*(buf + 47)) + (*(buf + 38))))) != 104)
    {

        wrong();
    }

    if ((((*(buf + 19)) ^ (*(buf + 42))) << 7) != 7936)
    {

        wrong();
    }
    if (((*(buf + 23)) & 'A') != 64)
    {

        wrong();
    }
    if (((*(buf + 24)) | 'z') != 122)
    {

        wrong();
    }
    if (((*(buf + 25)) ^ 0x10) != 113)
    {

        wrong();
    }
    if (((*(buf + 26)) | 0xd) != 79)
    {

        wrong();
    }
    if (((*(buf + 27)) & 'X') != 80)
    {

        wrong();
    }
    if (((*(buf + 28)) | 'Q') != 87)
    {

        wrong();
    }
    if (((*(buf + 29)) ^ 'h') != 19)
    {

        wrong();
    }
    if (((*(buf + 30)) | 'I') != 77)
    {

        wrong();
    }
    if (((*(buf + 31)) & 'O') != 4)
    {

        wrong();
    }
    if (((*(buf + 32)) | 'n') != 111)
    {

        wrong();
    }
    if (((*(buf + 33)) ^ 0x11) != 32)
    {

        wrong();
    }
    if (((*(buf + 34)) | 0xf) != 79)
    {

        wrong();
    }
    if (((*(buf + 35)) & 'M') != 77)
    {

        wrong();
    }
    if (((*(buf + 36)) | 'f') != 119)
    {

        wrong();
    }
    if (((*(buf + 37)) ^ 'a') != 40)
    {

        wrong();
    }
    if (((*(buf + 38)) | 'A') != 119)
    {

        wrong();
    }
    if (((*(buf + 39)) & 'r') != 96)
    {

        wrong();
    }
    if (((*(buf + 40)) | 'q') != 127)
    {

        wrong();
    }
    if (((*(buf + 41)) ^ 's') != 32)
    {

        wrong();
    }
    if (((*(buf + 42)) | 'o') != 127)
    {

        wrong();
    }
    if (((*(buf + 43)) & 0x12) != 0)
    {

        wrong();
    }
    if (((*(buf + 44)) | 0xc) != 78)
    {

        wrong();
    }
    if (((*(buf + 45)) ^ 'v') != 70)
    {

        wrong();
    }
    if (((*(buf + 46)) | 't') != 124)
    {

        wrong();
    }
    if (((*(buf + 47)) & 'h') != 32)
    {

        wrong();
    }
    if (((*(buf + 48)) | 'e') != 103)
    {

        wrong();
    }
    if (((*(buf + 49)) ^ 'c') != 60)
    {

        wrong();
    }
    if (((*(buf + 50)) | 'H') != 77)
    {

        wrong();
    }
    if (((((*(buf + 18)) << 3) + (*(buf + 24))) - (*(buf + 30))) != 803)
    {

        wrong();
    }
    if (((*(buf + 51)) & 'V') != 80)
    {

        wrong();
    }
    if (((((*(buf + 32)) << 6) - (*(buf + 35))) * (*(buf + 40))) != 422655)
    {

        wrong();
    }
    if (((((*(buf + 26)) ^ (*(buf + 27))) - (*(buf + 51))) + (*(buf + 36))) != 22)
    {

        wrong();
    }
    if (((((*(buf + 19)) ^ (*(buf + 23))) - (*(buf + 26))) + (*(buf + 38))) != 11)
    {

        wrong();
    }
    if (((((*(buf + 43)) + (*(buf + 36))))) != 164)
    {

        wrong();
    }
    if (((((*(buf + 18)) + (*(buf + 55))) ^ (*(buf + 46))) ^ (*(buf + 36))) != 174)
    {

        wrong();
    }

    if (((*(buf + 52)) | 'g') != 103)
    {

        wrong();
    }
    if (((*(buf + 53)) ^ 'S') != 16)
    {

        wrong();
    }
    if (((*(buf + 54)) | 'm') != 125)
    {

        wrong();
    }
    if (((*(buf + 55)) & 0x14) != 20)
    {

        wrong();
    }
    if (((*(buf + 56)) << 0xb) != 149504)
    {

        wrong();
    }
    if (((*(buf + 57)) ^ 'k') != 36)
    {

        wrong();
    }
    if ((((*(buf + 58)) << 0xa) * (*(buf + 1))) != 5670912)
    {

        wrong();
    }
    if (((*(buf + 59)) & '}') != 125)
    {

        wrong();
    }

    if (((((*(buf + 4)) - (*(buf + 7))) * (*(buf + 12))) + (*(buf + 52))) != 7728)
    {

        wrong();
    }

    if (((*(buf + 9)) ^ 'W') != 36)
    {

        wrong();
    }
    if (((*(buf + 11)) & 'd') != 96)
    {

        wrong();
    }
    if (((*(buf + 17)) ^ 'K') != 39)
    {

        wrong();
    }
    if (((*(buf + 18)) | 's') != 115)
    {

        wrong();
    }
    if (((*(buf + 19)) & 'e') != 101)
    {

        wrong();
    }
    if ((((*(buf + 58)) << 0xa) * (*(buf + 1))) != 5670912)
    {

        wrong();
    }
    if (((*(buf + 59)) & '}') != 125)
    {

        wrong();
    }
    if (((*(buf + 20)) | 'u') != 127)
    {

        wrong();
    }
    if (((*(buf + 21)) ^ 'p') != 49)
    {

        wrong();
    }
    if (((*(buf + 0)) + (*(buf + 3)) + (*(buf + 6)) + (*(buf + 9)) + (*(buf + 12)) + (*(buf + 15))) != 534)
    {

        wrong();
    }
    if (((*(buf + 22)) | 'A') != 109)
    {

        wrong();
    }
    if (((*(buf + 2)) + (*(buf + 5)) + (*(buf + 8)) + (*(buf + 11)) + (*(buf + 14)) + (*(buf + 17))) != 594)
    {

        wrong();
    }
    if (((((*(buf + 4)) - (*(buf + 7))) * (*(buf + 12))) + (*(buf + 52))) != 7728)
    {

        wrong();
    }
    if (((*(buf + 12)) | 'B') != 111)
    {

        wrong();
    }

    if (((*(buf + 23)) & 'A') != 64)
    {

        wrong();
    }
    if (((*(buf + 24)) | 'z') != 122)
    {

        wrong();
    }
    if (((*(buf + 13)) ^ '3') != 70)
    {

        wrong();
    }
    if (((*(buf + 14)) | 'L') != 126)
    {

        wrong();
    }
    if (((*(buf + 15)) & '6') != 32)
    {

        wrong();
    }
    if (((*(buf + 16)) | 'b') != 102)
    {

        wrong();
    }
    if ((((*(buf + 1)) ^ (*(buf + 38))) << 7) != 14336)
    {

        wrong();
    }
    if (((((*(buf + 51)) ^ (*(buf + 48))) + (*(buf + 46)))) != 103)
    {

        wrong();
    }
    if ((((*(buf + 1)) ^ (*(buf + 42))) << 7) != 3840)
    {

        wrong();
    }
    if ((((*(buf + 19)) ^ (*(buf + 42))) << 7) != 7936)
    {

        wrong();
    }
    if ((((*(buf + 20)) ^ (*(buf + 59))) << 7) != 9088)
    {

        wrong();
    }

    if (((*(buf + 0)) | 'T') != 87)
    {

        wrong();
    }
    if (((*(buf + 1)) | 'Z') != 95)
    {

        wrong();
    }
    if (((*(buf + 2)) | 'c') != 99)
    {

        wrong();
    }
    if (((*(buf + 3)) & 0x13) != 0)
    {

        wrong();
    }
    if (((((*(buf + 18)) << 3) + (*(buf + 24))) - (*(buf + 30))) != 803)
    {

        wrong();
    }
    if (((((*(buf + 32)) << 6) - (*(buf + 35))) * (*(buf + 40))) != 422655)
    {

        wrong();
    }
    if (((((*(buf + 26)) ^ (*(buf + 27))) - (*(buf + 51))) + (*(buf + 36))) != 22)
    {

        wrong();
    }
    if (((((*(buf + 19)) ^ (*(buf + 23))) - (*(buf + 26))) + (*(buf + 38))) != 11)
    {

        wrong();
    }
    if (((((*(buf + 43)) + (*(buf + 36))))) != 164)
    {

        wrong();
    }
    if (((((*(buf + 18)) + (*(buf + 55))) ^ (*(buf + 46))) ^ (*(buf + 36))) != 174)
    {

        wrong();
    }

    if (((((*(buf + 43)) + (*(buf + 36))))) != 164)
    {

        wrong();
    }
    if (((((*(buf + 47)) + (*(buf + 38))))) != 104)
    {

        wrong();
    }

    if ((((*(buf + 19)) ^ (*(buf + 42))) << 7) != 7936)
    {

        wrong();
    }
    if ((((*(buf + 20)) ^ (*(buf + 59))) << 7) != 9088)
    {

        wrong();
    }
    if ((((*(buf + 34)) <= 65)))
    {

        wrong();
    }

    if ((((*(buf + 23)) < 97)))
    {

        wrong();
    }
    if ((((*(buf + 16)) < 97)))
    {

        wrong();
    }
    if ((((*(buf + 34)) << 0x7) != 8576))
    {

        wrong();
    }
    if ((((*(buf + 39)) ^ (*(buf + 34))) != 43))
    {

        wrong();
    }

    if ((((*(buf + 27)) << 9) != 43008))
    {
        wrong();
    }
    if ((((*(buf + 57)) | 63) != 127))
    {
        wrong();
    }

    if (((*(buf + 54)) ^ 'c') != 54)
    {
        wrong();
    }
    if (((*(buf + 55)) | 'H') != 92)
    {

        wrong();
    }
    if (((((*(buf + 56)) << 3) + (*(buf + 57))) - (*(buf + 58))) != 585)
    {

        wrong();
    }
    if (((*(buf + 59)) & 'V') != 84)
    {
        wrong();
    }
    puts("GG, You got it!");

    return 0;
}
