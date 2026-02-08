function submitCode(path) {
    var code = document.getElementById("writer");
    code.innerText
    var text = encodeURI(code.innerText)
    console.log(text)
    var url = "/" + path + "?code=" + text;
    data = fetch(url)
}

async function getCode() {
    const response = await fetch("/getcode");
    const data = await response.json()
    console.log(data)
    if (data["status"] == "ok") {
        var code = document.getElementById("writer");
        code.innerText = data["code"]
        return
    }
}

getCode()

setInterval(() => {
    submitCode("save")
}, 1000);