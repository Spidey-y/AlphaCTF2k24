#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h> 
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>

#define PORT 1337
#define LISTENQ 20
#define ADMIN_USERNAME "7jGkL2sPqA"
#define ADMIN_PASSWORD "xY9bN4rH3F"

int list_s;

typedef struct {
	int returncode;
	char *filename;
} httpRequest;

typedef struct {
	pthread_mutex_t mutexlock;
	int totalbytes;
} sharedVariables;

char *header200 = "HTTP/1.0 200 OK\nServer: Crver\nContent-Type: text/html\n\n";
char *header400 = "HTTP/1.0 400 Bad Request\nServer: Crver\nContent-Type: text/html\n\n";
char *header401 = "HTTP/1.0 401 Unauthorized\nServer: Crver\nContent-Type: text/html\n\n";
char *header404 = "HTTP/1.0 404 Not Found\nServer: Crver\nContent-Type: text/html\n\n";

// get a message from the socket until a blank line is recieved
char *getMessage(int fd) {
  
    FILE *sstream;
    
    if( (sstream = fdopen(fd, "r")) == NULL)
    {
        fprintf(stderr, "Error opening file descriptor in getMessage()\n");
        exit(EXIT_FAILURE);
    }
    
    size_t size = 1;
    
    char *block;
    
    if( (block = malloc(sizeof(char) * size)) == NULL )
    {
        fprintf(stderr, "Error allocating memory to block in getMessage\n");
        exit(EXIT_FAILURE);
    }
  
    *block = '\0';
    
    char *tmp;
    if( (tmp = malloc(sizeof(char) * size)) == NULL )
    {
        fprintf(stderr, "Error allocating memory to tmp in getMessage\n");
        exit(EXIT_FAILURE);
    }

    *tmp = '\0';
    
    int end;
    int oldsize = 1;
    
    while( (end = getline( &tmp, &size, sstream)) > 0)
    {
        if( strcmp(tmp, "\r\n") == 0)
        {
            break;
        }
        
        // Resize block
        block = realloc(block, size+oldsize);
        oldsize += size;
        strcat(block, tmp);
    }
    
    free(tmp);
    
    return block;

}

int sendMessage(int fd, char *msg) {
    return write(fd, msg, strlen(msg));
}

char * getFileName(char* msg)
{
    char * file;
    if( (file = malloc(sizeof(char) * strlen(msg))) == NULL)
    {
        fprintf(stderr, "Error allocating memory to file in getFileName()\n");
        exit(EXIT_FAILURE);
    }
    
    sscanf(msg, "GET %s HTTP/1.1", file);
    
    char *base;
    if( (base = malloc(sizeof(char) * (strlen(file) + 18))) == NULL)
    {
        fprintf(stderr, "Error allocating memory to base in getFileName()\n");
        exit(EXIT_FAILURE);
    }
    
    char* ph = "public";
    
    strcpy(base, ph);
    
    strcat(base, file);
    
    free(file);
    
    return base;
}


int isValidCredentials(char *username, char *password) {
    int correct_username = 1;
    for (int i = 0; username[i] != '\0' && ADMIN_USERNAME[i] != '\0'; i++) {
        correct_username = correct_username & ((username[i] ^ ADMIN_USERNAME[i]) == 0);
    }

    int correct_pass = 1;
    for (int i = 0; password[i] != '\0' && ADMIN_PASSWORD[i] != '\0'; i++) {
        correct_pass = correct_pass & ((password[i] ^ ADMIN_PASSWORD[i]) == 0);
    }

    correct_pass = correct_pass & (strlen(username) == strlen(ADMIN_USERNAME));
    correct_pass = correct_pass & (strlen(password) == strlen(ADMIN_PASSWORD));

    return (correct_username && correct_pass);
}

