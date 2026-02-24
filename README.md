**Mental Health Support Chatbot**

A multi-turn AI companion powered by Google Gemini 2.5 Flash Lite, designed to provide a safe and empathetic space for users to express their thoughts and emotions.

💡 Overview

This project is an AI-driven mental health support chatbot that allows context-aware, multi-turn conversations and generates a chat summary for user reflection.

It includes secure authentication and session-based memory, ensuring users can interact seamlessly without permanent data storage.

✨ Features

🧠 Multi-Turn Conversation

Context-aware AI responses

Maintains session-based chat history

Real-time interaction

📝 Chat Summary

AI-generated summary of conversation

Helps users reflect on previous prompts and responses

🔒 Privacy Focused

No permanent database storage

Data resets when the app restarts or session ends

🧩 Project Structure

app.py — Main App

Handles user interface and main chat workflow

Manages chat history and session state

Entry point connecting frontend with backend

config.py — App Configuration

Stores API key and model settings

Centralized global constants

services/logger_service.py — Logging

Tracks API calls and errors for monitoring

Provides debugging info

requirements.txt — Dependencies

Lists all required Python libraries (including google-generativeai)

🧠 How It Works

User inputs a message through the chat interface

Chat history and system prompts are combined to provide context

Request is sent to Google Gemini API to generate a response

Response is returned to the user and logged for monitoring

Chat history is maintained temporarily within the session

AWS EC2 Deployment Guide

Launch an EC2 Instance on Amazon Web Services

Choose Ubuntu Server

Instance type: t3.micro (free tier eligible)

Add Security Group

Connect to EC2

Update the system
sudo apt update && sudo apt upgrade

Install Python & required tools
sudo apt install python3-pip python3

Upload project from local machine

Navigate to project folder
cd mental-health-chatbot

Create virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Add Streamlit secrets (API key)
nano .env


Run the Streamlit app
nohup streamlit run app.py

Navigate to project folder -cd mental-health-chatbot

Create virtual environment -python3 -m venv venv -source venv/bin/activate

Install dependencies -pip install -r requirements.txt
Add Streamlit secrets (API key) -nano .env [Open the terminal and add your API key using the Streamlit secrets configuration. Use the EC2 terminal to securely configure the API key in the secrets.toml file.]
Run the Streamlit app -nohup streamlit run app.py
