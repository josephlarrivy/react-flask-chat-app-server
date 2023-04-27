CREATE DATABASE chat_app_database;

DROP TABLE IF EXISTS user_chatnames;
DROP TABLE IF EXISTS chatnames;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  username TEXT PRIMARY KEY NOT NULL,
  password TEXT NOT NULL,
  email VARCHAR
);

CREATE TABLE chatnames (
  chat_id INTEGER PRIMARY KEY NOT NULL,
  chat_name TEXT NOT NULL
);

CREATE TABLE user_chatnames (
  user_id TEXT REFERENCES users(username) ON DELETE CASCADE,
  chat_id INTEGER REFERENCES chatnames(chat_id) ON DELETE CASCADE,
  PRIMARY KEY (user_id, chat_id)
);
