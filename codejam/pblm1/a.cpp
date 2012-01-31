#include<fstream>
#include<iostream>

#define mod(x)(x<0)?(-1*x):x

using namespace std;

class Robo {
public:
    int loc;
    int time;
    char name;
    Robo(char n){
    name=n;
    loc=1;
    }
    int moveTo(int P);
    void copyTo(Robo *g){
        g->loc=loc;
        g->name=name;
        g->time=time;
    }
    void copyTo(int loc,int time,char name){
        this->loc=loc;
        this->name=name;
        this->time=time;
    }
} O('O'),B('B'),Pre('G');

int Robo::moveTo(int P) {
    int t;
    t=P-loc;
    t=(t<0)?(-t):t;
    t++;
    cout<<t<<Pre.time<<endl;
    loc=P;
    if(Pre.name!=name) {
        t=t-Pre.time;
        if(t<1)t=1;
        time=t;
    } else {
        time+=t;
    }
    cout<< t<<endl;
    copyTo(&Pre);
    return t;
}

int main() {
    char fna[20];
    cin>>fna;
    ifstream a("A-small-attempt0.in");
    ofstream b("a.out");
    int i,j,N,P,T,tot=0,k;
    char R;
    a>>T;
    cout<<T<<endl;

    for(i=0; i<T;) {
        tot=0;
        a>>N;
        cout<<endl<<N;

        for(j=0; j<N; j++) {
            a>>R>>P;
            cout<<R<<P<<tot;
            if(R=='O') {
                tot+=O.moveTo(P);
            } else {
                tot+=B.moveTo(P);
            }
            //cin>>k;
        }
        if(i==43)
            cin>>k;

        b<<"Case #"<<++i<<": "<<tot<<endl;
        O.copyTo(1,0,'O');
        B.copyTo(1,0,'B');
        Pre.copyTo(1,0,'G');
    }
}
