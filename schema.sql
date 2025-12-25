-- Link Tracker Database Schema
-- SQLite schema for URL shortener and analytics tracker

-- Drop existing tables if they exist
DROP TABLE IF EXISTS links;
DROP TABLE IF EXISTS analytics;

-- Links table: stores shortened URLs and their metadata
CREATE TABLE links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT UNIQUE NOT NULL,
    original_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    description TEXT
);

-- Analytics table: tracks clicks and visitor information
CREATE TABLE analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link_id INTEGER NOT NULL,
    visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address TEXT,
    user_agent TEXT,
    referrer TEXT,
    FOREIGN KEY (link_id) REFERENCES links (id)
);

-- Create indexes for better query performance
CREATE INDEX idx_links_short_code ON links(short_code);
CREATE INDEX idx_links_created_at ON links(created_at);
CREATE INDEX idx_analytics_link_id ON analytics(link_id);
CREATE INDEX idx_analytics_visited_at ON analytics(visited_at);
