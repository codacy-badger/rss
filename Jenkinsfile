pipeline {
    agent any
    stages {
        stage('Install Requirements') {
            steps {
                sh '''
                    sudo pip --no-cache-dir install -r requirements.txt
                '''
            }
        }
        stage('Run Migrations') {
            steps {
                sh '''
                    python manage.py makemigrations
                '''
                sh '''
                    python manage.py migrate
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    python manage.py test
                '''
            }
        }
    }
}
