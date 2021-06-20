function copyLink() {
    var textField = document.getElementById("copy");
    textField.select();
    textField.setSelectionRange(0, 99999);
    document.execCommand("copy");
}