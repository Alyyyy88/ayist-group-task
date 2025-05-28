document.addEventListener("DOMContentLoaded", function () {
  // Enable form change detection
  const forms = document.querySelectorAll("form");
  const saveChangesBtn = document.getElementById("saveChangesBtn");

  forms.forEach((form) => {
    const initialFormData = new FormData(form);
    const initialValues = {};

    for (const [key, value] of initialFormData.entries()) {
      initialValues[key] = value;
    }

    const inputs = form.querySelectorAll("input, select, textarea");
    inputs.forEach((input) => {
      input.addEventListener("change", () => {
        const currentFormData = new FormData(form);
        let hasChanges = false;

        for (const [key, value] of currentFormData.entries()) {
          if (value !== initialValues[key]) {
            hasChanges = true;
            break;
          }
        }

        if (hasChanges) {
          saveChangesBtn.removeAttribute("disabled");
          saveChangesBtn.classList.remove("opacity-50", "cursor-not-allowed");
        } else {
          saveChangesBtn.setAttribute("disabled", "disabled");
          saveChangesBtn.classList.add("opacity-50", "cursor-not-allowed");
        }
      });
    });
  });

  // Password visibility toggle
  const togglePasswordButtons = document.querySelectorAll(".toggle-password");
  togglePasswordButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const input = this.closest("div").querySelector("input");
      const icon = this.querySelector("i");

      if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
      } else {
        input.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
      }
    });
  });

  // Form submission
  const companyProfileForm = document.getElementById("companyProfileForm");
  const changePasswordForm = document.getElementById("changePasswordForm");
  const successNotification = document.getElementById("successNotification");
  const closeNotification = document.getElementById("closeNotification");
  const notificationTitle = document.getElementById("notificationTitle");
  const notificationMessage = document.getElementById("notificationMessage");

  saveChangesBtn.addEventListener("click", function (e) {
    e.preventDefault();

    setTimeout(() => {
      notificationTitle.textContent = "{{ _('Success!') }}";
      notificationMessage.textContent =
        "{{ _('Company profile updated successfully.') }}";
      successNotification.classList.remove("hidden");
      successNotification.classList.add("flex");

      setTimeout(() => {
        successNotification.classList.add("hidden");
        successNotification.classList.remove("flex");
      }, 5000);

      saveChangesBtn.setAttribute("disabled", "disabled");
      saveChangesBtn.classList.add("opacity-50", "cursor-not-allowed");
    }, 1000);
  });

  changePasswordForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const currentPassword = document.getElementById("currentPassword").value;
    const newPassword = document.getElementById("newPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Simple validation
    if (!currentPassword || !newPassword || !confirmPassword) {
      alert("{{ _('All password fields are required.') }}");
      return;
    }

    if (newPassword !== confirmPassword) {
      alert("{{ _('New passwords do not match.') }}");
      return;
    }

    setTimeout(() => {
      notificationTitle.textContent = "{{ _('Password Updated!') }}";
      notificationMessage.textContent =
        "{{ _('Your password has been changed successfully.') }}";
      successNotification.classList.remove("hidden");
      successNotification.classList.add("flex");

      document.getElementById("currentPassword").value = "";
      document.getElementById("newPassword").value = "";
      document.getElementById("confirmPassword").value = "";

      setTimeout(() => {
        successNotification.classList.add("hidden");
        successNotification.classList.remove("flex");
      }, 5000);
    }, 1000);
  });

  // Close notification
  closeNotification.addEventListener("click", function () {
    successNotification.classList.add("hidden");
    successNotification.classList.remove("flex");
  });
});