httpRequest parseRequest(char *msg){
    httpRequest ret;
       
    char* filename;
    if( (filename = malloc(sizeof(char) * strlen(msg))) == NULL)
    {
        fprintf(stderr, "Error allocating memory to filename in parseRequest()\n");
        exit(EXIT_FAILURE);
    }
    filename = getFileName(msg);
    
    char *badstring = "..";
    char *test = strstr(filename, badstring);
    
    // if they asked for / and give them index.html
    int test2 = strcmp(filename, "public/");


    FILE *exists = fopen(filename, "r" );
    
    if( test != NULL )
    {
        // Return a 400 header and 400.html
        ret.returncode = 400;
        ret.filename = "400.html";
    }


    
    else if(test2 == 0)
    {
        ret.returncode = 200;
        ret.filename = "public/index.html";
    }
    
    // If they asked for a specific page and it exists because we opened it sucessfully return it 
    else if( exists != NULL )
    {
        
        ret.returncode = 200;
        ret.filename = filename;
        fclose(exists);
    }
    
    else
    {
        ret.returncode = 404;
        ret.filename = "404.html";
    }



    int isAdminRequest = (strcmp(filename, "public/admin.html") == 0);

    char *authHeader = strstr(msg, "Authorization: ");
    
    if (authHeader != NULL && isAdminRequest) {
        char *credentials = authHeader + strlen("Authorization: ");

        char *username = NULL;
        char *password = NULL;

        // Allocate memory for username and password
        if (sscanf(credentials, "%ms %ms", &username, &password) != 2) {
            // Handle error or reject the input

            // Free dynamically allocated memory
            free(username);
            free(password);

            ret.returncode = 400; // Bad Request
            ret.filename = "400.html";
             return ret;
         }

        // Check if the credentials are valid
        if (!isValidCredentials(username, password)) {
            // Return a 401 Unauthorized response

            // Free dynamically allocated memory
            free(username);
            free(password);

            ret.returncode = 401;
            ret.filename = "401.html";
            return ret;
        }

        // Free dynamically allocated memory after use
        free(username);
        free(password);
    } else if (isAdminRequest) {
        // If no Authorization header found for admin request, return 401
        ret.returncode = 401;
        ret.filename = "401.html";
        return ret;
    }
    
    // Return the structure containing the details
    return ret;
}

// print a file out to a socket file descriptor
int printFile(int fd, char *filename) {
  
    
    FILE *read;
    if( (read = fopen(filename, "r")) == NULL)
    {
        fprintf(stderr, "Error opening file in printFile()\n");
        exit(EXIT_FAILURE);
    }
    
    int totalsize;
    struct stat st;
    stat(filename, &st);
    totalsize = st.st_size;
    
    size_t size = 1;
    
    char *temp;
    if(  (temp = malloc(sizeof(char) * size)) == NULL )
    {
        fprintf(stderr, "Error allocating memory to temp in printFile()\n");
        exit(EXIT_FAILURE);
    }
    
    
    int end;
    
    while( (end = getline( &temp, &size, read)) > 0)
    {
        sendMessage(fd, temp);
    }
    
    sendMessage(fd, "\n");
    
    free(temp);
    
    return totalsize;
  
}

// clean up listening socket on ctrl-c
void cleanup(int sig) {
    
    printf("Cleaning up connections and exiting.\n");
    
    if (close(list_s) < 0) {
        fprintf(stderr, "Error calling close()\n");
        exit(EXIT_FAILURE);
    }
    
    shm_unlink("/sharedmem");
    
    // exit with success
    exit(EXIT_SUCCESS);
}

int printHeader(int fd, int returncode)
{
    switch (returncode)
    {
        case 200:
        sendMessage(fd, header200);
        return strlen(header200);
        break;
        
        case 400:
        sendMessage(fd, header400);
        return strlen(header400);
        break;

        case 401:
        sendMessage(fd, header401);
        return strlen(header401);
        break;
        
        case 404:
        sendMessage(fd, header404);
        return strlen(header404);
        break;

    }
}


