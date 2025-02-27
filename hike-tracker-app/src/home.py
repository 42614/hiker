from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from hike_details import hike_details_bp
from equipment_list import equipment_list_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hikes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(hike_details_bp)
app.register_blueprint(equipment_list_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)