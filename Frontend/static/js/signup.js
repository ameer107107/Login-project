function sendOTP() {
    const email = document.getElementById("email").value;

    if (!email) {
        alert("Enter email");
        return;
    }

    console.log("Sending request...");

    fetch("http://127.0.0.1:5000/send-otp", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(res => res.json())
    .then(data => {
        console.log("Response data:", data);
        if (data.status === "success") {
            localStorage.setItem("email", email); 
            alert("تم إرسال رمز OTP. يرجى التحقق من بريدك الإلكتروني .");
            window.location.href = "/otp";
        } else {
            alert("حدث خطأ: " + data.message);
        }
    })
    .catch(err => {
        console.error("Fetch error:", err);
        alert("خطأ في الاتصال بالخادم");
    });
}