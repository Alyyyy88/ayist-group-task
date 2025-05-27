document.addEventListener("DOMContentLoaded", function () {
  const statusDropdowns = document.querySelectorAll(".statusDropdown");
  const statusMenus = document.querySelectorAll(".statusMenu");

  document.addEventListener("click", function (event) {
    if (!event.target.closest(".statusDropdown")) {
      statusMenus.forEach((menu) => menu.classList.add("hidden"));
    }
  });

  statusDropdowns.forEach((dropdown) => {
    dropdown.addEventListener("click", function (event) {
      const menu = this.parentElement.querySelector(".statusMenu");
      statusMenus.forEach((m) => {
        if (m !== menu) m.classList.add("hidden");
      });
      menu.classList.toggle("hidden");
      event.stopPropagation();
    });
  });

  const statusOptions = document.querySelectorAll(".statusOption");
  statusOptions.forEach((option) => {
    option.addEventListener("click", function () {
      const projectId = this.getAttribute("data-project");
      const status = this.getAttribute("data-status");
      const dropdown = this.closest(".group").querySelector(
        ".statusDropdown span"
      );

      this.closest(".statusMenu").classList.add("hidden");

      dropdown.className =
        "inline-flex items-center px-4 py-2 rounded-md border";

      if (status === "In Progress") {
        dropdown.classList.add(
          "bg-blue-100",
          "text-blue-800",
          "border-blue-300"
        );
      } else if (status === "Completed") {
        dropdown.classList.add(
          "bg-green-100",
          "text-green-800",
          "border-green-300"
        );
      } else if (status === "On Hold") {
        dropdown.classList.add(
          "bg-yellow-100",
          "text-yellow-800",
          "border-yellow-300"
        );
      } else if (status === "Pending") {
        dropdown.classList.add(
          "bg-purple-100",
          "text-purple-800",
          "border-purple-300"
        );
      } else if (status === "Approved") {
        dropdown.classList.add(
          "bg-indigo-100",
          "text-indigo-800",
          "border-indigo-300"
        );
      } else if (status === "Rejected") {
        dropdown.classList.add("bg-red-100", "text-red-800", "border-red-300");
      } else {
        dropdown.classList.add(
          "bg-gray-100",
          "text-gray-800",
          "border-gray-300"
        );
      }

      dropdown.innerHTML =
        '<span class="mr-1">' +
        status +
        '</span><i class="fa-solid fa-chevron-down text-xs"></i>';
    });
  });
});
