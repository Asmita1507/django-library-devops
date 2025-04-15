pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Asmita1507/django-library-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m venv venv
                    source venv/bin/activate || venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate || venv\\Scripts\\activate
                    python manage.py test
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed"
        }
    }
}
