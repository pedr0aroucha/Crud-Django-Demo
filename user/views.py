from django.shortcuts import render
from .models import User

# Landing Page
def index(req):
	return render(req, 'index.html')

def create(req):
	message = False
	if req.POST:
		full_name = req.POST.get('full_name')
		age = req.POST.get('age')
		print(age, full_name)
		if User.objects.filter(full_name=full_name).first():
				message = 'user already exists'
		elif age and full_name:
			message = 'created'
			User.objects.create(age=age, full_name=full_name)
		else:
			message = 'it was bad'

	return render(req, '01_create.html', {'message':message})

def read(req):
	users = User.objects.all();
	return render(req, '02_read.html', {'users': users})

def update(req):
	user_update = ''
	message = False
	if req.POST: #search and edit
		full_name = req.POST.get('full_name')
		new_full_name = req.POST.get('new_full_name')
		age = req.POST.get('age')
		update = req.POST.get('update')
		user_update = User.objects.filter(full_name=full_name).first()
		if user_update and update: #update
			message = 'updated'
			user_update.age = age
			user_update.full_name = new_full_name
			user_update.save()
		elif user_update == None:
			message = 'not found'
	return render(req, '03_update.html', {'user':user_update, 'message':message})

def delete(req):
	user_delete = ''
	message = False
	if req.POST: #search
		full_name = req.POST.get('full_name')
		delete = req.POST.get('delete')
		user_delete = User.objects.filter(full_name=full_name).first()
		print(full_name, delete)
		if user_delete and delete: #delete
			message = 'deleted'
			user_delete.delete()
		elif user_delete == None:
			message = 'not found'
	return render(req, '04_delete.html', {'user':user_delete, 'message': message})

# Notas:

# Aparentemente o Django PURO não reconhece outros métodos HTTP Além do GET e POST.

# Criar um CRUD com Django é bem mais rápido que com NodeJS pois ele me dá várias ferramentas para isso, mas...
#...ao mesmo tempo que ele me dá um monte de ferramentas...
#...ele também me obriga a usar elas, então se eu não quiser usar um ORM por exemplo, vou ter um trabalho muito grande.