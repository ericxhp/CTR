


def GetTestLst():
	print "Get test case list"
	test_lst=[]
	f=open("TEST_CASE_SET.ini")
	lines=f.readlines()
	for line in lines:
		line=line.strip('\n')
		test_lst.append(line)

	return test_lst


def SetEnv(CaseLst):

	print CaseLst

	return 0

def main():
	test_lst=GetTestLst()
	SetEnv(test_lst)


main()