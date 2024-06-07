run: 
	coverage run --data-file=./coverage/.coverage -m pytest ./testings/test_structural.py 
	coverage report --data-file=./coverage/.coverage -m