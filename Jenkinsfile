pipeline {
    agent any

    environment {
        // 👇 Your actual Python installation path
        PYTHON_HOME = 'C:\\Users\\Vishnupriya\\AppData\\Local\\Programs\\Python\\Python312'
        PATH = "${env.PATH};${env.PYTHON_HOME};${env.PYTHON_HOME}\\Scripts"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📦 Cloning repository..."
                git 'https://github.com/priyapriya8888/gameproject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "🐍 Installing Python dependencies..."
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                bat 'docker --version'
                bat 'docker build -t snake-game .'
            }
        }

        stage('Deploy Container') {
            steps {
                echo "🚀 Deploying container..."
                // Stop old container if already running
                bat 'docker stop snake-game || echo "No existing container"'
                bat 'docker rm snake-game || echo "No container to remove"'

                // Run new one
                bat 'docker run -d -p 5000:5000 --name snake-game snake-game'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "🔍 Checking running containers..."
                bat 'docker ps'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check above logs."
        }
    }
}
