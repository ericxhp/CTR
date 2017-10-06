
import os

def GetTestLst():
	print "Get test case list"
	test_lst=[]
	f=open("TEST_CASE_SET.ini")
	lines=f.readlines()
	for line in lines:
		line=line.strip('\n')
		test_lst.append(line)

	return test_lst

def show():
	print "This Test case 1"
	print "env list"
	env_dist = os.environ
	for key in env_dist:
		print key + ' : ' + env_dist[key]
	return env_dist


def SetEnv(CaseLst):

	print CaseLst
	env_dist=show()
	env_dist["TEST_LIST"]=' '.join(CaseLst)
	print env_dist["TEST_LIST"]

	return 0

def main():
	test_lst=GetTestLst()
	SetEnv(test_lst)


main()