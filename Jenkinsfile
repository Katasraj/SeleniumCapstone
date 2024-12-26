pipeline {
    agent any

    environment {
        BROWSER = "chrome"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo "Installing project dependencies..."
                bat 'pip install -r requirements.txt || exit 1'
            }
        }

        stage('Run Smoke and Regression Tests') {
            steps {
                echo "Running Smoke Tests..."
                bat '''
                    echo Creating report directories...
                    if not exist report mkdir report
                    if not exist report\\smoke mkdir report\\smoke
                    pytest -m smoke --browser=%BROWSER --alluredir=report/smoke || exit 0
                '''

                echo "Running Regression Tests..."
                bat '''
                    if not exist report mkdir report
                    if not exist report\\regression mkdir report\\regression
                    pytest -m regression --browser=%BROWSER --alluredir=report/regression || exit 0
                '''
            }
        }

        stage('Generate Combined Allure Results') {
            steps {
                echo "Generating Combined Allure Results..."
                bat '''
                    allure generate report/smoke report/regression --clean -o report/allure-results || exit 1
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
            echo "Publishing Allure Report..."

            // Publish Allure Report using Allure Jenkins Plugin
            allure includeProperties: false, jdk: '',
                   results: [[path: 'report/allure-results']]
        }
        failure {
            echo "Pipeline failed! Check the logs for details."
        }
        cleanup {
            echo "Cleaning up workspace..."
            deleteDir()
        }
    }
}
