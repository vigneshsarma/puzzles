#include<fstream>
#include<iostream>


using namespace std;

int64_t N,j,m;

int64_t C[16],rm[2],rn[2];

int combine(int i) {
    int maxi=0;
    int l=i;


        if(l<N-1) {


            rm[0]+=C[l];
            rm[1]^=C[l];

            maxi=combine(l+1);
            m=(maxi>m)?maxi:m;
  //
            rm[0]-=C[l];
            rm[1]^=C[l];

            rn[0]+=C[l];
            rn[1]^=C[l];

            maxi=combine(l+1);
            m=(maxi>m)?maxi:m;

            rn[0]-=C[l];
            rn[1]^=C[l];
       //     cin>>j;
        }
         else if(l<N) {
            if(rn[0]==0) {
                rn[0]+=C[l];
                rn[1]^=C[l];
                maxi=combine(l+1);

                rn[0]-=C[l];
                rn[1]^=C[l];
            } else if(rm[0]==0) {
                rm[0]+=C[l];
                rm[1]^=C[l];
                m=combine(l+1);
                m=(maxi>m)?maxi:m;

                rm[0]-=C[l];
                rm[1]^=C[l];
            }else{
                 rm[0]+=C[l];
            rm[1]^=C[l];

            maxi=combine(l+1);
            m=(maxi>m)?maxi:m;
  //
            rm[0]-=C[l];
            rm[1]^=C[l];

            rn[0]+=C[l];
            rn[1]^=C[l];

            maxi=combine(l+1);
            m=(maxi>m)?maxi:m;

            rn[0]-=C[l];
            rn[1]^=C[l];
            }
        }
        else {
            if(rn[1]==rm[1]) {
                maxi=(rn[0]>rm[0])?rn[0]:rm[0];
                m=(maxi>m)?maxi:m;
                cout<<m;
             //   cout<<" "<<rm[0]<<" "<<rm[1]<<" "<<rn[0]<<" "<<rn[1]<<endl;
            } else
                m=(0>m)?0:m;

        }


    return m;
}

int main() {
    //char fna[20];

    ifstream a("C-large.in");
    ofstream b("c.out");

    int64_t maxi,T,i,k;

    a>>T;
    for(i=0; i<T;) {
        m=0;
        a>>N;
        for(j=0; j<N; j++) {
            a>>C[j];
            k^=C[j];
        }
        maxi=combine(0);
        m=(maxi>m)?maxi:m;
        //cout<<m;


        b<<"Case #"<<++i<<": ";
        if(m!=0)b<<m;
        else b<<"NO";
        b<<endl;
    }
}
