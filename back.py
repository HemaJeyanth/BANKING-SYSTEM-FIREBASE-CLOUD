import firebase_admin
from firebase_admin import credentials, auth, firestore
from flask import Flask, jsonify, request

# Initialize Firebase
cred = credentials.Certificate(r"D:\cloud bank\serviceAccountKey.json")  
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# User authentication (Login, Register)
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']
    user_name = data['user_name']
    account_name = data['account_name']

    # Firebase Authentication for user creation
    try:
        user = auth.create_user(email=email, password=password)
        db.collection('users').document(user.uid).set({
            'user_name': user_name,
            'account_name': account_name,
            'email': email,
            'balance': 0  # Initial balance
        })
        return jsonify({"status": "success", "message": "User registered successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    # Firebase Authentication
    try:
        user = auth.get_user_by_email(email)
        return jsonify({"status": "success", "user_id": user.uid})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Details Page (User info)
@app.route('/details/<user_id>', methods=['GET'])
def get_user_details(user_id):
    try:
        user_doc = db.collection('users').document(user_id).get()
        if user_doc.exists:
            return jsonify({"status": "success", "data": user_doc.to_dict()})
        else:
            return jsonify({"status": "error", "message": "User not found"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Balance Page (Check balance)
@app.route('/balance/<user_id>', methods=['GET'])
def get_balance(user_id):
    try:
        user_doc = db.collection('users').document(user_id).get()
        if user_doc.exists:
            balance = user_doc.to_dict().get('balance', 0)
            return jsonify({"status": "success", "balance": balance})
        else:
            return jsonify({"status": "error", "message": "User not found"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Transaction Page (Deposit/Withdraw)
@app.route('/transaction/<user_id>', methods=['POST'])
def make_transaction(user_id):
    data = request.json
    amount = data['amount']
    transaction_type = data['transaction_type']  # 'deposit' or 'withdraw'
    card_type = data['card_type']
    timestamp = firestore.SERVER_TIMESTAMP

    # Fetch user document
    user_doc = db.collection('users').document(user_id)
    user_balance = user_doc.get().to_dict().get('balance', 0)

    if transaction_type == 'withdraw' and user_balance < amount:
        return jsonify({"status": "error", "message": "Insufficient funds"})

    # Record transaction in Firestore
    db.collection('transactions').add({
        'user_id': user_id,
        'amount': amount,
        'card_type': card_type,
        'transaction_type': transaction_type,
        'timestamp': timestamp
    })

    # Update user balance (credit or debit)
    new_balance = user_balance + amount if transaction_type == 'deposit' else user_balance - amount
    user_doc.update({'balance': new_balance})

    return jsonify({"status": "success", "message": "Transaction successful", "new_balance": new_balance})

# View Transaction History
@app.route('/transaction-history/<user_id>', methods=['GET'])
def transaction_history(user_id):
    try:
        transactions = []
        # Fetch all transactions for the user
        transaction_docs = db.collection('transactions').where('user_id', '==', user_id).order_by('timestamp').get()
        for doc in transaction_docs:
            transactions.append(doc.to_dict())

        return jsonify({"status": "success", "transactions": transactions})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Cards Page
@app.route('/cards/<user_id>', methods=['GET'])
def get_card_details(user_id):
    try:
        card_docs = db.collection('users').document(user_id).collection('cards').get()
        cards = [doc.to_dict() for doc in card_docs]
        return jsonify({"status": "success", "data": cards})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Loans Page
@app.route('/loans/<user_id>', methods=['GET'])
def get_loan_details(user_id):
    try:
        loan_docs = db.collection('users').document(user_id).collection('loans').get()
        loans = [doc.to_dict() for doc in loan_docs]
        return jsonify({"status": "success", "data": loans})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Insurance Page
@app.route('/insurance/<user_id>', methods=['GET'])
def get_insurance_details(user_id):
    try:
        insurance_docs = db.collection('users').document(user_id).collection('insurance').get()
        insurance = [doc.to_dict() for doc in insurance_docs]
        return jsonify({"status": "success", "data": insurance})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Forex Page
@app.route('/forex/<user_id>', methods=['GET'])
def get_forex_details(user_id):
    try:
        forex_docs = db.collection('users').document(user_id).collection('forex').get()
        forex = [doc.to_dict() for doc in forex_docs]
        return jsonify({"status": "success", "data": forex})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Digital Rupee Page
@app.route('/digital-rupee/<user_id>', methods=['GET'])
def get_digital_rupee_details(user_id):
    try:
        digital_rupee_docs = db.collection('users').document(user_id).collection('digital_rupee').get()
        digital_rupee = [doc.to_dict() for doc in digital_rupee_docs]
        return jsonify({"status": "success", "data": digital_rupee})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Fast Tag Page
@app.route('/fastag/<user_id>', methods=['GET'])
def get_fastag_details(user_id):
    try:
        fastag_docs = db.collection('users').document(user_id).collection('fastag').get()
        fastag = [doc.to_dict() for doc in fastag_docs]
        return jsonify({"status": "success", "data": fastag})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
