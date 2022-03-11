node {
    checkout scm
    docker.build('build-image', 'Dockerfile').inside {
        stage('package') {
            sh "python -m build"
        }
    }
}
