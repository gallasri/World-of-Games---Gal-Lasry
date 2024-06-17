pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 --name myapp myapp'
            }
        }

        stage('Test') {
            steps {
                sh 'python e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker rm -f myapp'
                sh 'docker push myapp'
            }
        }
    }
}
