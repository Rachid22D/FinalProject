document.addEventListener('DOMContentLoaded', async () => {
    // تحميل البيانات من ملف JSON
    const response = await fetch('/static/cost_calculator/data/common_data.json');
    const data = await response.json();
    const houseParts = data.houseParts;
    const worksForParts = data.worksForParts;

    // تحديد العناصر
    const projectTypeSelect = document.getElementById('project_type');
    const partialSection = document.getElementById('partial_section');
    const housePartSelect = document.getElementById('house_part');
    const worksSection = document.getElementById('works_section');
    const worksList = document.getElementById('works_list');
    const workAreaInput = document.getElementById('work_area');
    const budgetCategorySelect = document.getElementById('budget_category');
    const submitButton = document.querySelector('button[type="submit"]');

    // تعبئة قائمة أجزاء المنزل
    houseParts.forEach(part => {
        const option = document.createElement('option');
        option.value = part.id;
        option.textContent = part.name;
        housePartSelect.appendChild(option);
    });

    // دالة التبديل بناءً على نوع المشروع
    projectTypeSelect.addEventListener('change', () => {
        if (projectTypeSelect.value === 'partial') {
            partialSection.style.display = 'block';
            worksSection.style.display = 'none';
            housePartSelect.value = ''; // إعادة تعيين اختيار جزء المنزل
            workAreaInput.value = ''; // إعادة تعيين مساحة العمل
            worksList.innerHTML = ''; // تفريغ الأعمال
        } else {
            partialSection.style.display = 'none';
            worksSection.style.display = 'none';
            housePartSelect.value = ''; // إعادة تعيين اختيار جزء المنزل
            workAreaInput.value = ''; // إعادة تعيين مساحة العمل
            worksList.innerHTML = ''; // تفريغ الأعمال
        }
    });

    // عند اختيار جزء من المنزل، يتم تحديث قائمة الأعمال
    housePartSelect.addEventListener('change', () => {
        const selectedPart = housePartSelect.value;
        updateWorksSection(selectedPart);
    });

    // تحديث قائمة الأعمال
    function updateWorksSection(selectedPart) {
        worksList.innerHTML = ''; // تفريغ المحتوى السابق
        const works = worksForParts[selectedPart];
        if (works) {
            worksSection.style.display = 'block';
            works.forEach(work => {
                const checkboxContainer = document.createElement('div');
                checkboxContainer.className = 'form-check';

                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.id = `work_${work}`;
                checkbox.name = 'works';
                checkbox.value = work;
                checkbox.className = 'form-check-input';

                const label = document.createElement('label');
                label.htmlFor = `work_${work}`;
                label.textContent = work;
                label.className = 'form-check-label';

                checkboxContainer.appendChild(checkbox);
                checkboxContainer.appendChild(label);
                worksList.appendChild(checkboxContainer);
            });
        } else {
            worksSection.style.display = 'none';
        }
    }

    // التحقق من المدخلات قبل إرسال النموذج
    
});
