pipeline {
  agent any
  stages {
    stage('Clone Git Repo') {
      steps {
        sh 'mkdir -p build'
        sh 'cd build'
        sh 'git clone git@github.com:stanton11/aws_cleanup_script.git'
      }
    }
    withCredentials([string(credentialsId: 'k8s-aws-access-key-id', variable: 'k8s-aws-access-key-id'), string(credentialsId: 'k8s-aws-secret-access-key', variable: 'k8s-aws-secret-access-key')]) {
      stage('Run Script') {
        steps {
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate && pip3 install boto3'
          sh '. venv/bin/activate && python3 aws_cleanup_automation.py $k8s-aws-access-key-id $k8s-aws-secret-access-key'
        }
      }
    }
    
  }
  post {
    always {
      cleanWs()
    }
  }

}