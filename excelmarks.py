#python module to open an excel file and calculating the average of the marks scored in six subjects
x=input('enter the name of the file along with extension: ')
f=open(x,'r')
text=f.read()
l=text.rstrip()
k=l.split(',')
n=len(k)
i=1
m=(int(k[1])+int(k[2])+int(k[3])+int(k[4])+int(k[5])+int(k[6]))/6
d=str(m)
f.close()
f=open(x,'w')
l=l.replace('0',d)
f.write(l)
f.close()