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
                '''
            }
        }

        stage('Build & Deploy Containers (Jenkins EC2)') {
            steps {
                sh '''
                    echo "Stopping old containers..."
                    docker rm -f service-a service-b || true
                    docker network rm app-network || true

                    echo "Creating network..."
                    docker network create app-network

                    echo "Building images..."
                    docker build -t microservice-a ./microservice-a
                    docker build -t microservice-b ./microservice-b

                    echo "Starting containers..."
                    docker run -d --name service-b --network app-network -p 5001:5001 microservice-b
                    docker run -d --name service-a --network app-network -p 5000:5000 microservice-a
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    docker ps
                    echo "Checking service-a..."
                    curl http://localhost:5000 || true
                '''
            }
        }

        stage('Deploy to Staging') {
            steps {
                sshagent(credentials: ['staging-ssh']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ec2-user@10.0.1.152 << EOF
                      cd ~/deploy/microservices-devops
                      docker-compose down || true
                      docker-compose up -d
                    EOF
                    '''
                }
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
