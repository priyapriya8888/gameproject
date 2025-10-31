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
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t snake-game .'
            }
        }
        stage('Deploy Container') {
            steps {
                bat 'docker run -d -p 5000:5000 snake-game'
            }
        }
    }
}
