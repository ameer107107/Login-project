from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Utils.otp import generate_otp, send_otp_email

app = Flask(__name__, template_folder='../Frontend/templates',
                static_folder='../Frontend/static')
CORS(app)

otps = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/otp")
def otp():
    return render_template("otp.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json()
    email = data.get("email")
    
    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400
        
    otp_code = generate_otp()
    otps[email] = otp_code
    
    success = send_otp_email(email, otp_code)
    
    if success:
        return jsonify({"status": "success", "message": "تم إرسال OTP بنجاح"}), 200
    else:
        return jsonify({"status": "error", "message": "حدث خطأ أثناء إرسال الإيميل"}), 500

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.get_json()
    email = data.get("email")
    user_otp = data.get("otp")
    
    if not email or not user_otp:
        return jsonify({"status": "error", "message": "Email and OTP are required"}), 400
        
    if email in otps and otps[email] == str(user_otp):
        del otps[email] 
        return jsonify({"status": "success", "message": "تم التحقق من الـ OTP بنجاح"}), 200
        
    else:
        return jsonify({"status": "error", "message": "رمز OTP غير صحيح"}), 400

if __name__ == "__main__":
    app.run(debug=True)