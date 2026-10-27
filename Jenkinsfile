
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code fetched from GitHub'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
    }
}
