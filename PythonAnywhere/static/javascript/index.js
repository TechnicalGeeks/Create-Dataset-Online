function alert_to_quit() {
    alert("Press q To CLOSE Image Capturing ")

}

function required(inputtx) {
    if (inputtx.value.length == 0) {
        alert("message");
        return false;
    }
    return true;
}

function validateForm() {
    var x = document.forms["form"]["lname"].value;
    var y = document.forms["form"]["roll"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
    if (y == "") {
        alert("Roll no must be filled out");
        return false;
    }
}