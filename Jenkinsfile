pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/devops-monitoring-dashboard.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r Microservice-a/requirements.txt'
            }
        }

        stage('Deploy Microservice A') {
            steps {
                sh 'nohup python3 Microservice-a/app.py &'
            }
        }
    }
}
