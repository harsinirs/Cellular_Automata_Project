import numpy as np
matrix1=np.array([[1,2,1,2,2,1],[1,1,2,0,2,1],[2,1,0,1,1,0],[2,1,2,1,1,1],[0,1,2,1,1,0],[1,1,2,2,1,1]])
(r,c)=matrix1.shape
print(r,c)
print(matrix1)
print("Total population: ",r*c)
matrix2=np.array([[1,2,3,2,2,3],[3,3,2,0,2,1],[2,3,0,3,1,0],[2,3,2,3,1,3],[0,1,2,3,3,0],[3,1,2,2,1,3]])
(row, col)=matrix2.shape
print(row, col)
print(matrix2)
print("Total population: ",row*col)

#calculate the number of healthy, infected, and removed individuals in population in a given neighbourhood.
def popstats(m):
    NH=NR=NI=0
    (row, col)=m.shape
    for x in range(row):
        for y in range(col):
            if (m[x][y]==1):
                NH+=1
            elif(m[x][y]==3):
                NH+=1
            elif (m[x][y]==0):
                NR+=1
            elif (m[x][y]==2):
                NI+=1
    print("Healthy: ",NH,"\nInfected: ",NI,"\n Population removed: ",NR)

def rules1(m,a,b):
  n1=n2=n3=n0=p=q=0
  for i in range(2):
    for j in range(3):
      if (m[i][j]==0):
        n0+=1
      elif (m[i][j]==1):
        n1+=1
      elif (m[i][j]==2):
        n2+=1
      elif (m[i][j]==3):
        n3+=1


  if (a==0)and (b==1):
    p=a
    q=b
  else:
    p=a-1
    q=b

  if m[p][q]==0:
    n0-=1
  elif m[p][q]==1:
    n1-=1
  elif m[p][q]==2:
    n2-=1
  elif m[p][q]==3:
    n3-=1

  d=dict()
  d={'no.of 0':n0,'no.of 1':n1, 'no of 2':n2, 'no of 3':n3}  
  return d

def rules2(m,x,y):
  n1=n2=n0=n3=p=q=0
  for i in range(3):
      for j in range(2):
        if (m[i][j]==0):
          n0+=1
        elif (m[i][j]==1):
          n1+=1
        elif (m[i][j]==2):
          n2+=1
        elif (m[i][j]==3):
          n3+=1

  if (x==1)and (y==0):
    p=x
    q=y
  else:
    p=x
    q=y-1

  if m[p][q]==0:
    n0-=1
  elif m[p][q]==1:
    n1-=1
  elif m[p][q]==2:
    n2-=1
  elif m[p][q]==3:
    n3-=1

  d=dict()
  d={'no.of 0':n0,'no.of 1':n1, 'no of 2':n2, 'no of 3':n3}  
  return d

def rules3(mat):
  
  n1=n2=n3=n0=0

  for i in range(3):
    for j in range(3):
      if mat[i][j]==0:
        n0+=1
      elif mat[i][j]==1:
        n1+=1
      elif mat[i][j]==2:
        n2+=1
      elif mat[i][j]==3:
        n3+=1

  if mat[1][1]==0:
    n0-=1
  if mat[1][1]==1:
    n1-=1
  if mat[1][1]==2:
    n2-=1
  if mat[1][1]==3:
    n3-=1
  
  
  d=dict()
  d={'no.of 0':n0,'no.of 1':n1, 'no of 2':n2, 'no of 3':n3}  
  nmat=np.copy(mat)
  l5 =[]
  for key in d.keys():
    l5.append(d[key])
  if ((mat[1][1] == 1) and (l5[2]>=4)): nmat[1][1] = 2
  elif ((mat[1][1] == 0 or 2 or 3)): nmat[1][1] = mat[1][1]
  return (nmat[1][1])

def modrules(mat):
  new=np.copy(mat)
  for i in range(3):
    for j in range(3):
      if (((i,j)==(0,0)) or ((i,j)==(0,2)) or ((i,j)==(2,0)) or ((i,j)==(2,2))):
        new[i][j]= mat[i][j]
      elif (((i,j)==(0,1)) or ((i,j)==(2,1))):
        l1=l2=[]
        if (i,j)==(0,1):
          nm1= mat[0:2,0:3]
          s1= rules1(nm1,i,j)
          for key in s1.keys():
            l1.append(s1[key])
          if ((nm1[0][1] == 1) and (l1[2]>=1)): new[0][1] = 2
          elif ((nm1[0][1] == 0 or 2)): new[0][1] = nm1[0][1]
        elif (i,j)==(2,1):
          nm2= mat[1:3,0:3]
          s2=rules1(nm2,i,j)
          for key in s2.keys():
            l2.append(s2[key])
          if ((nm2[1][1] == 1) and (l2[2]>=1)): new[2][1] = 2
          elif ((nm2[1][1] == 0 or 2)): new[2][1] = nm2[1][1]
        
      elif (((i,j)==(1,0)) or ((i,j)==(1,2))):
        l3=l4=[]
        if (i,j)==(1,0):
          nm3= mat[0:3,0:2]
          s3= rules2(nm3,i,j)
          for key in s3.keys():
            l3.append(s3[key])
          if ((nm3[1][0] == 1) and (l3[2]>=1)): new[1][0] = 2
          elif ((nm3[1][0] == 0 or 2)): new[1][0] = nm3[1][0]
        elif (i,j)==(1,2):
          nm4=mat[0:3,1:3]
          s4= rules2(nm4,i,j)  
          for key in s4.keys():
            l4.append(s4[key]) 
          if ((nm4[1][1] == 1) and (l4[2]>=1)): new[1][2] = 2
          elif ((nm4[1][1] == 0 or 2)): new[1][2] = nm4[1][1]   
  new[1][1]=rules3(mat)
  return new

