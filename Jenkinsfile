pipeline {
    agent any

    stages {

        stage('Check Tools') {
            steps {
                echo 'Checking Docker...'
                bat 'docker --version'
                bat 'docker compose version'
            }
        }

        stage('Build & Deploy Containers') {
            steps {
                echo 'Stopping old containers'
                bat 'docker compose down'

                echo 'Building and starting containers'
                bat 'docker compose up -d --build'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Listing running containers'
                bat 'docker ps'
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
