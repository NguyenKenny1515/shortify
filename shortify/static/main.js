function copyLink() {
    var textField = document.getElementById("copyLink");
    textField.select();
    textField.setSelectionRange(0, 99999);
    document.execCommand("copy");
    var button = document.getElementById("copyButton");
    button.innerHTML = "Copied";
}