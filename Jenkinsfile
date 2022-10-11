pipeline {
  agent any
  environment {
    GITLAB_CREDENTIALS = credentials('gitlab-couchbaseqe')
    REPO_URL = "git@github.com:stanton11/aws_cleanup_script.git"
  }
  stages {
    stage('Clone Git Repo') {
      steps {
        sh 'mkdir -p build'
        dir('build') {
            git branch: 'master', credentialsId:     $GITLAB_CREDENTIALS, url: $REPO_URL
            }
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
    post {
      always {
        cleanWs()
      }
    }
  }