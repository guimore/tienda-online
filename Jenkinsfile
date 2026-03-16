pipeline {
    agent any
    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/guimore/tienda-online'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'docker build -t tienda-online .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 --name tienda tienda-online'
            }
        }
    }
}