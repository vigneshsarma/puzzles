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
  void addToMap();
  void printCurrMap();
}obj;

void Googlerese::addToMap() {
  ifstream goog_map("map.txt");
 
  for (int i = 'a'; i <= 'z'; ++i)    
    {        
      goog_map>>googMap[i];
      printf("\n#%c: %c",i,googMap[i]);      
    }
  googMap[' ']=' ';
  goog_map.close();
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

  do {
    cout<<"Menu:\nsample ->1\ninput -3\nexit ->0\n>>>";
    cin>>opt;
    switch (opt) {
    case 1: {
      obj.addToMap();
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
