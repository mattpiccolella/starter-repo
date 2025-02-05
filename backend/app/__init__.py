from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {'error': 'Not Found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'error': 'Internal Server Error'}, 500
    
    # CLI commands
    @app.cli.command("init-db")
    def init_db():
        """Initialize the database."""
        db.create_all()
        print('Database initialized!')

    @app.cli.command("seed-db")
    def seed_db():
        """Seed the database with sample data."""
        from .models import User, Post, Category
        
        # Check if the database is empty
        if db.session.query(User).count() > 0 or db.session.query(Post).count() > 0 or db.session.query(Category).count() > 0:
            print('Database already contains data. Seeding aborted.')
            return
        
        # Create sample users
        users = [
            User(username='john_doe', email='john@example.com', password_hash='dummy_hash1'),
            User(username='jane_smith', email='jane@example.com', password_hash='dummy_hash2'),
            User(username='bob_wilson', email='bob@example.com', password_hash='dummy_hash3')
        ]
        for user in users:
            db.session.add(user)
        
        # Create sample categories
        categories = [
            Category(name='Technology', description='Posts about tech and programming'),
            Category(name='Travel', description='Travel experiences and tips'),
            Category(name='Food', description='Recipes and restaurant reviews')
        ]
        for category in categories:
            db.session.add(category)
        
        # Commit to get IDs
        db.session.commit()
        
        # Create sample posts
        posts = [
            Post(
                title='Getting Started with Flask',
                content='Flask is a lightweight WSGI web application framework...',
                author=users[0],
                categories=[categories[0]]
            ),
            Post(
                title='My Trip to Paris',
                content='The city of lights was absolutely beautiful...',
                author=users[1],
                categories=[categories[1]]
            ),
            Post(
                title='Best Pizza in Town',
                content='I discovered this amazing pizzeria...',
                author=users[2],
                categories=[categories[2]]
            ),
            Post(
                title='Tech Stack for Startups',
                content='Choosing the right technology stack is crucial...',
                author=users[0],
                categories=[categories[0]]
            ),
            Post(
                title='Food Guide: Tokyo',
                content='A culinary journey through Tokyo...',
                author=users[1],
                categories=[categories[1], categories[2]]
            )
        ]
        for post in posts:
            db.session.add(post)
        
        db.session.commit()
        print('Database seeded with sample data!')
        
    return app

# Import models after db is defined
from . import models
