pipeline {
    agent any
    environment {
        DJANGO_SETTINGS_MODULE = 'library.settings'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Asmita1507/django-library-devops.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Create virtual environment using Python
                bat 'python -m venv venv' // Windows command for creating virtualenv
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt' // Activate virtualenv and install dependencies
                // Install distutils if it's missing
                bat 'venv\\Scripts\\activate && pip install distutils' // Install distutils explicitly
            }
        }
        stage('Run Tests') {
            steps {
                // Running tests inside the activated virtual environment
                bat 'venv\\Scripts\\activate && python manage.py test --verbosity=2' // Run the tests
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
            echo 'Some tests failed!'
        }
    }
}
