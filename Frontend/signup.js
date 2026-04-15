async function handleSignup(event) {
  event.preventDefault();

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if (password !== confirmPassword) {
    alert('كلمات المرور غير متطابقة');
    return;
  }

  try {
    const response = await fetch('http://localhost:5000/api/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    });

    const data = await response.json();

    if (response.ok) {
      alert('تم التسجيل بنجاح!');
      window.location.href = 'login.html';
    } else {
      alert('خطأ: ' + data.message);
    }
  } catch (error) {
    console.error('خطأ:', error);
    alert('فشل الاتصال بالخادم');
  }
}

document.getElementById('signupForm').addEventListener('submit', handleSignup);