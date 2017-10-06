import os

class TestCase_1(object):

	def show(self):
		print "This Test case 1"
		print "env list"
		env_dist = os.environ
		for key in env_dist:
			print key + ' : ' + env_dist[key]
		




if __name__ == '__main__':
	test = TestCase_1()
	test.show()
