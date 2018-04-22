import os,re,sys,cStringIO

f=open("log.txt","rb")
fm=cStringIO.StringIO()

for line in f:
	if line.strip() != '':
		out=line.replace(u'\u001a',' ')
		fm.write(out)
f.close() 
try:
	buffer=fm.getvalue()
except Exception:
	print(str(Exception))
	sys.exit(1)
buffer=re.sub(r'\n([^"])',r'\1',buffer).split("\n")
err=False
i=0
length=len(buffer)
while not err:
	if i<length:
		line=buffer[i]
		print("query su mem "+line)
		if "ERR" in line:
			with open("out.txt","r+") as o:
				for l in o.read().split("\n"):
					if l==line:
						break
					elif not l.strip() or l.strip() == str(""):
						o.seek(0,2)
						o.write(line+"\n")
		i+=1
	elif i==length:
		sys.exit(0)
