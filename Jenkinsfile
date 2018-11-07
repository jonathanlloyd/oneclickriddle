pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                echo 'Installing..'
                sh 'make venv'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'make test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
