# Flask Visitor Counter with MongoDB

A simple Flask application that tracks visitor counts using MongoDB, fully containerized with Docker.

## Setup

1. **Clone the Repository**:  
   `git clone https://github.com/andresgamo/visitors_counter.git`  
   `cd visitors_counter`

2. **Install Dependencies**:  
   Ensure all necessary Python packages are installed:  
   `pip install -r requirements.txt`

3. **Build and Run Containers**:  
   `docker-compose up --build`

4. **Access the Application**:  
   Open your browser and navigate to `http://localhost:5001/home` to see the visitor count.

## Project Files

- **app.py**: Contains the Flask application code, defining the `/home` endpoint to increment and return the visitor count.
- **Dockerfile**: Defines the environment and dependencies for the Flask application.
- **docker-compose.yml**: Configures the multi-container setup, including the Flask app and MongoDB.
- **requirements.txt**: Lists the Python dependencies needed to run the application.

## Services

- **web**: The Flask application running on port `5000`, mapped to port `5001` on your local machine.
- **mongo**: MongoDB service running on port `27017`.

## API Endpoint

- **GET /home**: Increments and returns the visitor count in JSON format.
