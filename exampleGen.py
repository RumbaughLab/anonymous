import os
import names


path = r'C:\Users\Windows\Desktop\test'

for i in range(5):
	randName = names.get_first_name() + '_' + names.get_last_name()
	for j in ['avi','txt','h5']:
		randNew = randName+'.'+j
		print(randNew)

		if j == 'avi':
			with open(path+os.sep+randNew, 'w') as fp:
			    pass

		for k in range(3):
			os.makedirs(path+os.sep+'childDir'+str(k), exist_ok=True)
			with open(path+os.sep+'childDir'+str(k)+os.sep+randNew, 'w') as fp:
			    pass