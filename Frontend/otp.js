 const otpBoxes = document.querySelectorAll('.otp-box');
    const verifyOtpBtn = document.getElementById('verifyOtpBtn');
    const resultBox = document.getElementById('result');

    const generatedOtp = '123456';

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

    verifyOtpBtn.addEventListener('click', () => {
      const enteredOtp = Array.from(otpBoxes).map(box => box.value).join('');
      
      if (enteredOtp.length !== 6) {
        showMessage('يرجى إدخال جميع الأرقام.', 'error');
        return;
      }

      if (enteredOtp === generatedOtp) {
        showMessage('تم التحقق بنجاح! ✓', 'success');
      } else {
        showMessage('رمز OTP غير صحيح. حاول مرة أخرى.', 'error');
      }
    });

    otpBoxes[0].focus();
 