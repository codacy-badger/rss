pipeline {
  agent any
  stages {
    stage('Install Requirements') {
      steps {
        sh '''
          sudo pip --no-cache-dir install -r requirements.txt
        '''
      }
    }
  }
}
