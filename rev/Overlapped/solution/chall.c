#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  FILE *file;
  char c;
  char binary[9] = {'\0'};
  char *binaryData = NULL;
  char *byteList = NULL;
  char *shuffledList = NULL;
  char *newShuffledList = NULL;
  char *overlappedList = NULL;

  size_t dataSize = 0;

  // Open file
  file = fopen("flag.txt", "r");

  if (file == NULL)
  {
    printf("Could not open the file\n");
    return 1;
  }

  // Read file character by character, convert to binary, and save in a variable
  while ((c = fgetc(file)) != EOF)
  {
    for (int i = 7; i >= 0; i--)
    {
      binary[7 - i] = ((c >> i) & 1) ? '1' : '0';
    }
    binary[8] = '\0'; // Null-terminate the string
    dataSize += 8;
    binaryData = realloc(binaryData, dataSize);
    strcat(binaryData, binary);
  }

  // Close file
  fclose(file);

  printf("Over and Over Over lappppppppp\n");

  // Convert binary string to list of characters
  int binaryLength = strlen(binaryData);
  shuffledList = (char *)malloc((int)binaryLength / 8 * sizeof(char) + 1);

  int i;
  char *shuffledbinary = (char *)malloc(binaryLength * sizeof(char) + 1);
  // zero out the memory
  memset(shuffledbinary, 0, binaryLength * sizeof(char) + 1);

  for (int k = 0; k < (int)binaryLength / 64; k++)
  {
    for (i = 0; i < 8; ++i)
    {
      for (int j = 0; j < 8; ++j)
      {
        shuffledList[i * 8 + j] = binaryData[k * 64 + j * 8 + i];
      }
    }
    strcat(shuffledbinary, shuffledList);
  }

  byteList = (char *)malloc(binaryLength * sizeof(char) + 1); // Allocate memory for the char list

  for (size_t i = 0; i < binaryLength / 8; ++i)
  {
    byteList[i] = 0;
    for (size_t j = 0; j < 8; ++j)
    {
      byteList[i] = byteList[i] << 1;
      byteList[i] += shuffledbinary[i * 8 + j] - '0';
    }
  }
  int mid = binaryLength / 16;
  overlappedList = (char *)malloc(binaryLength / 8 * sizeof(char) + 1); // Allocate memory for the char list

  int j = 0;
  for (int i = 0; i < mid; i++)
  {
    overlappedList[j] = byteList[i];
    overlappedList[j+1] = byteList[(mid) + i];
    j += 2;
  }

  FILE *out = fopen("output.bin", "wb");
  if (out == NULL)
  {
    printf("Error opening file.\n");
    return 1;
  }

  fwrite(overlappedList, sizeof(unsigned char), binaryLength / 8, file);
  fclose(file);

  // Free dynamically allocated memory
  free(binaryData);
  free(shuffledbinary);
  free(shuffledList);
  free(byteList);

  return 0;
}
