if __name__ == "__main__":
    fin = open("B-large-0.in",'r')
    N = fin.readline()
    fout = open("B.out","w")
    N=int(N[:-1])
    print N
    for i in range(0,N):
        words = fin.readline().split()
        T,S,p,result = int(words[0]),int(words[1]),int(words[2]),0
        #print T,S,p
        for each in words[3:]:
            test = int(each)
            #print test,
            avg = test/3
            mod = test%3
            if avg>=p:
                result +=1
            elif mod == 0 and avg:
                if avg+1>=p and S:
                    result +=1
                    S-=1
            elif mod == 1:
                if avg+1>=p:
                    result +=1
            elif mod == 2:
                if avg+1>=p:
                    result +=1
                elif avg+2>=p and S:
                    result +=1
                    S-=1
        fout.write("Case #"+str(i+1)+": "+str(result)+"\n")
            
