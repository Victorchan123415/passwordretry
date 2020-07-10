password = 'a123456'
versuch = 3
while True:
	enter_password = input('please enter your password: ')
	if password == enter_password:
		print('password correct, welcome!')
		break
	else:
		versuch = versuch - 1
		print('password incorrect, you have', versuch, 'more chance')
		if versuch == 0:
			print('your account is locked')
			break