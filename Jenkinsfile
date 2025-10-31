pipeline {
    agent any

    environment {
        // ✅ Python + Docker Paths
        PYTHON_HOME = 'C:\\Users\\Vishnupriya\\AppData\\Local\\Programs\\Python\\Python312'
        DOCKER_HOME = 'C:\\Program Files\\Docker\\Docker\\resources\\bin'
        PATH = "${env.PATH};${env.PYTHON_HOME};${env.PYTHON_HOME}\\Scripts;${env.DOCKER_HOME}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "📦 Cloning Snake Game repository..."
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
                echo "🐳 Building Docker image for Snake Game..."
                bat 'docker --version'
                // Use lightweight base image if possible (make sure Dockerfile uses python:3.12-slim)
                bat 'docker build -t snakegame:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                echo "🔐 Logging into Docker Hub..."
                bat 'docker logout || exit 0'  // ensure fresh login
                bat 'docker login -u vishnupriya68 -p "Shivapriya123@"'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "⬆️ Pushing Docker image to Docker Hub (repo: snakegame)..."
                script {
                    retry(2) {
                        bat 'docker tag snakegame:v1 vishnupriya68/snakegame:latest'
                        // Limit concurrent uploads for Windows reliability
                        bat 'docker push --max-concurrent-uploads 1 vishnupriya68/snakegame:latest'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "🚀 Deploying Snake Game to Kubernetes..."
                withEnv(['KUBECONFIG=C:\\Users\\Vishnupriya\\.kube\\config']) {
                    bat 'kubectl apply -f deployment.yaml --validate=false'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "🔍 Checking Kubernetes Pods and Services..."
                withEnv(['KUBECONFIG=C:\\Users\\Vishnupriya\\.kube\\config']) {
                    bat 'kubectl get pods'
                    bat 'kubectl get svc'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Snake Game pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed! Please check above logs."
        }
    }
}
