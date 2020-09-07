function submitAction() {
    // 选择机器人
    var select = document.getElementById('robot_value');
    var index = select.selectedIndex;
    var robotKey = select.options[index].value;
    
    // 输入内容
    var textArea = document.getElementById('content-textArea');
    var content = textArea.value;
    
    var atAllCheckbox = document.getElementById('at_all');
    var isAtAll = atAllCheckbox.checked;

    if (content === undefined || content.length === 0) {
        alert('请输入内容');
        return;
    }

    var body = {'key': robotKey, 'content': content, 'atAll': isAtAll};
    var request = new XMLHttpRequest();
    request.open("POST", "/execute");
    console.log(request);
    request.setRequestHeader("Content-type", "application/json");
    request.send(JSON.stringify(body));
    request.onreadystatechange = () => {
        if (request.status == 200 && request.readyState == 4) {
            var response = JSON.parse(request.response);
            if (response.status === 'error') {
                console.log(response.msg);
                alert(response.msg);
                return;
            } 
            textArea.value = '';
            notification(true, response.msg);
        }
    };
};

function notification(isSuccess, content) {
    var clazz = isSuccess === true ? ' is-success' : ' is-danger'
    var element = document.getElementById('alert-content');
    
    var elementClazz = element.getAttribute('class');
    elementClazz = elementClazz.replace('is-success', '');
    elementClazz = elementClazz.replace('is-danger', '');
    elementClazz = elementClazz.concat(clazz);
    element.setAttribute('class', elementClazz);
    element.innerText = content;
    console.log(element);
    element.style.display = 'block';
    setTimeout(() => {
        element.style.display = 'none';
    }, 2000);
}