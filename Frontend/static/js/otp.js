 const otpBoxes = document.querySelectorAll('.otp-box');
    const verifyOtpBtn = document.getElementById('verifyOtpBtn');
    const resultBox = document.getElementById('result');

    function showMessage(text, type) {
      resultBox.textContent = text;
      resultBox.className = `message ${type}`;
      resultBox.classList.remove('hidden');
    }

    otpBoxes.forEach((box, index) => {
      box.addEventListener('input', (e) => {
        if (e.target.value && index < otpBoxes.length - 1) {
          otpBoxes[index + 1].focus();
        }
      });

      box.addEventListener('keydown', (e) => {
        if (e.key === 'Backspace' && !e.target.value && index > 0) {
          otpBoxes[index - 1].focus();
        }
      });
    });

    verifyOtpBtn.addEventListener('click', async () => {
      const enteredOtp = Array.from(otpBoxes).map(box => box.value).join('');
      
      if (enteredOtp.length !== 6) {
        showMessage('يرجى إدخال جميع الأرقام.', 'error');
        return;
      }

     
      const email = localStorage.getItem('email');
      if (!email) {
        showMessage('الإيميل غير متوفر.', 'error');
        return;
      }

      try {
        const res = await fetch("http://127.0.0.1:5000/verify-otp", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({ email, otp: enteredOtp })
        });

        const data = await res.json();
        if (data.status === 'success') {
          showMessage('تم التحقق بنجاح! ✓', 'success');
          setTimeout(() => {
              window.location.href = "/welcome";
          }, 2000);
        } else {
          showMessage('رمز OTP غير صحيح. حاول مرة أخرى.', 'error');
        }
      } catch (error) {
        showMessage('خطأ في الاتصال بالخادم.', 'error');
      }
    });

    otpBoxes[0].focus();