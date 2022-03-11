node {
    docker.build('build-image', 'Dockerfile').inside {
        checkout scm
        stage('package') {
            sh "python -m build"
        }
    }
}
