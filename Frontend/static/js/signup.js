function sendOTP() {
    const email = document.getElementById("email").value;
    const firstname = document.getElementById("firstname").value;
    const lastname = document.getElementById("lastname").value;
    const password = document.getElementById("password").value;
   
      if (!email || !firstname || !lastname || !password) {
        alert(`Please fill the ${!email ? 'email' 
            : !firstname ? 'first name' 
            : !lastname ? 'last name' 
            : 'password'}
             .`);
        return;
    }


    console.log("Sending request...");

    fetch("http://127.0.0.1:5000/send-otp", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ 
            email: email,
            firstname: firstname,
            lastname: lastname,
            password: password
        })
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

async function data() {
    const email = document.getElementById("email").value;
    const firstname = document.getElementById("firstname").value;
    const lastname = document.getElementById("lastname").value;
    const password = document.getElementById("password").value;

    if (!email || !firstname || !lastname || !password) {
        alert("Please fill in all fields.");
        return;
    }
    
}