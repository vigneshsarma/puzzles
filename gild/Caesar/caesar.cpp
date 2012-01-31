#include<stdio.h>
#include<stdlib.h>
int map[127];
int key;
char len[10];

void generateMap(int start,int stop){
  int i;

  for(i=start;i<=stop;i++){
    if((i-key)<start){
      map[i]=(stop+1-(start-(i-key)));
    } else{
      map[i]=(i-key);
    }
  }
}

void fromMap(int x) {
 
   if(map[x]!=0){
      printf("%c",map[x]);
    }else{
      printf("%c",x);
    }
}


int main(int argc, char *argv[]){
  FILE *file = fopen( argv[1], "r" );
  int x;
  int i;

  for(i=0;i<127;i++){
    map[i]=0;
  }

  fgets(len,10,file );
  key=atoi(len)%26+26;
  generateMap('a','z');
  generateMap('A','Z');

  //printf("%d",key);     
  while  ( ( x = fgetc( file ) ) != EOF ) {
    fromMap(x);
  }
  fclose( file );
  return 0;
}
