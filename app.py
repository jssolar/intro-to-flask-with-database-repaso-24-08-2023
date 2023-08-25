import os # os es una libreria nativa de python, que permite detectar las configuraciones de acuerdo al sistema operativo que esté usando y lo ajusta al sistm oprtvo
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from models import db, Task


#----lo 1ro en ejecutar es load_dotenv(), porque
# necesito leer este archivo en cuanto cargue la applicacion -----#

load_dotenv()

app = Flask(__name__)
app.config['DEBUG']= True
app.config['ENV']= 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URL')


db.init_app(app)#---vinculacion de archivo models con mi aplicacion---#
Migrate(app, db)  #---comandos que permiten gestionar mi base de datos recive estas dos instancias {app, y db}---#
                    #---posee 3 comandos: flask db init; flask db migrate; flask deb upgrade---#
CORS(app) #--evita que en la aplicacion de front de error---#

#---configuracion ruta inicial---#

@app.route('/')
def main():
    return jsonify({"message": "mi 1ra app con flask y base de datos"})

@app.route('/todos', methods=['GET'])
def listar_todos():
    todos = Task.query.all() #SELECT *FROM todos; [<task1, Task2...taskn]
    todos = list(map(lambda task: task.serialize(), todos))#--por cada tarea que consiga en todos, va a llamar a la funcions serialize()
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def crear_task():
    body = request.get_json()
    
    task = Task()
#--si hay done en el body, aplica linea45, si no, sigue de largo--# 
    if 'done' in body:         
        task.label = body["label"]
    task.done = body["done"]

#--------guardando los datos--------------
    db.session.add(task)
    db.session.commit()
#--------respuesta al usuario--------------
    
    return jsonify(task.serialize()), 201 #--respuesta al usuario
























if __name__ == '__main__':
    app.run()
