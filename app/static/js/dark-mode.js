function toggleDarkMode() {
  const isDarkMode = document.documentElement.classList.contains("dark");

  const darkModeToggle = document.getElementById("darkModeToggle");

  if (isDarkMode) {
    document.documentElement.classList.remove("dark");
    if (darkModeToggle) {
      darkModeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
    }
    localStorage.setItem("darkMode", "light");
  } else {
    document.documentElement.classList.add("dark");
    if (darkModeToggle) {
      darkModeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
    }
    localStorage.setItem("darkMode", "dark");
  }

  document.body.style.transition = "background-color 0.3s ease";

  fetch(
    "/set_theme/" +
      (document.documentElement.classList.contains("dark") ? "dark" : "light"),
    {
      method: "GET",
      headers: {
        Accept: "application/json",
      },
    }
  )
    .then((response) => {
    })
    .catch((error) => {
      console.error("Error saving theme preference:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const darkModeToggle = document.getElementById("darkModeToggle");
  if (darkModeToggle) {
    const isDarkMode = document.documentElement.classList.contains("dark");
    darkModeToggle.innerHTML = isDarkMode
      ? '<i class="fa-solid fa-sun"></i>'
      : '<i class="fa-solid fa-moon"></i>';
  }

  if (
    window.updateChartColors &&
    typeof window.updateChartColors === "function"
  ) {
    window.updateChartColors();
  }
});

window.toggleDarkMode = toggleDarkMode;
