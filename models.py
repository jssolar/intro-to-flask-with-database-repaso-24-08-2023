from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()    # creacion de instancia

# para crear la base de datos, haré un nuevo model
class Task(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    label=db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean(), default=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done 
        }