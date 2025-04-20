pipeline {
    agent any
    tools {
        python 'Python310'
    }
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
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python manage.py test --verbosity=2'
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
