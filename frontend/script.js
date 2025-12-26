document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const files = document.getElementById('file-input').files;
    if (files.length === 0) {
        alert('Пожалуйста, выберите файлы');
        return;
    }

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
    }

    try {
        const response = await fetch('/merge', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'merged.txt';
            document.body.appendChild(a);
            a.click();
            a.remove();
        } else {
            const errorText = await response.text();
            document.getElementById('result').innerText = `Ошибка: ${errorText}`;
        }
    } catch (error) {
        document.getElementById('result').innerText = `Ошибка: ${error.message}`;
    }
});
