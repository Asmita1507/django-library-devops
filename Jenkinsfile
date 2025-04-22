pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub_id')
        DOCKER_IMAGE = "sagar/django-library"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Asmita1507/django-library-devops.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'if exist venv rmdir /s /q venv'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && python manage.py test'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% .'
                bat 'docker tag %DOCKER_IMAGE%:%BUILD_NUMBER% %DOCKER_IMAGE%:latest'
            }
        }
        stage('Push Docker Image') {
            steps {
                bat 'echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin'
                bat 'docker push %DOCKER_IMAGE%:%BUILD_NUMBER%'
                bat 'docker push %DOCKER_IMAGE%:latest'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up -d --build'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully! Docker image pushed and deployed.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
