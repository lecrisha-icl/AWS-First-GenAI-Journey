# First Cloud Journey Cloud Day - Generative AI Call Center

This guide provides step-by-step instructions to create a call center solution that integrates Amazon Bedrock as an AI assistant and uses OpenAI's Whisper model for real-time voice-to-text transcription. The implementation will utilize Amazon SageMaker to deploy Whisper and Amazon Bedrock to enhance the interaction with AI-driven responses.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Architecture Overview](#architecture-overview)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Create Whisper Endpoint](#step-1-create-whisper-endpoint)
  - [Step 2: Deploy Lambda Function](#step-2-deploy-lambda-function)
  - [Step 3: Set Up Amazon Connect Flow](#step-3-set-up-amazon-connect-flow)
- [Congratulations](#congratulations)

## Prerequisites

Before getting started, ensure you have the following:

- An AWS account with access to:
  - Amazon Connect 
  - Kinesis Video Stream
  - Bedrock
  - SQS
  - Lambda
  - SageMaker
  - DynamoDB

- Basic knowledge of Python, Jupyter Notebook, and familiarity with AWS services.

- [AWS CLI](https://aws.amazon.com/cli/) and [SageMaker Studio](https://aws.amazon.com/sagemaker/studio/) set up on your machine.

## Architecture Overview

![Architecture](https://github.com/vuongbachdoan/PRSV24-HACKATHON-GENAI/blob/main/call_center/call_system_architecture.png?raw=true)

## Setup Instructions

Before you go, clone this repository to your local machine:

```bash
git clone https://github.com/aws-samples/AWS-First-GenAI-Journey
cd AWS-GenAI-Contact-Center
```

### Step 1: Create Whisper Endpoint

#### About Whisper  
The Whisper endpoint is a powerful tool for speech recognition, offering extensive capabilities for transcription and understanding spoken language across various applications. It leverages advanced machine learning techniques to deliver accurate and efficient transcriptions.

#### How it Works

The Jupyter notebook deploys a SageMaker endpoint with a custom inference script similar to this [example in the SageMaker SDK documentation](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_inferenece_script_mode.html). The components required to deploy a pre-trained model to an endpoint in SageMaker are:
1. A serialized model artifact (tar file) in Amazon S3.
2. The code and requirements that run inference.

These components are packaged into a SageMaker endpoint, which serves the serialized model with custom code behind it as an API. See the architecture below for a visual description.

![Architecture](https://raw.githubusercontent.com/vuongbachdoan/AWS-First-GenAI-Journey/4597197b1a70e7e4129b11c7e0075ef9522c826b/AWS-GenAI-Contact-Center/whisper/imgs/endpoint-arch.svg)

#### Setup SageMaker Notebook

1. Navigate to the [SageMaker dashboard](https://us-west-2.console.aws.amazon.com/sagemaker).
2. Go to **Application and IDEs** > **Notebooks** in the left sidebar.
3. Click **Create notebook instance** and complete the following configurations:
   - For **Notebook instance name**, enter a unique name.
   - For **Notebook instance type**, choose **ml.m5.2xlarge**.
   - Expand **Additional configuration** and set the **Volume size** in GB to **10GB**.
   - Leave other fields as default.
4. Wait until the status of the notebook instance changes to **In service** before using the instance.
5. Open **JupyterLab** to run your notebook.

#### Run Notebook

1. Navigate to the `/whisper` folder in your local repository.
2. Copy all files and folders, upload them to the current notebook, and run the notebook.
3. It is recommended to run every cell **one by one**.
4. The folder structure will look like this:

![Folder Structure](https://github.com/vuongbachdoan/fcj-cd-demo/blob/main/whisper/imgs/notebook.png?raw=true)

> You will have an endpoint named **whisper-endpoint** under **Inference** > **Endpoints**.

### Step 2: Deploy Lambda Function

1. Navigate to `/amazon-connect` in your local repository.
    ```
    cd amazon-connect
    ```
2. Makesure AWS Profile already setup on local local machine:

    ```bash
    aws configure
    ```

   Then enter your AWS Access Key ID, AWS Secret Access Key, and set default region name to (**us-west-2**).

4. Create a `.env` file:

    ```bash
    cat << EOF > .env
    WHISPER_ENDPOINT="whisper-endpoint"
    EOF
    ```

5. Execute the following script once:

    ```bash
    ./scripts/create_deployment_bucket.sh dev
    ```

6. To deploy, execute this script as often as required:

    ```bash
    ./scripts/serverless_deploy.sh dev
    ```
After doing this, there are 3 Lambda functions, 3 DynamoDB tables, SQS will be created in your accounts.
### Step 3: Create Amazon Connect Instance

Follow this document to create Amazon Connect Instance
[https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html)

### Step 4: Add Lambda function to using with your Amazon Connect


Go to **Contact Flow** > Scroll down to **AWS Lambda** and add 3 previous Lambda functions

![Add Lambda function](https://docs.aws.amazon.com/images/connect/latest/adminguide/images/lambda-add-myfirstconnectlambda.png)


### Step 5: Enable KVS media streaming
Enable KVS media stream in your Amazon Connect instance and set a retention period for KVS (24 hours minimum during testing).

![KVS Enable](https://github.com/vuongbachdoan/fcj-cd-demo/blob/main/amazon-connect/doc/enable_kvs.png?raw=true)

### Step 6: Set Up Amazon Connect Flow

1. Access your Amazon Connect instance with the credentials you created before.
2. Create a flow using the template located at `amazon-connect/contact_flow/prsv-aws-connect-flow.json`.
3. Claim a phone number by navigating to **Phone numbers > Voice > Toll free > Choose the flow you imported previously**.
4. You're all set! Call your contact center now.

### DEMO

https://github.com/user-attachments/assets/dfa474e0-186e-428e-873c-f7f2c991da4d


## 🎉 Congratulations! 🎉

In this workshop, you have learned how to implement a call center using Amazon Connect and Generative AI. You’ve gained valuable insights into setting up efficient customer support systems that leverage cutting-edge technology to enhance user experience.

Feel free to ask me any questions about this solution! Connect with me on [LinkedIn](https://www.linkedin.com/in/vuongbd2007/).
