#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int isPrime(long n){
  int limit=0,i;
  limit=sqrt(n);
  if(n==0||n==1)
    return 0;
  for(i=2;i<=limit;i++){
    if(n%i==0)
      return 0;
  }
  return 1;
}

int main(int argc, char *argv[]){
  FILE *file = fopen( argv[1], "r" );
  long long sum=0;
  long num,i;
  char len[20];

  fgets(len,10,file );
  num=atoi(len);

  for(i=2;i<=num;i++){
    if(isPrime(i)){
      sum+=i;
    }
  }
  printf("%llu\n",sum);
  fclose( file );
  return 0;
}
