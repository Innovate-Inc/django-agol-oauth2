node {
    checkout scm
    docker.build('build-image').inside {
        stage('package') {
            sh "python -m build"
        }
    }
}
