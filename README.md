# Link Tracker

A URL shortener and analytics tracker application built with Flask and SQLite.

## Features

- URL shortening with custom short codes
- Click analytics and tracking
- RESTful API endpoints
- SQLite database for persistent storage

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/WebCraftPhil/link-tracker.git
cd link-tracker
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your configuration
# Update SECRET_KEY with a secure random key for production
```

### 5. Initialize the Database

```bash
python init_db.py
```

This will create a SQLite database file (`link_tracker.db`) with the necessary schema.

### 6. Run the Application

```bash
# Development mode
python app.py

# Or using Flask CLI
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The application will start on `http://localhost:5000`

## API Endpoints

### Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Returns a welcome message and API status
- **Response**:
  ```json
  {
    "message": "Welcome to Link Tracker API",
    "status": "running",
    "version": "1.0.0"
  }
  ```

### Health Check
- **URL**: `/health`
- **Method**: GET
- **Description**: Returns application health status
- **Response**:
  ```json
  {
    "status": "healthy",
    "database": "link_tracker.db"
  }
  ```

## Project Structure

```
link-tracker/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization script
├── schema.sql          # SQLite database schema
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore         # Git ignore rules
├── LICENSE            # Project license
└── README.md          # Project documentation
```

## Database Schema

### Links Table
Stores shortened URLs and metadata:
- `id`: Primary key
- `short_code`: Unique short code for the URL
- `original_url`: The original long URL
- `created_at`: Timestamp of creation
- `expires_at`: Optional expiration timestamp
- `is_active`: Boolean flag for active links
- `description`: Optional description

### Analytics Table
Tracks click events and visitor information:
- `id`: Primary key
- `link_id`: Foreign key to links table
- `visited_at`: Timestamp of the visit
- `ip_address`: Visitor IP address
- `user_agent`: Browser user agent
- `referrer`: HTTP referrer

## Development

### Running Tests

```bash
pytest
```

### Code Style

This project follows PEP 8 style guidelines for Python code.

## Environment Variables

- `FLASK_ENV`: Flask environment (development/production/testing)
- `SECRET_KEY`: Secret key for Flask sessions (change in production)
- `PORT`: Port number for the application (default: 5000)
- `DATABASE`: SQLite database file path (default: link_tracker.db)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the terms in the LICENSE file.

## Support

For issues and questions, please open an issue on the GitHub repository.
