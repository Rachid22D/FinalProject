document.addEventListener('DOMContentLoaded', () => {
    // جلب قيمة CSRF Token من الحقل المخفي
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // التعامل مع أزرار الحذف
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', () => {
            const projectId = button.getAttribute('data-id');

            // إرسال طلب الحذف عبر Fetch API
            fetch(`/delete-project/${projectId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // تمرير الـ CSRF Token في الرؤوس
                },
                body: JSON.stringify({}) // يمكن إرسال بيانات إضافية إذا لزم الأمر
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // حذف العنصر من الصفحة إذا تمت العملية بنجاح
                    const projectElement = document.getElementById(`project-${projectId}`);
                    if (projectElement) {
                        projectElement.remove();
                    }
                } else {
                    console.error("Failed to delete project:", data.message);
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });
});
