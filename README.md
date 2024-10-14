# RailBot

## Description
RailBot is a chatbot to explore Google DialogFlow's capability to design and implement Low-code conversational Interface. I have tried to Leverage DialogFlow’s NLP & ML capabilities to process human language and extract the intent to service dynamic responses. 
The Bot answers queries on IRCTC and provides real time seat availability on trains directly using freely available Indian railways APIs. The fullfillment logic is placed in a google cloud function which processes user requests, then requests the railways API for data, receives & processes the respective response and finally sends responses back to Dialogflow.

## Demo
https://bot.dialogflow.com/b6fc6734-029d-44e7-b3c3-597a522784d1

## Installation
To set up the RailBot project, follow these steps:

### Prerequisites
1. **Google Cloud Account**: You need a Google Cloud account. If you don't have one, sign up [here](https://cloud.google.com/).
2. **Dialogflow Account**: Create a Dialogflow account at [Dialogflow Console](https://dialogflow.cloud.google.com/).


### Steps to Set Up the Project

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/rail-bot.git
   cd rail-bot

2. **Set Up Dialogflow**:
  * Go to the Dialogflow Console.
  * Create a new agent or use an existing one.
  * Import  Dialogflow intents and entities from the intents directory in this repository. You can do this by clicking on
    the gear icon next to your agent's name, selecting Export and Import, and then Import from Zip.

3. **Service Account for Authentication**:
  * In the Google Cloud Console, create a service account:
    * Go to IAM & Admin > Service Accounts.
    * Click Create Service Account.
    * Assign roles like Dialogflow API Client.
  * Download the service account key in JSON format and save it as service-account.json in your project directory.

4. **Fulfillment Logic Deployment**
   * The fulfillment logic is stored in the `fulfillment/` directory. The code is written in Python and runs on
     Google Cloud Function.
   * Go to Google Cloud Console: Visit Google Cloud Console, select your project, or create a new one.
   * Enable Cloud Functions API: Navigate to APIs & Services > Library, search for Cloud Functions API, and click Enable.
   * Create a Cloud Function: Go to Cloud Functions, click Create Function, and configure:
     *  Function Name: Choose a name (e.g., dialogflow-fulfillment).
     *  Runtime: Select the appropriate runtime (Python).
     *  Trigger: Select HTTP Trigger and allow unauthenticated access
   * Upload Fulfillment Code:
     * Choose Inline Editor and paste the code from the fulfillment/ directory of this repository.
     * Create your own API key from https://rapidapi.com/ and update the api key value in code. 
   * Set Entry Point: Set the Entry Point to the function’s main handler "train_schedule_webhook" in this case.
   * Deploy: Click Deploy and wait for the process to complete. Copy the provided function URL
   * Connect to Dialogflow: In the Dialogflow Console, enable the Webhook under Fulfillment and paste the Cloud Function URL.
     
