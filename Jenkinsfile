pipeline {
  agent any
  stages {
    stage('Install Requirements') {
      steps {
        sh '''
          sudo pip --no-cache-dir install -r requirments.txt
        '''
      }
    }
    stage('Run Tests') {
      steps {
        sh "nosetests --nocapture --with-xunit --with-coverage --cover-xml Tests/food.py --cover-inclusive --cover-package=start"
      }
    }
  }
}
