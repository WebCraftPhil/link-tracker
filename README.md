# link-tracker

A URL shortener and analytics tracker built with Python Flask, Jupyter Notebook, and SQLite.

## Features

- 🔗 **URL Shortening**: Create short, easy-to-share links
- 📊 **Analytics Dashboard**: Track clicks, referrers, and user agents in real-time
- 📈 **Data Visualization**: Jupyter Notebook with detailed analytics and visualizations
- 💾 **SQLite Database**: Lightweight database for storing links and click data
- 🎨 **Modern UI**: Beautiful, responsive web interface
- 🔒 **Click Tracking**: Capture IP addresses, user agents, referrers, and timestamps

## Installation

### Prerequisites
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

### Setup

1. Clone the repository:
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/WebCraftPhil/link-tracker.git
cd link-tracker
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Flask Application

Start the Flask web server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

**Note:** The application runs in debug mode for development purposes. For production deployment, use a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Web Interface

- **Home Page** (`/`): Create shortened URLs
- **Analytics Dashboard** (`/analytics`): View statistics and link performance
- **Redirect** (`/<short_code>`): Automatically redirects to the original URL

### API Endpoints

#### Shorten URL
```bash
POST /shorten
Content-Type: application/json

{
  "url": "https://example.com/very/long/url"
}

Response:
{
  "short_url": "http://localhost:5000/abc12345",
  "short_code": "abc12345"
}
```

#### Get All Analytics
```bash
GET /api/analytics

Response: Array of link objects with click counts
```

#### Get Detailed Analytics for a Link
```bash
GET /api/analytics/<short_code>

Response: Detailed analytics including all clicks
```

### Jupyter Notebook Analytics

Launch Jupyter Notebook for advanced analytics:

```bash
jupyter notebook analytics.ipynb
```

The notebook includes:
- Overview statistics
- Top clicked links
- Click distribution over time
- Hourly click patterns
- Referrer analysis
- Browser/User agent analysis
- Unique visitor tracking
- Recent activity logs
- Export functionality for CSV reports
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
- `id`: Primary key
- `short_code`: Unique short code for the URL
- `original_url`: The original long URL
- `created_at`: Timestamp when the link was created

### Clicks Table
- `id`: Primary key
- `link_id`: Foreign key to links table
- `clicked_at`: Timestamp of the click
- `ip_address`: IP address of the visitor
- `user_agent`: Browser/device information
- `referrer`: Source URL (if available)

## Project Structure

```
link-tracker/
├── app.py                  # Main Flask application
├── analytics.ipynb         # Jupyter Notebook for analytics
├── requirements.txt        # Python dependencies
├── link_tracker.db        # SQLite database (created on first run)
├── templates/             # HTML templates
│   ├── index.html         # Home page
│   ├── result.html        # Success page after shortening
│   ├── analytics.html     # Analytics dashboard
│   └── 404.html          # Error page
└── README.md             # This file
```

## Technologies Used

- **Flask**: Web framework for Python
- **SQLite**: Lightweight database
- **shortuuid**: Generate unique short codes
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive analytics environment

## Development

### Adding New Features

The application is designed to be easily extensible:

- Add new routes in `app.py`
- Create new templates in the `templates/` directory
- Extend database schema by modifying the `init_db()` function
- Add visualizations in `analytics.ipynb`

### Security Considerations

This is a basic implementation. For production use, consider:

- Adding rate limiting to prevent abuse
- Implementing user authentication
- Validating and sanitizing URLs
- Adding HTTPS support
- Implementing link expiration
- Adding custom short codes
- Blacklisting malicious URLs
- Adding CAPTCHA for URL submission
- Implementing proper session management

## Privacy

The application implements basic privacy measures:

- IP addresses are anonymized (last octet replaced with "xxx")
- No personally identifiable information is collected beyond anonymized IPs and user agents
- For production use, implement:
  - User consent mechanisms
  - GDPR compliance features
  - Data retention policies
  - Right to deletion functionality

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
