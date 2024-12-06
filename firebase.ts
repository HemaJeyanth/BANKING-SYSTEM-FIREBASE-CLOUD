// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD9ywQKBysV05PTEo6ugISQkcfD8Nbx4N0",
  authDomain: "banking-with-cloud.firebaseapp.com",
  projectId: "banking-with-cloud",
  storageBucket: "banking-with-cloud.appspot.com",
  messagingSenderId: "638684226654",
  appId: "1:638684226654:web:2f0bed7cec3ebd99a5c0cf",
  measurementId: "G-1RT8QKPF7L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const firestore = getFirestore(app);

export { app, analytics, auth, firestore };
