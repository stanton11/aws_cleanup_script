pipeline {
  agent any
  stages {
    stage('Clone Git Repo') {
      steps {
        sh 'mkdir -p build'
        sh '''dir(\'build\') {
            git branch: \'master\', credentialsId:     $GITLAB_CREDENTIALS, url: $REPO_URL
        }  '''
        }
      }

      stage('Run Script') {
        steps {
          sh 'cd build'
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate && pip3 install boto3'
          sh '. venv/bin/activate && python3 aws_cleanup_automation.py'
        }
      }

    }
  }