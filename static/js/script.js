document.addEventListener('DOMContentLoaded', function () {
    const taskInput = document.getElementById('task-title');
    const addTaskButton = document.getElementById('add-task-button');
    const taskList = document.getElementById('tasks');

    addTaskButton.addEventListener('click', function () {
        const taskTitle = taskInput.value;
        if (taskTitle) {
            const li = document.createElement('li');
            li.innerHTML = `${taskTitle} <button class="delete-button">Delete</button>`;
            taskList.appendChild(li);
            taskInput.value = '';

            const deleteButtons = document.querySelectorAll('.delete-button');
            deleteButtons.forEach(function (button) {
                button.addEventListener('click', function () {
                    this.parentElement.remove();
                });
            });
        }
    });
});
