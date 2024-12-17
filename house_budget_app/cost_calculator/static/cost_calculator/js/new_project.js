function toggleProjectDetails() {
    const projectType = document.getElementById('project_type').value;
    const partialSection = document.getElementById('partial_section');
    const worksSection = document.getElementById('works_section');

    if (projectType === 'partial') {
        partialSection.style.display = 'block';
        worksSection.style.display = 'none'; // Reset works visibility
    } else {
        partialSection.style.display = 'none';
        worksSection.style.display = 'none';
    }
}

function showWorks() {
    const housePart = document.getElementById('house_part').value;
    const worksSection = document.getElementById('works_section');
    const worksList = document.getElementById('works_list');

    fetch(`/get-works/${housePart}/`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                worksSection.style.display = 'block';
                worksList.innerHTML = '';

                data.works.forEach(work => {
                    worksList.innerHTML += `
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" name="works" value="${work}">
                            <label class="form-check-label">${work}</label>
                        </div>
                    `;
                });
            }
        });
}

document.getElementById('projectForm').addEventListener('change', function () {
    const formData = new FormData(this);

    fetch('/calculate-cost/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('total_cost').innerText = `Total Cost: $${data.total_cost}`;
        }
    });
});
