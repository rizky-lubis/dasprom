# Measure some strings:
words = ['cat', 'window', 'defenestrate','gajah mada']
for w in words:
	print (w, len(w))
print("======================================")
# Crate a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy: iterate over a copy
for user, status in users.copy().items():	
	if status == 'inactive':
		del users [user]
# Startegy: crate a new collectionp
active_users = {}
for user, status in users.items():
	if status == 'active':
		active_users [user] = status
print(active_users)

