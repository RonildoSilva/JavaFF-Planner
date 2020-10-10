import os
import subprocess

rootdir = 'problems/rovers/'
domain = 'problems/rovers/domain.pddl/'

pfiles = list()

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if(not file.endswith('.pddl')):
			pfiles.append(os.path.join(subdir, file))
			#print(os.path.join(subdir, file))

pfiles.sort()

#p = subprocess.Popen('java -Xmx1024m -cp /usr/lib/jvm/java-8-openjdk-amd64/bin/java -Dfile.encoding=UTF-8 -classpath /home/ronildo/GitHubProjects/JavaFF/bin javaff.JavaFF problems/rovers/domain.pddl problems/rovers/pfile01', shell=True, stdout=subprocess.PIPE)

#algorithm = 'BreadthFirstSearch_'
#algorithm = 'BestFirstSearch_'
algorithm = 'EnforcedHillClimbingSearch_'


for param in pfiles:
	l = param.split('/')
	sufix = l[len(l)-1]
	if(not os.path.exists(algorithm+sufix+'.txt')):
		p = subprocess.Popen('java -Xmx1024m -cp /usr/lib/jvm/java-8-openjdk-amd64/bin/java -Dfile.encoding=UTF-8 -classpath /home/ronildo/GitHubProjects/JavaFF/bin javaff.JavaFF problems/rovers/domain.pddl '+param, shell=True, stdout=subprocess.PIPE, text=True)

		out, err = p.communicate()

		f = open(algorithm+sufix+'.txt', 'w')
		f.write(str(out))
		f.close()

#print(out)

