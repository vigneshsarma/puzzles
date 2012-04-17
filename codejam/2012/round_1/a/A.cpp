#include<fstream>
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

class Googlerese
{
  char googMap[150];
public:
  Googlerese(){
    for (int i = 'a'; i <= 'z'; ++i)    
    {
      googMap[i]=0;      
    }
  }
  void addToMap();
  void mapAndPrint(char fileName[20]);
}obj;

void Googlerese::addToMap() {
  char goog_map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q','\0'};

  cout << goog_map<<endl;
  printf("%d",' ');
  for (int i = 'a', j = 0; i <= 'z'; i++,j++)    
    {        
      googMap[i]=goog_map[j];
      printf("#%c: %c\n",i,googMap[i]);      
    }
  cout<<"sfd";
  googMap[32]=32;
}

void Googlerese::mapAndPrint(char fileName[20]) {
  char inpFile[20],outFile[20],tmp[120];
  char goog_map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q','\0'};
  int i=0,N,j;
  cout<<"tata ";
  strcpy(inpFile,fileName);
  strcat(inpFile,".in");
  strcpy(outFile,fileName);
  strcat(outFile,".out");
  ifstream fin(inpFile);
  ofstream fout(outFile);

  fin>>N;
  fin.ignore();
  while(i<N) {
    i++;j=0;
    fout<<"Case #"<<i<<": ";
    
    fin.getline(tmp,120);
    do
      {
	if(tmp[j] == ' '){
	  fout<< ' ';
	}else{
	  fout<<goog_map[tmp[j]-'a'];
	  cout<<goog_map[tmp[j]-'a'];
	}
	j++;
      } while (tmp[j]!='\0');
    fout<<endl;
  }
  fin.close();
  fout.close();
}

int main(int argc, char *argv[]){
  int opt;
  //obj.addToMap();
  obj.mapAndPrint(argv[1]);

  return 0;
}
