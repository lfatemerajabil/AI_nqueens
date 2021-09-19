import numpy as np

import random
import time
import matplotlib.pyplot as pl
n = 8
initial = []
for i in range(n):
    r = random.randint(1,n)
    initial.append(r)

def action(state , n):
    S = []
    act = []
    for i in range(n):
        for j in range(1,n+1):
            if(state[i] != j):
                s = np.array(state)
                s[i] = j
                act.append(s)
    for a in act:
        h = 0
        for i in range(n):
            for j in range(i+1 , n):
                if(a[i] == a[j]):
                    h += 1
                if(abs(a[i]-a[j]) == j-i):
                    h += 1
        S.append((a , h))
    return S

def nqueen_randomly(state , n):
    time1 = time.perf_counter()
    h = 0
    for i in range(n):
        for j in range(i+1 , n):
            if(state[i] == state[j]):
                h += 1
            if(abs(state[i]-state[j]) == j-i):
                h += 1
    s = np.array(state)
    while(True):
        x = s
        '''
        nx = ny = n
        exp = []
        for i in range(n):
            ex = []
            xx = s[i]
            for j in range(1 , n+1):
                if(j == xx):
                    ex.append('*')
                else:
                    ex.append('')
            exp.append(ex)
        expand = np.array(exp)
        pl.figure()
        tb = pl.table(cellText=expand, loc=(0,0), cellLoc='center')
        tc = tb.properties()['child_artists']
        for cell in tc:
            cell.set_height(1/ny)
            cell.set_width(1/nx)
        ax = pl.gca()
        ax.set_xticks([])
        ax.set_yticks([])
        pl.show()
        time.sleep(1)
        '''
        Action = action(s.tolist() , n)
        for act in Action:
            if(act[1] < h):
                h = act[1]
                s = act[0]
        if(x.tolist() == s.tolist() and h == 0):
            break
        if(x.tolist() == s.tolist() and h!= 0):
            r = random.randint(0 , n*(n-1)-1)
            s = Action[r][0]
            continue
        if(x.tolist() != s.tolist()):
            continue
    time2 = time.perf_counter()
    print("time for solving w.r.t randomly:",(time2-time1))
    return s

def nqueen_stochastic(state , n):
    time1 = time.perf_counter()
    h = 0
    for i in range(n):
        for j in range(i+1 , n):
            if(state[i] == state[j]):
                h += 1
            if(abs(state[i]-state[j]) == j-i):
                h += 1
    s = np.array(state)
    while(True):
        x = s
        '''
        nx = ny = n
        exp = []
        for i in range(n):
            ex = []
            xx = s[i]
            for j in range(1 , n+1):
                if(j == xx):
                    ex.append('*')
                else:
                    ex.append('')
            exp.append(ex)
        expand = np.array(exp)
        pl.figure()
        tb = pl.table(cellText=expand, loc=(0,0), cellLoc='center')
        tc = tb.properties()['child_artists']
        for cell in tc:
            cell.set_height(1/ny)
            cell.set_width(1/nx)
        ax = pl.gca()
        ax.set_xticks([])
        ax.set_yticks([])
        pl.show()
        time.sleep(1)
        '''
        Action = action(s.tolist() , n)
        for act in Action:
            if(act[1] < h):
                h = act[1]
                s = act[0]
        if(x.tolist() == s.tolist() and h == 0):
            break
        if(x.tolist() == s.tolist() and h!= 0):
            R = sorted(Action , key=lambda tup :tup[1])
            H = R[0][1]
            c = 0
            for r in R:
                if(r[1] == H):
                    c += 1
            r = random.randint(0 , c-1)
            s = R[r][0]
            continue
        if(x.tolist() != s.tolist()):
            continue
    time2 = time.perf_counter()
    print("time for solving w.r.t stochastic:",(time2-time1))
    return s

def nqueen_sideway(state , n):
    time1 = time.perf_counter()
    h = 0
    for i in range(n):
        for j in range(i+1 , n):
            if(state[i] == state[j]):
                h += 1
            if(abs(state[i]-state[j]) == j-i):
                h += 1
    s = np.array(state)
    X = []
    while(True):
        x = s
        
        nx = ny = n
        exp = []
        for i in range(n):
            ex = []
            xx = s[i]
            for j in range(1, n+1):
                if(j == xx):
                    ex.append('*')
                else:
                    ex.append('')
            exp.append(ex)
        expand = np.array(exp)
        pl.figure()
        tb = pl.table(cellText=expand, loc=(0,0), cellLoc='center')
        tc = tb.properties()['child_artists']
        for cell in tc:
            cell.set_height(1/ny)
            cell.set_width(1/nx)
        ax = pl.gca()
        ax.set_xticks([])
        ax.set_yticks([])
        pl.show()
        time.sleep(1)
        
        Action = action(s.tolist() , n)
        for act in Action:
            if((act[1] < h)and(act[0].tolist() not in X)):
                h = act[1]
                s = act[0]
        if(x.tolist() == s.tolist() and h == 0):
            break
        if(x.tolist() == s.tolist() and h!= 0):
            X.append(x.tolist())
            R = sorted(Action , key=lambda tup :tup[1])
            H = R[0][1]
            c = 0
            for r in R:
                if(r[1] == H):
                    c += 1
            r = random.randint(0 , c-1)
            s = R[r][0].copy()
            continue
        if(x.tolist() != s.tolist()):
            continue
    time2 = time.perf_counter()
    print("time for solving w.r.t sideway:",(time2-time1))    
    return s

def nqueen_random_restart(state , n):
    h = 0
    for i in range(n):
        for j in range(i+1 , n):
            if(state[i] == state[j]):
                h += 1
            if(abs(state[i]-state[j]) == j-i):
                h += 1
    s = (np.array(state) , h)
    while(True):
        x = s
        '''
        nx = ny = n
        exp = []
        for i in range(n):
            ex = []
            xx = s[0][i]
            for j in range(1 , n+1):
                if(j == xx):
                    ex.append('*')
                else:
                    ex.append('')
            exp.append(ex)
        expand = np.array(exp)
        pl.figure()
        tb = pl.table(cellText=expand, loc=(0,0), cellLoc='center')
        tc = tb.properties()['child_artists']
        for cell in tc:
            cell.set_height(1/ny)
            cell.set_width(1/nx)
        ax = pl.gca()
        ax.set_xticks([])
        ax.set_yticks([])
        pl.show()
        time.sleep(1)
        '''
        Action = action(s[0].tolist() , n)
        for act in Action:
            if(act[1] < h):
                h = act[1]
                s = act
        if(x[0].tolist() == s[0].tolist()):
            break
        if(x[0].tolist() != s[0].tolist()):
            continue 
    return s

time1 = time.perf_counter()
s = nqueen_random_restart(initial , n)
while(s[1] != 0):
    current = []
    for i in range(n):
        r = random.randint(1,n)
        current.append(r)
    s = nqueen_random_restart(current , n)
    continue
time2 = time.perf_counter()
print("time for solving w.r.t random_restart:",(time2-time1))
print(s[0])
print(nqueen_stochastic(initial , n))
print(nqueen_sideway(initial , n))
print(nqueen_randomly(initial , n))