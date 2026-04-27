

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Utils.otp import generate_otp, send_otp_email
from models.user import User
app = Flask(__name__, template_folder='../Frontend/templates',
                static_folder='../Frontend/static')
CORS(app)

otps = {}
pending_users = {}

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



@app.route("/login-api", methods=["POST"])
def login_api():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"status": "error", "message": "Email and password are required"}), 400
        
    if User.verify_credentials(email, password):
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        return jsonify({"status": "error", "message": "الإيميل أو كلمة المرور غير صحيحة"}), 401



@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json()
    email = data.get("email")
   
    if not email:
        return jsonify({"status": "error", "message": "Email is required"}), 400
        
    if User.email_exists(email):
        return jsonify({"status": "error", "message": "هذا الإيميل مسجل مسبقاً"}), 400
        
    otp_code = generate_otp()
    otps[email] = otp_code
    pending_users[email] = data 
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
        user_data = pending_users.get(email)
        print(user_data)
        if not user_data:
            return jsonify({"status": "error", "message": "User data not found"}), 400

        user = User(
                user_data["firstname"],
                user_data["lastname"],
                user_data["email"],
                user_data["password"]
            )
        user.add_to_list()
        
        print("المستخدمون في القائمة حالياً:", len(User.users_list))

        del pending_users[email]
        del otps[email]
        return jsonify({"status": "success", "message":  "   ...تم التحقق من الايميل  وتم انشاء الحساب بنجاح"}), 200
            
    else:
        return jsonify({"status": "error", "message": "رمز OTP غير صحيح"}), 400





if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)