# Load balancer and development environment setup
https://www.youtube.com/watch?v=42Q65H8ch7U

https://www.youtube.com/watch?v=0H2miBK_gAk

# Create a venv 
    https://docs.python.org/3/library/venv.html 

    python3 -m venv tutorial-b

    source tutorial-b/bin/activate

    deactivate

# Install flask and gunicorn
    pip3 install flask, gunicorn

# Create requirements.txt
    pip3 list

    pip3 freeze > requirements.txt
    
# Create simple flask application app.py
    https://flask.palletsprojects.com/en/2.2.x/

    flask run
    http://127.0.0.1:5000/

# Create a Dockerfile
    https://docs.docker.com/samples/flask/

# Build Image and run
    docker build . -t webapp:2.0

    docker run -dp 5000:5000 webapp:2.0

    http://0.0.0.0/5000

# Create a docker-compose.yaml and run
    
    docker-compose up
    
    http://0.0.0.0
    
    docker-compose down
    
    docker-compose up -d --build --scale app=3

Add a render_template for container ID


