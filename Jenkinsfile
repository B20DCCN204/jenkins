pipeline{
    agent any

    environment {
        DOCKER_USERNAME = "jangg"
        IMAGE_NAME = "${DOCKER_USERNAME}/flaskimg:1.0"  
        DOCKER_HUB_CREDENTIALS = "dockerhub-acc"
        CONTAINER_NAME = "sum-test-container"
    }

    stages {
        stage('Clone repository'){
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image'){
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage("Run Tests") {
            steps {
                script {
                    sh "docker run --rm -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                    sleep 5
                    sh "python -m unittest discover -s tests -p 'test_*.py'"
                    sh "docker stop ${CONTAINER_NAME}"
                }
            }
        }

        stage("Push to DockerHub") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-acc', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "docker login -u $USER -p $PASS"
                }
                sh "docker push ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            echo "Job completed! Cleaning up resources..."
        }
        success {
            echo "Build & Test Passed! Image push to DockerHub successfully!"
        }
        failure {
            echo "Job failed! Cleaning up unused Docker resources..."
        }
    }
}