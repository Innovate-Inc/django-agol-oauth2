node {
    docker.image('python:3.7').inside {
        checkout scm
        stage('setup python build tools') {
            sh "pip install --upgrade build"
        }
        stage('package') {
            sh "python -m build"
        }
    }
}
