node {
    try {
        checkout scm
        docker.build('build-image').inside {
            stage('package') {
                sh "python -m build"
            }
            stage('commit to DMT') {
                withCredentials([
                    gitUsernamePassword(credentialsId: 'd68c969d-4750-418f-aec5-9fc2e194fc4f', gitToolName: 'Default')
                ]) {
                    sh "git clone https://github.com/Innovate-Inc/R9-DMT.git"
                    dir('./R9-DMT') {
                        sh 'git config user.email "innovate-services@innovateteam.com"'
                        sh 'git config user.name "Innovate Services"'
                        sh "cp ../dist/*.whl ./"
                        sh "git add *.whl"
                        sh 'git commit -am "updated django_agol_oauth2"'
                        sh 'git push'
                    }
                }
            }
        }
    } finally {
        cleanWs()
    }
}
