
const greetingElement = document.getElementById('greeting');

greetingElement.style.color = 'blue';
greetingElement.style.fontFamily = 'Arial, sans-serif';


async function fetchData() {
    const response = await fetch('http://localhost:8000');
    const data = await response.json();
    greetingElement.textContent = data.message;
}

fetchData();