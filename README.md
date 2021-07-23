## DOCKER
- docker-compose build
- docker-compose up -d
- docker-compose exec app python manage.py create_db
- docker-compose exec app python manage.py create_super_user

## USER

1. Create User **POST**

- http://localhost:5000/user/create/
- Permissions: HeadOfCompany, HeadOfOffice
- Example request:
```
{
	"email": "antonantonov@gmail.com",
	"password": "12345",
	"first_name_user": "Anton",
	"last_name_user": "Antonov",
	"salary_user": 1150,
	"department_id": 1,
	"role_id": 2
}
```

2. Read User **GET**
- Permissions: HeadOfCompany, HeadOfOffice
- http://localhost:5000/user/read/

3. Read one user by pk **GET**
- Permissions: HeadOfCompany, HeadOfOffice
- http://localhost:5000/user/read/<int:pk>/

4. Read yourself **GET**
- Permissions: jwt required
- http://localhost:5000/user/read/me/

5. Login user **GET**
- Permissions: no permissions
- http://localhost:5000/user/login/
- Example request:
```
{
	"email": "headofcompany@gmail.com",
	"password": "12345"
}
```

6. Update user by pk **PUT**
- Permissions: HeadOfCompany, HeadOfOffice
- http://localhost:5000/user/update/<int:pk>
- Example request:
```
{
	"first_name_user": "Ivan",
	"department_id": 2
}
```
- p.s. also can use method **GET** user by pk after/before update in this route
- http://127.0.0.1:5000/user/update/<int:pk>

7. Delete user by pk **DELETE**
- Permissions: HeadOfCompany, HeadOfOffice
- http://localhost:5000/user/delete/<int:pk>

## DEPARTMENT
- Permissions: HeadOfCompany, HeadOfOffice
- URLS:
- http://localhost:5000/department/create/
- http://localhost:5000/department/read/
- http://localhost:5000/department/read/<int:pk>
- http://localhost:5000/department/update/<int:pk>
- http://localhost:5000/department/delete/<int:pk>

## OFFICE
- Permissions: HeadOfCompany
- URLS:
- http://localhost:5000/office/create/
- http://localhost:5000/office/read/
- http://localhost:5000/office/read/<int:pk>
- http://localhost:5000/office/update/<int:pk>
- http://localhost:5000/office/delete/<int:pk>

## ROLE
- Permissions: HeadOfCompany
- URLS:
- http://localhost:5000/role/create/
- http://localhost:5000/role/read/
- http://localhost:5000/role/read/<int:pk>
- http://localhost:5000/role/update/<int:pk>
- http://localhost:5000/role/delete/<int:pk>

## FILTERS
1. Filter by salary office **GET**
- Permissions: HeadOfCompany
- http://localhost:5000/filter/salary/office/<int:pk>/

2. Filter by params [office_id, department_id, salary_user, role_id] **GET**
- Permissions: HeadOfCompany
- http://localhost:5000/filter/
- Example_request:
```
{
	"office_id": 1,
	"salary": 2000
}
```