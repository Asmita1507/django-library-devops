pipeline {
           agent any
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
           }
           post {
               success {
                   echo 'Testing completed successfully!'
               }
               failure {
                   echo 'Tests failed!'
               }
           }
       }
