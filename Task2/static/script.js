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
      form.addEventListener("submit",function(event){
        if(isChecked === false){
            event.preventDefault();
          window.alert("Please check the checkbox first");
        }
      });