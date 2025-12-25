"""
Flask URL Shortener and Analytics Tracker Application
Main application file.
"""

import os
from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Load configuration from environment variables
secret_key = os.environ.get('SECRET_KEY')
if not secret_key:
    # Only use default in development, warn in production
    flask_env = os.environ.get('FLASK_ENV', 'production')
    if flask_env == 'development':
        secret_key = 'dev-secret-key-change-in-production'
        print("WARNING: Using default SECRET_KEY for development. Set SECRET_KEY environment variable for production.")
    else:
        raise ValueError("SECRET_KEY environment variable must be set in production")

app.config['SECRET_KEY'] = secret_key
app.config['DATABASE'] = os.environ.get('DATABASE', 'link_tracker.db')


@app.route('/')
def index():
    """
    Root endpoint - returns a welcome message.
    """
    return jsonify({
        'message': 'Welcome to Link Tracker API',
        'status': 'running',
        'version': '1.0.0'
    })


@app.route('/health')
def health():
    """
    Health check endpoint - returns application status.
    """
    return jsonify({
        'status': 'healthy',
        'database': app.config['DATABASE']
    })


if __name__ == '__main__':
    # Run the application
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=debug_mode
    )
