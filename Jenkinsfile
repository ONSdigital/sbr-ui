#!/usr/bin/env groovy

// Global scope required for multi-stage persistence
def artServer = Artifactory.server 'art-p-01'
def buildInfo = Artifactory.newBuildInfo()
def distDir = 'build/dist/'
def agentPythonVersion = 'python_3.3.0'

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
                sh 'python --version'
                sh '/usr/local/bin/python3.3 --version'
                sh 'chmod 777 /usr/local/lib/python3.3/'
                sh '/usr/local/bin/python3.3 get-pip.py'
                sh 'pip --version'
                //sh $echo $PATH | tr ':' '\n'  | xargs -I %  sh -c "echo \"Checking %\";  ls -l % 2>/dev/null | grep -i 'py\|python\|pip'$
                sh 'echo $PATH'
                sh "echo $PATH | tr ':' '\n'  || true"
                sh "which python"
                sh 'python3 --version'
                //sh 'pip --version'
                //sh "python -m venv venv"
                //sh "source venv/bin/activate"
                //sh "source .envrc"
                sh "pip install -r requirements.txt"
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

        stage('Validate') {
            failFast true
            parallel {
                stage('Test: Unit'){
                    agent { label "build.${agentPythonVersion}" }
                    steps {
                        unstash name: 'Checkout'
                        sh 'ENVIRONMENT=TEST pytest --cov ./ --cov-report term-missing --cov-report xml --cov-config .coveragerc --junitxml=junit.xml --ignore=tests/selenium'
                    }
                    post {
                        // TODO: generate and publish test reports here
                        always {
                            junit '**/junit.xml'
                            cobertura autoUpdateHealth: false,
                                    autoUpdateStability: false,
                                    coberturaReportFile: '**/coverage.xml',
                                    conditionalCoverageTargets: '70, 0, 0',
                                    failUnhealthy: false,
                                    failUnstable: false,
                                    lineCoverageTargets: '80, 0, 0',
                                    maxNumberOfBuilds: 0,
                                    methodCoverageTargets: '80, 0, 0',
                                    onlyStable: false,
                                    zoomCoverageChart: false
                        }
                        success {
                            colourText("info","Stage: ${env.STAGE_NAME} successful!")
                        }
                        failure {
                            colourText("warn","Stage: ${env.STAGE_NAME} failed!")
                        }
                    }
                }
                stage('Style'){
                    agent { label "build.${agentPythonVersion}" }
                    steps {
                        unstash name: 'Checkout'
                        sh 'pylint $(find . -maxdepth 4 -name "*.py") --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"> pylint.log'
                    }
                    post {
                        always {
                            script {
                                step([$class                   : 'WarningsPublisher',
                                      consoleParsers           : [[parserName: 'PC-Lint', pattern: 'pylint.log']],
                                      defaultEncoding          : '',
                                      excludePattern           : '',
                                      healthy                  : '',
                                      includePattern           : '',
                                      messagesPattern          : '',
                                      unHealthy                : '',
                                      useStableBuildAsReference: true
                                ])
                            }
                        }
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
                    colourText("info","Stage: ${env.STAGE_NAME} successful!")
                }
                failure {
                    colourText("warn","Stage: ${env.STAGE_NAME} failed!")
                }
            }
        }

        /*stage('Test: Acceptance') {
            agent { label "build.${agentPythonVersion}" }
            steps {
                unstash name: 'Checkout'
                sh "pytest tests/selenium/"
            }
            post {
                success {
                    colourText("info","Stage: ${env.STAGE_NAME} successful!")
                }
                failure {
                    colourText("warn","Stage: ${env.STAGE_NAME} failed!")
                }
            }
        }*/

        stage ('Publish') {
            agent { label "build.${agentPythonVersion}" }
            when {
                branch "master"
                // evaluate the when condition before entering this stage's agent, if any
                beforeAgent true
            }
            steps {
                colourText("info", "Building ${env.BUILD_ID} on ${env.JENKINS_URL} from branch ${env.BRANCH_NAME}")
                unstash name: 'Checkout'
                sh "zip -r sbr-ui-${buildInfo.number}.zip ."
                script {
                    def uploadSpec = """{
                        "files": [
                            {
                                "pattern": "sbr-ui-${buildInfo.number}.zip",
                                "target": "registers-npm-snapshots/uk/gov/ons/${buildInfo.name}/sbr-ui-${buildInfo.number}.zip"
                            }
                        ]
                    }"""
                    artServer.upload spec: uploadSpec, buildInfo: buildInfo
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

        stage ('Vendor') {
            agent { label "build.${agentPythonVersion}" }
            when {
                branch "master"
                // evaluate the when condition before entering this stage's agent, if any
                beforeAgent true
            }
            steps {
                colourText("info", "Vendoring ${env.BUILD_ID} on ${env.JENKINS_URL} from branch ${env.BRANCH_NAME}")
                script {
                    def downloadSpec = """{
                        "files": [
                            {
                                "pattern": "registers-npm-snapshots/uk/gov/ons/${buildInfo.name}/sbr-ui-${buildInfo.number}.zip",
                                "target": "sbr-ui-${buildInfo.number}.zip",
                                "flat": "true"
                                "explode": "true"
                            }
                        ]
                    }"""
                    artServer.download spec: downloadSpec, buildInfo: buildInfo
                }
                sh "pip download -d vendor -r requirements.txt --no-binary :all:"
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
            when {
                branch "master"
                // evaluate the when condition before entering this stage's agent, if any
                beforeAgent true
            }
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

        stage('Deploy: Test'){
            agent { label 'deploy.cf' }
            when {
                branch "master"
                // evaluate the when condition before entering this stage's agent, if any
                beforeAgent true
            }
            environment{
                CREDS = 's_jenkins_sbr_test'
                SPACE = 'Test'
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
