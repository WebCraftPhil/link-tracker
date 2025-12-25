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

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
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

## License

See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
