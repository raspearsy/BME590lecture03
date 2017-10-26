import pytest
def add(x,y):
	if((type(x) == int or type(x) == float) and (type(y) == int or type(y) == float)):
		if((x+y)>=0):
			return x+y
		else:
			return 0

def test_add():
	assert add(2,3) == 5
	assert add(-1,-3) == 0
	assert add(0,0) == 0
	assert add('2','2') == None
	assert add(2.5,5.5) == 8.0
	assert add(complex(1),complex(3)) == None