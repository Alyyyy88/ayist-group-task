function sortProjects() {
  const sortBy = document.getElementById('sortProjects').value;
  const container = document.getElementById('projectsContainer');
  const projects = Array.from(container.children);
  
  projects.sort((a, b) => {
    if (sortBy === 'name') {
      return a.dataset.name.localeCompare(b.dataset.name);
    } else if (sortBy === 'status') {
      return a.dataset.status.localeCompare(b.dataset.status);
    } else if (sortBy === 'progress') {
      return parseInt(b.dataset.progress) - parseInt(a.dataset.progress);
    }
  });
  
  container.innerHTML = '';
  projects.forEach(project => container.appendChild(project));
}

function filterProjects() {
  const searchText = document.getElementById('searchProjects').value.toLowerCase();
  const projects = document.querySelectorAll('#projectsContainer > div');
  
  projects.forEach(project => {
    const name = project.dataset.name.toLowerCase();
    const status = project.dataset.status.toLowerCase();
    const client = project.querySelector('p').textContent.toLowerCase();
    
    if (name.includes(searchText) || status.includes(searchText) || client.includes(searchText)) {
      project.style.display = '';
    } else {
      project.style.display = 'none';
    }
  });
}