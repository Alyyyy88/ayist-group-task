
  document.addEventListener("DOMContentLoaded", function () {
    // Status dropdown functionality
    const statusDropdowns = document.querySelectorAll(".statusDropdown");
    const statusMenus = document.querySelectorAll(".statusMenu");

    // Close all dropdowns when clicking outside
    document.addEventListener("click", function (event) {
      if (!event.target.closest(".statusDropdown")) {
        statusMenus.forEach((menu) => menu.classList.add("hidden"));
      }
    });

    // Toggle dropdown on click
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

    // Handle status option selection
    const statusOptions = document.querySelectorAll(".statusOption");
    statusOptions.forEach((option) => {
      option.addEventListener("click", function () {
        const projectId = this.getAttribute("data-project");
        const status = this.getAttribute("data-status");
        const dropdown = this.closest(".group").querySelector(
          ".statusDropdown span"
        );

        // Hide dropdown
        this.closest(".statusMenu").classList.add("hidden");

        // Update status visually
        dropdown.className =
          "text-xs px-2.5 py-1 rounded-full inline-flex items-center gap-1";

        // Add appropriate color class based on status
        if (status === "In Progress") {
          dropdown.classList.add("bg-blue-100", "text-blue-800");
        } else if (status === "Completed") {
          dropdown.classList.add("bg-green-100", "text-green-800");
        } else if (status === "On Hold") {
          dropdown.classList.add("bg-yellow-100", "text-yellow-800");
        } else if (status === "Pending") {
          dropdown.classList.add("bg-purple-100", "text-purple-800");
        } else if (status === "Approved") {
          dropdown.classList.add("bg-indigo-100", "text-indigo-800");
        } else if (status === "Rejected") {
          dropdown.classList.add("bg-red-100", "text-red-800");
        } else {
          dropdown.classList.add("bg-gray-100", "text-gray-800");
        }

        dropdown.innerHTML =
          status + ' <i class="fa-solid fa-chevron-down ml-1 text-xs"></i>';
          
        // Update the project card's data-status attribute for filtering
        const projectCard = this.closest(".project-card");
        if (projectCard) {
          projectCard.setAttribute("data-status", status);
        }
          
        // Show notification
        showNotification("Status Updated", "Project status has been updated successfully");
      });
    });

    // Filter projects by status
    const filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach(button => {
      button.addEventListener("click", function() {
        const status = this.getAttribute("data-status");
        
        // Update active button styling
        filterButtons.forEach(btn => {
          btn.classList.remove("bg-indigo-100", "text-indigo-800");
          btn.classList.add("bg-gray-100", "text-gray-800");
        });
        this.classList.remove("bg-gray-100", "text-gray-800");
        this.classList.add("bg-indigo-100", "text-indigo-800");
        
        // Filter projects
        const projects = document.querySelectorAll("#projectsGrid > div");
        projects.forEach(project => {
          const projectStatus = project.querySelector(".statusDropdown span").textContent.trim().replace(/\s+/g, ' ').split(' ')[0];
          
          if (status === "all" || projectStatus === status) {
            project.style.display = "";
          } else {
            project.style.display = "none";
          }
        });
      });
    });
    
    // Project search functionality
    const searchInput = document.getElementById("searchProjects");
    searchInput.addEventListener("input", function () {
      const searchTerm = this.value.toLowerCase();
      const projects = document.querySelectorAll("#projectsGrid > div");

      projects.forEach((project) => {
        const projectName = project
          .querySelector("h3")
          .textContent.toLowerCase();
        const projectDesc = project
          .querySelector("p")
          .textContent.toLowerCase();

        if (
          projectName.includes(searchTerm) ||
          projectDesc.includes(searchTerm)
        ) {
          project.style.display = "";
        } else {
          project.style.display = "none";
        }
      });
    });
    
    function showNotification(title, message) {
      const notification = document.getElementById("statusNotification");
      const notificationTitle = document.getElementById("notificationTitle");
      const notificationMessage = document.getElementById("notificationMessage");
      
      if (notification && notificationTitle && notificationMessage) {
        notificationTitle.textContent = title;
        notificationMessage.textContent = message;
        notification.classList.remove("hidden");
        
        setTimeout(() => {
          notification.classList.add("hidden");
        }, 3000);
      }
    }
    
    const closeNotification = document.getElementById("closeNotification");
    if (closeNotification) {
      closeNotification.addEventListener("click", function() {
        document.getElementById("statusNotification").classList.add("hidden");
      });
    }
  });
