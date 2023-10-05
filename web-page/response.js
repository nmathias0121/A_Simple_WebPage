let params = new URLSearchParams(location.search);
window.onload = function() {
    const name = params.get("preferredname");
    document.getElementById("thankname").innerText = name;
    document.getElementById("foodploy").innerText = params.get("food");
    
    const secret = params.get("secret");
    if (secret == "magic" || secret == "abracadabra") {
    const secretButton = document.createElement("button");
    secretButton.setAttribute("id", "secretButton");
    secretButton.textContent = "Take me to the secrets.";

    const secretURL = `secret_page.html?preferredname=${name}&secret=${secret}`;
    secretButton.onclick = function() {
        const duration = 500;
        setTimeout(function() { location.href=secretURL; }, duration);
    };

    const secretArea = document.getElementById("secrets");
    secretArea.appendChild(secretButton);
    }
}