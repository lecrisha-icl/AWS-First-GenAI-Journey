# Amazon Connect Real Time Transcription using Whisper in the IVR

## Installation

Customise env/dev.sh with your target region, account number and whisper end point. Pay attention to the AWS Profile name, if deploying and testing from the command line.

Change the stage and rename to env/<stage>.sh to deploy to a new stage environment.

Execute this script once:

    ./scripts/create_deployment_bucket.sh <stage>

To deploy execute this script as often as required:

    ./scripts/serverless_deploy.sh <stage>

