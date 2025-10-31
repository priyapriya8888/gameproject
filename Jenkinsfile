pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/snake-game.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t snake-game .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 snake-game'
            }
        }
    }
}
