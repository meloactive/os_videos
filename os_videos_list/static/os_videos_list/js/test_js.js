function getVersion() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById('demoGet').innerHTML = this.responseText;
        console.log(this.responseText)
      }
    };
    xhttp.open('GET', 'test_js', true);
    xhttp.send();
}

function postAdd() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById('demoPost').innerHTML = this.responseText;
      }
    };
    xhttp.open('POST', 'add', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("a=1&b=2");
}

// var tag = document.createElement("p");
//    var text = document.createTextNode("Tutorix is the best e-learning platform");
//    tag.appendChild(text);
//    var element = document.getElementById("new");
//    element.appendChild(tag);