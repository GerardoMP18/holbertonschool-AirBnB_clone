<p align="center">
  <a href="https://ibb.co/K5t3PpC"><img src="https://i.ibb.co/yNzb9cL/65f4a1dd9c51265f49d0.png" alt="65f4a1dd9c51265f49d0" border="0" height="60%" width="50%"></a>
</p>
<h1 align= "center">🔶 AirBnB clone 🔶</h1>

This is the first part of the AirBnB clone proyect!
That is to write a console that interpret the AirBnB objects.

## Command Interpreter

The console have many functions, that are:
- Create a new object
- Show an object
- Update an object's attributes
- destroy an object

# Installation
```
git clone git@github.com:GerardoMP18/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB_clone
```
How can we use the interpreter?
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) create
(hbnb) ** class name missing **
(hbnb) quit
$
```
## Using the create, show, update and destroy functions:
```
$ ./console.py
(hbnb)
(hbnb)
(hbnb) create
** class name missing **
(hbnb) create BaseModel
0aeb0145-807f-4b39-8111-c793d8af36d5
(hbnb) show dfdgdfg
** class doesn't exist **
(hbnb) show BaseModel 0aeb0145-807f-4b39-8111-c793d8af36d5
[BaseModel] (0aeb0145-807f-4b39-8111-c793d8af36d5) {'id': '0aeb0145-807f-4b39-8111-c793d8af36d5',
'created_at': datetime.datetime(2022, 7, 3, 0, 1, 12, 264613), 'updated_at': datetime.datetime(2022, 7, 3, 0, 1, 12, 264637)}
(hbnb) update BaseModel
** instance id missing **
(hbnb) update BaseModel 5b63ffeb-3630-42fe-bfc4-e446a36da937 AirIsfun "NoTooMuch"
hbnb) show BaseModel 0aeb0145-807f-4b39-8111-c793d8af36d5
[BaseModel] (0aeb0145-807f-4b39-8111-c793d8af36d5) {'id': '0aeb0145-807f-4b39-8111-c793d8af36d5', 
'created_at': datetime.datetime(2022, 7, 3, 0, 1, 12, 264613), 
'updated_at': datetime.datetime(2022, 7, 3, 0, 1, 12, 264637), 'AirIsfun': 'NoTooMuch'}
(hbnb) destroy BaseModel 0aeb0145-807f-4b39-8111-c793d8af36d5
(hbnb) show BaseModel 0aeb0145-807f-4b39-8111-c793d8af36d5
** no instance found **
(hbnb) quit
$
```
## Environment used
`Ubuntu 20.04 LTS using python3 (version 3.8.5)`
## Authors

- Gerardo Marin | [GitHub](https://github.com/GerardoMP18)  
- Dhanna Palomino | [GitHub](https://github.com/FoleKhali)
