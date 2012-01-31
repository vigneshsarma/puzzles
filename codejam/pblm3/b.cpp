#include<fstream>
#include<iostream>


using namespace std;

int k,C,N,D;
char c[36][3],d[28][2],n[100];

char combine(char a) {
    char z=a;
    int i;
    for(i=0; i<C; i++) {
        if(c[i][1]==a) {
            if(c[i][0]==n[k-1])
                z=c[i][2];
        } else if(c[i][0]==a) {
            if(c[i][1]==n[k-1])
                z=c[i][2];
        }
    }
    return z;
}

int clear(char a) {
    int i,j;
    for(i=0; i<D&&k!=0; i++) {
        if(d[i][1]==a) {
            for(j=0; j<k; j++) {
                if(d[i][0]==n[j]) {
                    k=0;
                    break;
                }
            }

        }
        else if(d[i][0]==a) {
            for(j=0; j<k; j++) {
                if(d[i][1]==n[j]) {
                    k=0;
                    break;
                }
            }
        }
    }

    return k;
}

int main() {

    ifstream a("b.in");
    ofstream b("b.out");
    int T,i,j,w;
    char ni,nw;
    a>>T;
    for(i=0; i<T;) {

        a>>C;
        for(j=0; j<C; j++) {
            a>>c[j][0]>>c[j][1]>>c[j][2];
        }
        a>>D;
        for(j=0; j<D; j++) {
            a>>d[j][0]>>d[j][1];
        }
        a>>N;
        k=0;
        for(j=0; j<N; j++) {
            a>>ni;
            if(k!=0) {
                nw=combine(ni);
                if(nw==ni) {
                    w=clear(ni);
                    if(w!=0)
                        n[k++]=ni;

                } else {
                    n[k-1]=nw;
                }
            } else {
                n[k++]=ni;
            }
        }

        b<<"Case #"<<++i<<": "<<"[";
        for(j=0; j<k; j++) {
            b<<n[j];
            if(j!=k-1) {
                b<<", ";
            }
        }
        b<<"]"<<endl;
    }
}
