function update(ev) {
    const content = document.querySelector('div#content');
    content.innerHTML = ev.data;
}

function main() {
    const eventSource = new EventSource("/game/");
    eventSource.addEventListener('message',update);
}

window.addEventListener("load",main)
