# Full Stack Blog Application

A modern blog application built with Flask backend and React frontend.

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── __init__.py      # Flask app initialization
│   │   ├── models.py        # Database models
│   │   ├── config.py        # Configuration settings
│   │   └── api/            
│   │       ├── __init__.py  # API blueprint
│   │       └── routes.py    # API endpoints
│   ├── run.py              # Application entry point
│   ├── requirements.txt    # Python dependencies
│   └── run_backend.sh     # Backend startup script
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── services/      # API services
│   │   ├── types/         # TypeScript interfaces
│   │   ├── App.tsx        # Main App component
│   │   └── index.tsx      # React entry point
│   ├── package.json       # Node.js dependencies
│   └── run_frontend.sh    # Frontend startup script
```

## Features

### Backend (Flask)
- RESTful API design
- SQLAlchemy ORM for database management
- Flask-Migrate for database migrations
- CORS support for frontend integration
- Sample data seeding
- Environment-based configuration

### Frontend (React)
- TypeScript for type safety
- React Router for navigation
- Axios for API calls
- Modern component architecture
- Responsive design

## API Endpoints

- `GET /api/v1/users` - List all users
- `GET /api/v1/users/<id>` - Get user details
- `GET /api/v1/posts` - List all posts
- `GET /api/v1/posts/<id>` - Get post details
- `POST /api/v1/posts` - Create new post
- `GET /api/v1/categories` - List all categories
- `GET /api/v1/categories/<id>/posts` - Get posts in category

## Setup

### Backend Setup
1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend:
   ```bash
   ./run_backend.sh
   ```
   The backend will start on http://localhost:5001

### Frontend Setup
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the frontend:
   ```bash
   ./run_frontend.sh
   ```
   The frontend will start on http://localhost:3001

## Database Models

### User
- id: Primary key
- username: Unique username
- email: Unique email
- posts: One-to-many relationship with Posts

### Post
- id: Primary key
- title: Post title
- content: Post content
- user_id: Foreign key to User
- categories: Many-to-many relationship with Categories

### Category
- id: Primary key
- name: Category name
- description: Category description
- posts: Many-to-many relationship with Posts

## Development

### Running in Development Mode
1. Start the backend:
   ```bash
   cd backend
   ./run_backend.sh
   ```

2. In a separate terminal, start the frontend:
   ```bash
   cd frontend
   ./run_frontend.sh
   ```

### Available Scripts

Backend:
- `flask db migrate` - Generate database migrations
- `flask db upgrade` - Apply migrations
- `flask seed-db` - Seed database with sample data

Frontend:
- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
