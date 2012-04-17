if __name__ == '__main__':
    fin = open("D.in","r")
    N = int(fin.readline())
    print N
    for i in range(0,N):
        h, w, d = fin.readline().split()
        h,w,d = int(h),int(w),int(d)
        map_mirr = []
        for j in range(0,h):
            map_mirr.append(fin.readline()[:-1])
            if 'X' in map_mirr[-1]:
                loc = (j,map_mirr[-1].index('X'))
        print map_mirr,loc
