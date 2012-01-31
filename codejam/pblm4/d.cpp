#include<fstream>
#include<iostream>


using namespace std;

int T,N,n[10],hold[10],free[10],hl,fl;
double p;

double findProb(int l) {
    double pi;
    if(l<N) {
        hold[hl++]=n[l];
        pi=findProb(l+1);
        p=(pi<p)?pi:p;
        hl--;
        hold[fl]=n[l];
        pi=findProb(l+1);
        p=(pi<p)?pi:p;
        fl--;
    } else {
        pi=prob(hold);

        }
}

int main() {

    ifstream a("d.in");
    ofstream b("d.out");
    int i,j;
//double p;
    a >>T;
    for(i=0; i<T; i++) {
        a>>N;
        for(j=0; j<N; j++) {
            a>>n[j];
        }
        p=findProb(0);
    }

    b<<"Case #"<<++i<<": "<<p<<endl;

}
