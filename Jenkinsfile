pipeline {
  agent any
  stages {
    stage('Clone Git Repo') {
      steps {
        sh 'mkdir -p build'
        sh 'cd build'
        sh 'git clone https://github.com/stanton11/aws_cleanup_script.git'
      }
    }
    
      stage('Run Script') {
        steps {
          withCredentials([string(credentialsId: 'k8s_aws_id', variable: 'ID'), string(credentialsId: 'k8s_aws_key', variable: 'KEY')]) {
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate && pip3 install boto3'
          sh 'echo $ID $KEY'
          sh '. venv/bin/activate && python3 aws_cleanup_automation.py $ID $KEY'
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