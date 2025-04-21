pipeline {
    agent any
    environment {
        DJANGO_SETTINGS_MODULE = 'library.settings'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    credentialsId: '4239d8ac-fb6a-4833-a06e-66bdb34cf65d', 
                    url: 'https://github.com/Asmita1507/django-library-devops.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Clean up existing virtual environment
                bat 'if exist venv rmdir /s /q venv'
                // Create virtual environment
                bat 'python -m venv venv'
                // Activate and upgrade pip, then install dependencies
                bat '''
                    venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests in the activated virtual environment
                bat '''
                    venv\\Scripts\\activate
                    python manage.py test --verbosity=2
                '''
            }
        }
    }
    post {
        always {
            echo 'Testing completed!'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
    }
}
