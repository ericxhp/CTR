import os
class TestCase_2(object):

	def show(self):
		print "This Test case 2"
		print "env list"
		env_dist = os.environ
		for key in env_dist:
			print key + ' : ' + env_dist[key]




if __name__ == '__main__':
	test = TestCase_2()
	test.show()
