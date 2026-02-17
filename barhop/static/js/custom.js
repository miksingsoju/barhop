// load dark mode colours on startup
document.addEventListener("DOMContentLoaded", () => {
    localStorage.setItem("data-bs-theme", "dark");
});

// nav bar interaction
document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.getElementsByClassName("nav-link");
    const linkHover = document.querySelector("span.nav-hover-pill");
    const activeLink = document.querySelector("a.nav-link.active");

    const hideBorder = () => {
        switch (window.location.pathname.split("/")[1]) {
            case "accounts":
            case "profile":
            // case "":
                linkHover.style.opacity = "0";
                linkHover.style.width = "0";
                linkHover.style.border = "none";
                break;
            default:
                linkHover.style.opacity = "100%";
                linkHover.style.border = "solid 1px";
                linkHover.style.width = activeLink ? `${activeLink.clientWidth}px` : "0";
                linkHover.style.transform = activeLink ? `translateX(${activeLink.offsetLeft}px)` : "translate(0px)";
                break;
        }
    }

    hideBorder();

    for (let el of navLinks) {
        el.addEventListener("mouseover", () => {
            if (activeLink && !el.classList.contains("active")) {
                activeLink.firstElementChild.style.color = "var(--bs-gray-800)";
                activeLink.style.color = "#fff";
            }
            linkHover.style.opacity = "100%";
            linkHover.style.border = "solid 1px";
            linkHover.style.width = `${el.clientWidth}px`;
            linkHover.style.transform = `translateX(${el.offsetLeft}px)`;
        });
        el.addEventListener("mouseleave", () => {
            activeLink && (activeLink.firstElementChild.style = "");
            activeLink && (activeLink.style = "");
            hideBorder();
        });
    }
});