from models import *

for model in [User]:
	model.drop_table(fail_silently=True, cascade=True)
	model.create_table();