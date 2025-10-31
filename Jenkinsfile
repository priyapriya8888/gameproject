pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/priyapriya8888/gameproject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // ✅ Use python -m pip (works even if pip command isn't in PATH)
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                // ✅ Add docker version check (helps debug PATH issues)
                bat 'docker --version'
                bat 'docker build -t snake-game .'
            }
        }

        stage('Deploy Container') {
            steps {
                // ✅ Stop old container if already running
                bat 'docker stop snake-game || echo "No existing container"'
                bat 'docker rm snake-game || echo "No container to remove"'

                // ✅ Run new container
                bat 'docker run -d -p 5000:5000 --name snake-game snake-game'
            }
        }
    }
}
