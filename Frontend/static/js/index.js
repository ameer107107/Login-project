function loginUser() {
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    if (!email || !password) {
        alert("Please enter both email and password.");
        return;
    }

    fetch("http://127.0.0.1:5000/login-api", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "success") {
            window.location.href = "/welcome";
        } else {
            alert(data.message);
        }
    })
    .catch(err => {
        console.error("Fetch error:", err);
        alert("خطأ في الاتصال بالخادم");
    });
}