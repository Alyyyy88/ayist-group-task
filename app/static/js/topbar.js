  function toggleDropdown(menuId) {
    const menu = document.getElementById(menuId);
    menu.classList.toggle("hidden");
  }

  function changeLanguage(langCode) {
    window.location.href = "/set_language/" + langCode;
  }

  function toggleMobileMenu() {
    const mobileSidebar = document.getElementById("mobileSidebar");
    mobileSidebar.classList.toggle("hidden");

    document.body.classList.toggle("overflow-hidden");
  }

  document.addEventListener("click", function (e) {
    const langButton = document.getElementById("dropdownButton");
    const langMenu = document.getElementById("dropdownMenu");
    if (
      langButton &&
      langMenu &&
      !langButton.contains(e.target) &&
      !langMenu.contains(e.target)
    ) {
      langMenu.classList.add("hidden");
    }

    const userButton = document.getElementById("userDropdownButton");
    const userMenu = document.getElementById("userDropdownMenu");
    if (
      userButton &&
      userMenu &&
      !userButton.contains(e.target) &&
      !userMenu.contains(e.target)
    ) {
      userMenu.classList.add("hidden");
    }
  });
