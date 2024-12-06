Project Overview

The Online Banking System is a web application designed to provide users with a secure and seamless banking experience. This system leverages Firebase Cloud services for real-time data management, user authentication, and storage. Users can log in, view their account details, perform transactions, and receive updates instantly, all while ensuring their data's security and reliability.

Setup and Installation

Prerequisites:

Node.js installed on your system.

Firebase CLI installed.

A Firebase project set up in your Firebase console.

Steps:

Clone the repository:

git clone https://github.com/your-repo/online-banking-system.git

Navigate to the project directory:

cd online-banking-system

Install Firebase CLI (if not already installed):

npm install -g firebase-tools

Log in to Firebase:

firebase login

Initialize Firebase in the project:

firebase init

Select Hosting and Realtime Database.

Configure the project using your Firebase project settings.

Deploy the application:

firebase deploy
Firebase Configuration

Ensure you update the Firebase configuration in your firebaseConfig object within the JavaScript files:

const firebaseConfig = {
  apiKey: "<YOUR_API_KEY>",
  authDomain: "<YOUR_PROJECT_ID>.firebaseapp.com",
  databaseURL: "https://<YOUR_PROJECT_ID>.firebaseio.com",
  projectId: "<YOUR_PROJECT_ID>",
  storageBucket: "<YOUR_PROJECT_ID>.appspot.com",
  messagingSenderId: "<YOUR_SENDER_ID>",
  appId: "<YOUR_APP_ID>"
};

Folder Structure

online-banking-system/
|— index.html      # Login page
|— details.html    # Customer details page
|— styles.css      # CSS styles for the project
|— app.js          # Main JavaScript for Firebase integration
|— firebase.json   # Firebase Hosting configuration

Future Enhancements

Add transaction history functionality.

Implement push notifications for account updates using Firebase Cloud Messaging.

Enable mobile banking support with a responsive design.

Add multi-factor authentication for enhanced security.

License

This project is licensed under the MIT License. See the LICENSE file for details.

