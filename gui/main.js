var editor = CodeMirror.fromTextArea(document.getElementById("writer"), {
    lineNumbers: true,
    mode: "python",
    theme: "dracula",
    indentUnit: 4
});

async function submitCode(path) {
    var text = encodeURI(editor.getValue())
    console.log(text)
    var url = "/" + path + "?code=" + text;
    data = await fetch(url)
    data = await data.json()
    if (path == "run"){
        elem = document.getElementById("output")
        console.log(elem)
        elem.innerText = data["result"]
    }
}

async function getCode() {
    console.log("getting code...")
    const response = await fetch("/getcode");
    const data = await response.json()
    console.log(data)
    if (data["status"] == "ok") {
        editor.setValue(data["code"]);
    }
}


getCode()

setInterval(() => {
    submitCode("save")
}, 1000);