def rules(m):
  new=np.copy(m)
  
  for i in range(3):
    for j in range(3):
      if (((i,j)==(0,0)) or ((i,j)==(0,2)) or ((i,j)==(2,0)) or ((i,j)==(2,2))):
        new[i][j]= m[i][j]
      elif (((i,j)==(0,1)) or ((i,j)==(2,1))):
        l1=l2=[]
        if (i,j)==(0,1):
          nm1= m[0:2,0:3]
          s1= rules1(nm1,i,j)
          for key in s1.keys():
            l1.append(s1[key])
          if ((nm1[0][1] == 1) and (l1[2]>=4)): new[0][1] = 2
          elif ((nm1[0][1] == 0 or 2 or 3)): new[0][1] = nm1[0][1]
        elif (i,j)==(2,1):
          nm2= m[1:3,0:3]
          s2=rules1(nm2,i,j)
          for key in s2.keys():
            l2.append(s2[key])
          if ((nm2[1][1] == 1) and (l2[2]>=4)): new[2][1] = 2
          elif ((nm2[1][1] == 0 or 2 or 3)): new[2][1] = nm2[1][1]
        
      elif (((i,j)==(1,0)) or ((i,j)==(1,2))):
        l3=l4=[]
        if (i,j)==(1,0):
          nm3= m[0:3,0:2]
          s3= rules2(nm3,i,j)
          for key in s3.keys():
            l3.append(s3[key])
          if ((nm3[1][0] == 1) and (l3[2]>=4)): new[1][0] = 2
          elif ((nm3[1][0] == 0 or 2 or 3)): new[1][0] = nm3[1][0]
        elif (i,j)==(1,2):
          nm4=m[0:3,1:3]
          s4= rules2(nm4,i,j)  
          for key in s4.keys():
            l4.append(s4[key]) 
          if ((nm4[1][1] == 1) and (l4[2]>=4)): new[1][2] = 2
          elif ((nm4[1][1] == 0 or 2 or 3 or 4)): new[1][2] = nm4[1][1]   
  new[1][1]=rules3(m)
  return new

if ((r == c) and (r%2==0)):
  stepp1= int (r/2)
  stepp2=stepp1
else:
  stepp1= int ((r+1)/2)
  stepp2=int ((c+1)/2)
NH3=NR3=NI3=0
print("Model 1:\n")
for i in range(0,r,stepp1):
    for j in range(0,c,stepp2):
        nmat= matrix1[i:i+3,j:j+3]
    if (nmat.shape==(3,3)):
      print("extracted matrix:\n", nmat)
      newmat= modrules(nmat)
      for x in range(3):
        for y in range(3):
          if (newmat[x][y]==1):
            NH3+=1
          elif (newmat[x][y]==0):
            NR3+=1
          elif (newmat[x][y]==2):
            NI3+=1
      print("New Matrix\n", newmat)

if ((row == col) and (row%2==0)):
  step1= int (row/2)
  step2=step1
else:
  step1= int ((row+1)/2)
  step2=int ((col+1)/2)
NH4=NI4=NR4=0
print("Model 2:\n")
for i in range(0,row,step1):
  for j in range(0,col,step2):
    nmatrix= matrix2[i:i+3,j:j+3]
    if (nmatrix.shape==(3,3)):
      print("extracted matrix:\n", nmatrix)
      newnmat= rules(nmatrix)
      for x in range(3):
        for y in range(3):
          if (newnmat[x][y]==1):
            NH4+=1
          elif (newnmat[x][y]==3):
            NH4+=1
          elif (newnmat[x][y]==0):
            NR4+=1
          elif (newnmat[x][y]==2):
            NI4+=1
      print("New Matrix\n", newnmat)

print("In model 1,\n No of healthy indivuals: \n", NH3,"\n No of infected indivuals: \n", NI3)     
print("In model 2,\n No of healthy indivuals: \n", NH4, "\n No of infected indivuals: \n", NI4)
