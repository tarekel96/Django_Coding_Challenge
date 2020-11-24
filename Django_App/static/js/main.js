/* wait for the DOM to load before allowing any JS to work */
window.onload = () => {
        /* VARIABLES */
        const profileLink = document.querySelector("#profile-link");
        /* EVENT HANDLERS */
        profileLink.addEventListener("click", () => {
                profileLink.setAttribute("href", "/profile")
        })
}