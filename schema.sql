-- Link Tracker Database Schema
-- SQLite schema for URL shortener and analytics tracker

-- Drop existing tables if they exist
DROP TABLE IF EXISTS clicks;
DROP TABLE IF EXISTS links;

-- Links table: stores shortened URLs and their metadata
CREATE TABLE links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT UNIQUE NOT NULL,
    original_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Clicks table: tracks clicks and visitor information
CREATE TABLE clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link_id INTEGER NOT NULL,
    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address TEXT,
    user_agent TEXT,
    referrer TEXT,
    FOREIGN KEY (link_id) REFERENCES links (id)
);

-- Create indexes for better query performance
CREATE INDEX idx_links_short_code ON links(short_code);
CREATE INDEX idx_links_created_at ON links(created_at);
CREATE INDEX idx_clicks_link_id ON clicks(link_id);
CREATE INDEX idx_clicks_clicked_at ON clicks(clicked_at);
