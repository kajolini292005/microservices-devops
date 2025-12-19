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
        echo 'Stopping and removing old containers...'
        bat 'docker compose down --remove-orphans'
        bat 'docker rm -f service-a service-b || exit 0'

        echo 'Building fresh images...'
        bat 'docker compose build'

        echo 'Starting new containers...'
        bat 'docker compose up -d'
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
