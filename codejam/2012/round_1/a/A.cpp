#include<fstream>
#include<iostream>
#include<stdio.h>
#include<stdlib.h>

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
  void addToMap(char *input,char *output);
  void printCurrMap();
}obj;

void Googlerese::addToMap(char *input,char *output) {
  int i = 0;
  while(input[i]!='\0') {
    googMap[input[i]]=output[i];
    printf("\n#%c: %c",input[i],output[i]);
     i++;
  }
}

void Googlerese::printCurrMap() {
  ofstream goog_map("map.txt");
 
  for (int i = 'a'; i <= 'z'; ++i)    
    {
      
      printf("\n#%c: %c",i,googMap[i]);
      goog_map<<googMap[i];
      
    }
  goog_map.close();
}

int main(int argc, char *argv[]){
  int opt;
  char ginput[120],goutput[120];
  do {
    cout<<"Menu:\nsample ->1\nmap ->2\ninput -3\nexit ->0\n>>>";
    cin>>opt;
    switch (opt) {
    case 1: {
      cout<<"Input: ";
      cin.ignore();
      cin.getline (ginput,120);
      
      cout<<"Output: ";
      //cin.ignore();
      cin.getline (goutput,120);
      obj.addToMap(ginput,goutput);
      break;
    }
    case 2: {
      obj.printCurrMap();
      break;
    }
    case 3: {
      break;
    }
    case 0:
      exit(0);
    default: {
      cout<<"invalid option";
    }
    }
  } while (opt!=0);

  return 0;
}
