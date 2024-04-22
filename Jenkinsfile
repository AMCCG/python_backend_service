pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Build Image') {
            steps {
                echo 'Building Image..'
                bat 'docker --version'
                bat 'docker build -t hello-fastapi:0.0.1-JENKINS .'
            }
        }
        stage('Deploy') {
            steps {
                timeout(time: 15, unit: "MINUTES") {
                    input message: 'Do you want to approve the deployment?', ok: 'Yes'
                }
                echo 'Deploying....'
                bat 'docker run -d --name hello-fastapi -p 8000:8000 hello-fastapi:0.0.1-JENKINS'
            }
        }
    }
}