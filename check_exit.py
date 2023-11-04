# Code to check if the user wants to quit or continue.

User_Said = input('Please type p or q.')
while User_Said != 'q':
	if User_Said == 'p':
		print('Hello')
		User_Said = input('Please type p or q.')
	else:
		User_Said = input('Please type p or q.')
else:
	print('Done')
