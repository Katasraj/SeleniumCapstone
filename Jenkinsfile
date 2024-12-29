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

        stage('Run Smoke Tests') {
            steps {
                echo "Running Smoke Tests..."
                bat 'pytest -vv -s tests/login_tests.py --alluredir=Reports/allure-smoke-results'

                // Archive the Smoke Allure results into a tar.gz file
                bat 'tar -czvf allure-smoke-report.tar.gz -C Reports allure-smoke-results'
            }
        }

        stage('Run Regression Tests') {
            steps {
                echo "Running Regression Tests..."
                bat 'pytest -m regression --order-scope=session --alluredir=Reports/allure-regression-results'

                // Archive the Regression Allure results into a tar.gz file
                bat 'tar -czvf allure-regression-report.tar.gz -C Reports allure-regression-results'
            }
        }

        stage('Generate Allure Report for Smoke Tests') {
            steps {
                echo "Generating Allure Report for Smoke Tests..."
                allure includeProperties: false, jdk: '', results: [[path: 'Reports/allure-smoke-results']]
            }
        }

        stage('Generate Allure Report for Regression Tests') {
            steps {
                echo "Generating Allure Report for Regression Tests..."
                allure includeProperties: false, jdk: '', results: [[path: 'Reports/allure-regression-results']]
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"

            // List files to confirm the tar.gz files exist
            bat 'dir'

            // Send email with both Smoke and Regression Allure report archives attached
            emailext attachLog: true,
                     attachmentsPattern: 'allure-smoke-report.tar.gz,allure-regression-report.tar.gz',
                     body: """
The Jenkins pipeline has completed successfully.
Please find the following Allure reports attached:
- Smoke Tests Report
- Regression Tests Report
""",
                     subject: "Jenkins Pipeline - Success",
                     to: "naga45@gmail.com"
        }
        failure {
            echo "Pipeline failed! Check the logs for details."
            // Send email on failure without attachments
            emailext attachLog: true,
                     body: "The Jenkins pipeline has failed. Please check the logs for details.",
                     subject: "Jenkins Pipeline - Failure",
                     to: "naga45@gmail.com"
        }
        cleanup {
            echo "Cleaning up workspace after email is sent..."
            deleteDir()  // Cleanup now happens last
        }
    }
}
