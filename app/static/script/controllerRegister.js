
// function validateData(){
//     var inputController=document.getElementById("inputTest").value
// }

(function () {
    var arr=[]
    'use strict'
    var forms = document.querySelectorAll('.needs-validation')
    Array.prototype.slice.call(forms)
    .forEach(function (form) {
        arr.push(form)
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
            }
            form.classList.add('was-validated')
        }, false)
    })
    console.log(arr)
})()