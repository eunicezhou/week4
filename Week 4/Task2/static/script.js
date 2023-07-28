let form = document.querySelector("#agreementForm");
      let checkBox = document.querySelector("#agreement");
      let isChecked = false;
      checkBox.addEventListener("change", () => {
        if (isChecked === false) {
          isChecked = true;
        } else {
          isChecked = false;
        }
      });
      form.addEventListener("submit", () => {
        if (isChecked === false) {
          window.alert("Please check the checkbox first");
        }
      });