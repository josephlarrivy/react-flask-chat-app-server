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
  chat_id TEXT PRIMARY KEY UNIQUE NOT NULL,
  chat_name TEXT NOT NULL,
  chat_owner TEXT REFERENCES users(username) NOT NULL
);

CREATE TABLE user_chatnames (
  user_id TEXT REFERENCES users(username) ON DELETE CASCADE,
  chat_id TEXT REFERENCES chatnames(chat_id) ON DELETE CASCADE,
  PRIMARY KEY (user_id, chat_id)
);