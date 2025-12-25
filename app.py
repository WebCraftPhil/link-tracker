import os
import sqlite3
from datetime import datetime
from flask import Flask, request, redirect, render_template, jsonify, url_for
import shortuuid

app = Flask(__name__)
app.config['DATABASE'] = 'link_tracker.db'

def get_db():
    """Get database connection"""
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """Initialize the database"""
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                short_code TEXT UNIQUE NOT NULL,
                original_url TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS clicks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link_id INTEGER NOT NULL,
                clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT,
                user_agent TEXT,
                referrer TEXT,
                FOREIGN KEY (link_id) REFERENCES links (id)
            )
        ''')
        db.commit()
        db.close()

def generate_short_code():
    """Generate a unique short code"""
    return shortuuid.uuid()[:8]

@app.route('/')
def index():
    """Home page with URL shortener form"""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Shorten a URL"""
    original_url = request.form.get('url') or request.json.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Add http:// if no scheme is provided
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url
    
    # Basic URL validation to prevent malicious URLs
    if not original_url.startswith(('http://', 'https://')):
        return jsonify({'error': 'Invalid URL scheme'}), 400
    
    db = get_db()
    
    # Check if URL already exists
    existing = db.execute('SELECT short_code FROM links WHERE original_url = ?', 
                         (original_url,)).fetchone()
    
    if existing:
        short_code = existing['short_code']
    else:
        # Generate unique short code
        while True:
            short_code = generate_short_code()
            exists = db.execute('SELECT id FROM links WHERE short_code = ?', 
                              (short_code,)).fetchone()
            if not exists:
                break
        
        # Insert new link
        db.execute('INSERT INTO links (short_code, original_url) VALUES (?, ?)',
                  (short_code, original_url))
        db.commit()
    
    db.close()
    
    short_url = request.host_url + short_code
    
    if request.is_json:
        return jsonify({'short_url': short_url, 'short_code': short_code})
    else:
        return render_template('result.html', short_url=short_url, original_url=original_url)

@app.route('/<short_code>')
def redirect_url(short_code):
    """Redirect to original URL and track analytics"""
    db = get_db()
    
    # Get link
    link = db.execute('SELECT id, original_url FROM links WHERE short_code = ?', 
                     (short_code,)).fetchone()
    
    if not link:
        db.close()
        return render_template('404.html'), 404
    
    # Track click (anonymize IP for privacy)
    anonymized_ip = request.remote_addr.rsplit('.', 1)[0] + '.xxx' if request.remote_addr else 'unknown'
    db.execute('''
        INSERT INTO clicks (link_id, ip_address, user_agent, referrer)
        VALUES (?, ?, ?, ?)
    ''', (link['id'], 
          anonymized_ip,
          request.headers.get('User-Agent'),
          request.headers.get('Referer')))
    db.commit()
    db.close()
    
    return redirect(link['original_url'])

@app.route('/analytics')
def analytics():
    """Show analytics dashboard"""
    return render_template('analytics.html')

@app.route('/api/analytics')
def api_analytics():
    """Get analytics data as JSON"""
    db = get_db()
    
    # Get all links with click counts
    links = db.execute('''
        SELECT l.id, l.short_code, l.original_url, l.created_at,
               COUNT(c.id) as click_count
        FROM links l
        LEFT JOIN clicks c ON l.id = c.link_id
        GROUP BY l.id
        ORDER BY click_count DESC
    ''').fetchall()
    
    result = []
    for link in links:
        result.append({
            'id': link['id'],
            'short_code': link['short_code'],
            'short_url': request.host_url + link['short_code'],
            'original_url': link['original_url'],
            'created_at': link['created_at'],
            'click_count': link['click_count']
        })
    
    db.close()
    return jsonify(result)

@app.route('/api/analytics/<short_code>')
def api_analytics_detail(short_code):
    """Get detailed analytics for a specific link"""
    db = get_db()
    
    # Get link
    link = db.execute('SELECT * FROM links WHERE short_code = ?', 
                     (short_code,)).fetchone()
    
    if not link:
        db.close()
        return jsonify({'error': 'Link not found'}), 404
    
    # Get clicks
    clicks = db.execute('''
        SELECT clicked_at, ip_address, user_agent, referrer
        FROM clicks
        WHERE link_id = ?
        ORDER BY clicked_at DESC
    ''', (link['id'],)).fetchall()
    
    click_list = []
    for click in clicks:
        click_list.append({
            'clicked_at': click['clicked_at'],
            'ip_address': click['ip_address'],
            'user_agent': click['user_agent'],
            'referrer': click['referrer']
        })
    
    result = {
        'short_code': link['short_code'],
        'short_url': request.host_url + link['short_code'],
        'original_url': link['original_url'],
        'created_at': link['created_at'],
        'click_count': len(click_list),
        'clicks': click_list
    }
    
    db.close()
    return jsonify(result)

if __name__ == '__main__':
    init_db()
    # Debug mode should only be used in development
    # For production, use a WSGI server like Gunicorn or uWSGI
    app.run(debug=True, host='0.0.0.0', port=5000)
