
document.getElementById('construction-type').addEventListener('change', function () {
    const selectedOption = this.value;
    const partsDropdown = document.getElementById('parts-dropdown');
    const dataDisplay = document.getElementById('data-display');
    const housePart = document.getElementById('house-part');
    const unitQuantitySection = document.getElementById('unit-quantity-section');
    const fullHouseAreaSection = document.getElementById('full-house-area-section');
    const displayContent = document.getElementById('display-content');
    const totalCalculation = document.getElementById('total-calculation');

    if (selectedOption === 'part_of_house') {
        partsDropdown.style.display = 'block';
        unitQuantitySection.style.display = 'none';
        fullHouseAreaSection.style.display = 'none';
        dataDisplay.style.display = 'none';

        // إرسال طلب لجلب الأجزاء المتاحة
        fetch('/get_subcategories/')
            .then((response) => response.json())
            .then((data) => {
                housePart.innerHTML = '<option value="">Select a part</option>';
                data.subcategories.forEach((subcategory) => {
                    const option = document.createElement('option');
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    housePart.appendChild(option);
                });
            })
            .catch((error) => console.error('Error fetching subcategories:', error));
    } else if (selectedOption === 'full_house') {
        partsDropdown.style.display = 'none';
        unitQuantitySection.style.display = 'none';
        fullHouseAreaSection.style.display = 'block';
        dataDisplay.style.display = 'block';

        // التعامل مع إدخال مساحة المنزل
        document.getElementById('full-house-area').addEventListener('input', function () {
            const area = parseFloat(this.value);
            if (area && area > 0) {
                // إرسال طلب لجلب بيانات المنزل بالكامل
                fetch('/get_full_house_data/')
                    .then((response) => response.json())
                    .then((data) => {
                        displayContent.innerHTML = '';
                        let totalCost = 0;

                        // حساب تكلفة كل جزء بناءً على المساحة
                        data.house_parts.forEach((house_part) => {
                            const partCost = area * (parseFloat(house_part.material_cost) + parseFloat(house_part.labor_cost));
                            totalCost += partCost;

                            displayContent.innerHTML += `
                                <div>
                                    <h4>${house_part.name}</h4>
                                    <p><strong>Material Cost (per ${house_part.unit}):</strong> $${house_part.material_cost}</p>
                                    <p><strong>Labor Cost (per ${house_part.unit}):</strong> $${house_part.labor_cost}</p>
                                    <p><strong>Total Cost for ${area} m²:</strong> $${partCost.toFixed(2)}</p>
                                </div>
                                <hr>
                            `;
                        });

                        totalCalculation.innerHTML = `Total House Cost: $${totalCost.toFixed(2)}`;
                    })
                    .catch((error) => console.error('Error fetching full house data:', error));
            } else {
                displayContent.innerHTML = '';
                totalCalculation.innerHTML = '';
            }
        });

    } else {
        partsDropdown.style.display = 'none';
        unitQuantitySection.style.display = 'none';
        fullHouseAreaSection.style.display = 'none';
        dataDisplay.style.display = 'none';
    }
});

// التعامل مع تغيير اختيار جزء من المنزل
document.getElementById('house-part').addEventListener('change', function () {
    const partId = this.value;
    const unitQuantitySection = document.getElementById('unit-quantity-section');
    const dataDisplay = document.getElementById('data-display');
    const displayContent = document.getElementById('display-content');
    const totalCalculation = document.getElementById('total-calculation');

    if (partId) {
        unitQuantitySection.style.display = 'block';
        dataDisplay.style.display = 'block';

        // إرسال طلب لجلب بيانات الجزء المختار
        fetch(`/get_house_part_data/${partId}/`)
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    displayContent.innerHTML = `<p style="color: red;">${data.error}</p>`;
                    return;
                }

                // عرض البيانات بتنسيق
                displayContent.innerHTML = `
                
                    <div>
                        <h4>${data.name}</h4>
                        <p><strong>Description:</strong> ${data.description}</p>
                        <p><strong>Material Cost (per ${data.unit.name}):</strong> $${data.material_cost}</p>
                        <p><strong>Labor Cost (per ${data.unit.name}):</strong> $${data.labor_cost}</p>
                        <hr>
                    </div> 
                    `;
                


                // حساب التكلفة الإجمالية عند إدخال الكمية
                document.getElementById('unit-quantity').addEventListener('input', function () {
                    const quantity = parseFloat(this.value);
                    if (quantity && quantity > 0) {
                        const totalCost = quantity * (data.material_cost + data.labor_cost);
                        totalCalculation.innerHTML = `Total Cost: $${totalCost.toFixed(2)}`;
                    } else {
                        totalCalculation.innerHTML = '';
                    }
                });
            })
            .catch((error) => console.error('Error fetching house part data:', error));
    } else {
        unitQuantitySection.style.display = 'none';
        dataDisplay.style.display = 'none';
    }
});

// زر حفظ المشروع
document.getElementById('save-project').addEventListener('click', function () {
    const title = document.getElementById('project-title').value;
    const type = document.getElementById('construction-type').value;
    const area = document.getElementById('full-house-area').value || null;
    const part = document.getElementById('house-part').value || null;
    const quantity = document.getElementById('unit-quantity').value || null;
    
    if (!title || !type) {
        alert('Please fill in all required fields before saving.');
        return;
    }

    const data = {
        title: title,
        type: type,
        area: area,
        part: part,
        quantity: quantity
    };
    fetch('/save_project/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Project saved successfully!');
                // إعادة التوجيه أو عرض رسالة أخرى بعد الحفظ
            } else {
                alert('Error saving project');
            }
        })
        .catch(error => console.error('Error saving project:', error));
});
