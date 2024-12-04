from app import create_app
import os

app = create_app()
###

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER', 'user')}:{os.getenv('POSTGRES_PASSWORD', 'password')}@db:5432/{os.getenv('POSTGRES_DB', 'flaskdb')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
