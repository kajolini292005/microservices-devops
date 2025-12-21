pipeline {
    agent any

    stages {
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Webhook Test') {
    steps {
        echo '🔥 Webhook successfully triggered this build!'
    }
}


        stage('Check Tools') {
            steps {
                echo 'Checking Docker...'
                sh 'docker --version'
                sh 'docker compose version'
            }
        }

       stage('Build & Deploy Containers') {
    steps {
        echo 'Stopping and removing old containers...'
        sh 'docker compose down --remove-orphans'
        sh 'docker rm -f service-a service-b || exit 0'

        echo 'Building fresh images...'
        sh 'docker compose build'

        echo 'Starting new containers...'
        sh 'docker compose up -d --build'
    }
}


        stage('Verify Deployment') {
            steps {
                echo 'Listing running containers'
                sh 'docker ps'
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
