pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kajolini292005/microservices-devops.git'
            }
        }

        stage('Webhook Test') {
            steps {
                echo '🔥 Webhook successfully triggered this build!'
            }
        }

        stage('Check Tools') {
            steps {
                sh '''
                    docker --version
                    docker-compose --version
                '''
            }
        }

        stage('Build & Deploy Containers') {
            steps {
                sh '''
                    echo "Stopping old containers..."
                    docker-compose down --remove-orphans || true
                    docker rm -f service-a service-b || true

                    echo "Building images..."
                    docker-compose build

                    echo "Starting containers..."
                    docker-compose up -d
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully 🎉'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
