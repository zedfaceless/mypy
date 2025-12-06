// theme.js: handles dark mode toggle using localStorage
const btn = document.getElementById("themeToggle");
const root = document.documentElement;

function applyTheme(theme) {
    if (theme === "dark") {
        root.classList.remove("light");
        root.classList.add("dark");
        document.body.classList.add("bg-gray-900", "text-white");
    } else {
        root.classList.remove("dark");
        root.classList.add("light");
        document.body.classList.remove("bg-gray-900", "text-white");
    }
}

function loadTheme() {
    const theme = localStorage.getItem("theme") || "light";
    applyTheme(theme);
}

function toggleTheme() {
    const current = localStorage.getItem("theme") || "light";
    const next = current === "light" ? "dark" : "light";
    localStorage.setItem("theme", next);
    applyTheme(next);
}

if (btn) {
    btn.addEventListener("click", toggleTheme);
}

document.addEventListener("DOMContentLoaded", loadTheme);