// Increment the global count of data sent out 
int recordTotalBytes(int bytes_sent, sharedVariables *mempointer)
{
    pthread_mutex_lock(&(*mempointer).mutexlock);
    (*mempointer).totalbytes += bytes_sent;
    pthread_mutex_unlock(&(*mempointer).mutexlock);
    return (*mempointer).totalbytes;
}


int main(int argc, char *argv[]) {
    int conn_s;                  //  connection socket
    short int port = PORT;       //  port number
    struct sockaddr_in servaddr; //  socket address structure
    
    // set up signal handler for ctrl-c
    (void) signal(SIGINT, cleanup);
    
    // create the listening socket
    if ((list_s = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) {
        fprintf(stderr, "Error creating listening socket.\n");
        exit(EXIT_FAILURE);
    }
    
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family      = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port        = htons(port);
    
    if (bind(list_s, (struct sockaddr *) &servaddr, sizeof(servaddr)) < 0 ) {
        fprintf(stderr, "Error calling bind()\n");
        exit(EXIT_FAILURE);
    }
    
    
    // Listen on socket list_s
    if( (listen(list_s, 20)) == -1)
    {
        fprintf(stderr, "Error Listening\n");
        exit(EXIT_FAILURE);
    } 
    
    
    shm_unlink("/sharedmem");
    
    int sharedmem;
    
    // Open the memory
    if( (sharedmem = shm_open("/sharedmem", O_RDWR | O_CREAT | O_EXCL, S_IRUSR | S_IWUSR)) == -1)
    {
        fprintf(stderr, "Error opening sharedmem in main() errno is: %s ", strerror(errno));
        exit(EXIT_FAILURE);
    }
    
    // Set the size of the shared memory to the size of my structure
    ftruncate(sharedmem, sizeof(sharedVariables) );
    
    // Map the shared memory into our address space
    sharedVariables *mempointer;
    
    // Set mempointer to point at the shared memory
    mempointer = mmap(NULL, sizeof(sharedVariables), PROT_READ | PROT_WRITE, MAP_SHARED, sharedmem, 0); 
    
    // Check the memory allocation went OK
    if( mempointer == MAP_FAILED )
    {
        fprintf(stderr, "Error setting shared memory for sharedVariables in recordTotalBytes() error is %d \n ", errno);
        exit(EXIT_FAILURE);
    }
    pthread_mutex_init(&(*mempointer).mutexlock, NULL);
    (*mempointer).totalbytes = 0;

    int addr_size = sizeof(servaddr);
    
    int headersize;
    int pagesize;
    int totaldata;
    // Number of child processes we have spawned
    int children = 0;
    // pid of the process we get when we spawn
    pid_t pid;
    
    // Loop infinitly serving requests
    while(1)
    {
    
        // spawn 20 children
        if( children <= 20)
        {
            pid = fork();
            children++;
        }
        
        if( pid == -1)
        {
            fprintf(stderr,"can't fork, error %d\n" , errno);
            exit (1);
        }
        
        // Have the child process deal with the connection
        if ( pid == 0)
        {	
            // Have the child loop infinetly dealing with a connection then getting the next one in the queue
            while (1) {
                // Accept a connection
                conn_s = accept(list_s, (struct sockaddr *)&servaddr, &addr_size);

                if (conn_s == -1) {
                    fprintf(stderr, "Error accepting connection \n");
                    exit(1);
                }

                char *header = getMessage(conn_s);

                printf("Received Request:\n%s\n", header);

                httpRequest details = parseRequest(header);

                free(header);

                headersize = printHeader(conn_s, details.returncode);

                pagesize = printFile(conn_s, details.filename);

                totaldata = recordTotalBytes(headersize + pagesize, mempointer);

                printf("Process %d served a request of %d bytes. Total bytes sent %d  \n", getpid(), headersize + pagesize, totaldata);

                close(conn_s);
            }
        }
    }
    
    return EXIT_SUCCESS;
}
