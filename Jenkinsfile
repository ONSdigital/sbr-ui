#!/usr/bin/env groovy

// Global scope required for multi-stage persistence
def artServer = Artifactory.server 'art-p-01'
def buildInfo = Artifactory.newBuildInfo()
def distDir = 'build/dist/'
def agentPythonVersion = 'python_3.6.0'

pipeline {
    libraries {
        lib('jenkins-pipeline-shared')
    }
    environment {
        SVC_NAME = "sbr-ui"
        ORG = "SBR"
        LANG = "en_US.UTF-8"
    }
    options {
        skipDefaultCheckout()
        buildDiscarder(logRotator(numToKeepStr: '30', artifactNumToKeepStr: '30'))
        timeout(time: 1, unit: 'HOURS')
        ansiColor('xterm')
        timestamps()
    }
    agent { label 'download.jenkins.slave' }
    stages {
        stage('Checkout') {
            agent { label 'download.jenkins.slave' }
            steps {
                checkout scm
                script {
                    buildInfo.name = "${SVC_NAME}"
                    buildInfo.number = "${BUILD_NUMBER}"
                    buildInfo.env.collect()
                }
                colourText("info", "BuildInfo: ${buildInfo.name}-${buildInfo.number}")
                stash name: 'Checkout'
            }
        }

        stage('Build'){
            agent { label "build.${agentPythonVersion}" }
            steps {
                unstash name: 'Checkout'
                sh 'python3.6 --version'
                sh 'python3.6 -c "import locale; locale.setlocale(locale.LC_ALL, \'\')"'
                sh 'python3.6 -v -m venv venv'
                sh 'source venv/bin/activate'

				sh '''
				mkdir -p $HOME/.pip
                cat > $HOME/.pip/pip.conf <<WHATEVS3
[install]
user = true

[global]
index-url=http://af-py-pi:JNJl6DEVMtQ2M9k0t8zc@art-p-01.ons.statistics.gov.uk/artifactory/api/pypi/yr-python/simple
trusted-host=art-p-01.ons.statistics.gov.uk
WHATEVS3'''
                
                
                //sh 'pip3.6 install -r requirements.txt'
                sh "pip3.6 download -d vendor -r requirements.txt --no-binary :all:"
                dir('config') {
                    git url: "${GITLAB_URL}/StatBusReg/${env.SVC_NAME}.git", credentialsId: 'JenkinsSBR__gitlab'
                }
                stash name: 'Vendor'

            }
            post {
                success {
                    colourText("info","Stage: ${env.STAGE_NAME} successful!")
                }
                failure {
                    colourText("warn","Stage: ${env.STAGE_NAME} failed!")
                }
            }
        }


        stage('Deploy: Dev'){
            agent { label 'deploy.cf' }
            environment{
                CREDS = 's_jenkins_sbr_dev'
                SPACE = 'Dev'
            }
            steps {
                unstash name: 'Vendor'
                colourText("info", "Deploying ${env.BUILD_ID} on ${env.JENKINS_URL} from branch ${env.BRANCH_NAME} to ${env.SPACE}")
                script {
                    cfDeploy {
                        credentialsId = "${this.env.CREDS}"
                        org = "${this.env.ORG}"
                        space = "${this.env.SPACE}"
                        appName = "${this.env.SPACE.toLowerCase()}-${this.env.SVC_NAME}"
                        appPath = "./${distDir}/${this.env.SVC_NAME}.zip"
                        manifestPath  = "config/${this.env.SPACE.toLowerCase()}/manifest.yml"
                    }
                }
            }
            post {
                success {
                    colourText("info","Stage: ${env.STAGE_NAME} successful!")
                }
                failure {
                    colourText("warn","Stage: ${env.STAGE_NAME} failed!")
                }
            }
        }
    }

    post {
        success {
            colourText("success", "All stages complete. Build was successful.")
            slackSend(
                color: "good",
                message: "${env.JOB_NAME} success: ${env.RUN_DISPLAY_URL}"
            )
        }
        unstable {
            colourText("warn", "Something went wrong, build finished with result ${currentResult}. This may be caused by failed tests, code violation or in some cases unexpected interrupt.")
            slackSend(
                color: "warning",
                message: "${env.JOB_NAME} unstable: ${env.RUN_DISPLAY_URL}"
            )
        }
        failure {
            colourText("warn","Process failed at: ${env.NODE_STAGE}")
            slackSend(
                color: "danger",
                message: "${env.JOB_NAME} failed at ${env.STAGE_NAME}: ${env.RUN_DISPLAY_URL}"
            )
        }
    }
}

