from flask import jsonify, request
from . import api
from .. import db
from ..models import User, Post, Category

@api.route('/health', methods=['GET'])
def health_check():
    """Basic health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200

@api.route('/example', methods=['GET', 'POST'])
def example():
    """Example endpoint demonstrating GET and POST methods"""
    if request.method == 'GET':
        return jsonify({
            'message': 'This is a GET request',
            'status': 'success'
        })
    
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({
            'message': 'This is a POST request',
            'received_data': data,
            'status': 'success'
        })

# User routes
@api.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'post_count': user.posts.count()
    } for user in users])

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID with their posts"""
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'posts': [{
            'id': post.id,
            'title': post.title,
            'categories': [c.name for c in post.categories]
        } for post in user.posts]
    })

# Post routes
@api.route('/posts', methods=['GET'])
def get_posts():
    """Get all posts with optional category filter"""
    category_name = request.args.get('category')
    if category_name:
        category = Category.query.filter_by(name=category_name).first_or_404()
        posts = category.posts
    else:
        posts = Post.query.all()
    
    return jsonify([{
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'categories': [c.name for c in post.categories],
        'created_at': post.created_at.isoformat()
    } for post in posts])

@api.route('/posts', methods=['POST'])
def create_post():
    """Create a new post"""
    data = request.get_json()
    
    # Validate user
    user = User.query.get_or_404(data['user_id'])
    
    # Get categories
    categories = []
    for cat_name in data.get('categories', []):
        category = Category.query.filter_by(name=cat_name).first()
        if category:
            categories.append(category)
    
    post = Post(
        title=data['title'],
        content=data['content'],
        author=user,
        categories=categories
    )
    
    db.session.add(post)
    db.session.commit()
    
    return jsonify({
        'message': 'Post created successfully',
        'post_id': post.id
    }), 201

@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Get post by ID"""
    post = Post.query.get_or_404(post_id)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': {
            'id': post.author.id,
            'username': post.author.username
        },
        'categories': [{
            'id': c.id,
            'name': c.name
        } for c in post.categories],
        'created_at': post.created_at.isoformat(),
        'updated_at': post.updated_at.isoformat()
    })

# Category routes
@api.route('/categories', methods=['GET'])
def get_categories():
    """Get all categories with post count"""
    categories = Category.query.all()
    return jsonify([{
        'id': category.id,
        'name': category.name,
        'description': category.description,
        'post_count': category.posts.count()
    } for category in categories])

@api.route('/categories/<int:category_id>/posts', methods=['GET'])
def get_category_posts(category_id):
    """Get all posts in a category"""
    category = Category.query.get_or_404(category_id)
    return jsonify({
        'category': category.name,
        'posts': [{
            'id': post.id,
            'title': post.title,
            'author': post.author.username,
            'created_at': post.created_at.isoformat()
        } for post in category.posts]
    }) 