const container = document.getElementById('post-list');
form_element = document.querySelector('form');
textarea_element = document.getElementById('post-content');

// ----------------------------------------------------
// 1. DELETE FUNCTION
// ----------------------------------------------------

async function deletePost(id) {
    try {
        const id_ = parseInt(id);
        const response = await fetch(`http://127.0.0.1:8000/post/${id_}`, {
            method: 'DELETE',
        });
        
        const deleteToastElement = document.createElement('div');
        
        if (response.ok) {
            deleteToastElement.innerHTML = `
                <div class="toast">
                    <div class="alert alert-info">
                        <span>Post ${id} deleted.</span>
                    </div>
                </div>
            `;
            
            // 🚨 THE CRITICAL MISSING STEP:
            // Append the new element to the <body> so it becomes visible.
            document.body.appendChild(deleteToastElement);
            
            setTimeout(() => {
                deleteToastElement.remove(); // This removes the element after 3 seconds
            }, 3000);
            
            loadPosts(); 
        } else {
            alert(`Failed to delete post ${id}. Status: ${response.status}`);
        }
    } catch (error) {
        console.error("Error deleting post:", error);
    }
}
// ----------------------------------------------------
// 2. LOAD POSTS FUNCTION (for initial load and refresh)
// ----------------------------------------------------

async function loadPosts() {
    // Clear existing content to prevent duplicates on refresh
    container.innerHTML = ''; 
    
    const response = await fetch('http://127.0.0.1:8000/posts');
    const data = await response.json();
    
    // Use Object.keys() for robust check of empty dictionary/object
    if (Object.keys(data).length === 0 || data.length === 0) { 
        container.innerHTML = `<li class="list-none">No posts available.</li>`;
        return;
    }

    // Ensure we handle both array and object data structures
    const postsArray = Array.isArray(data) ? data : Object.values(data);

    postsArray.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = "mb-4 p-4 border rounded shadow-sm";
        postElement.innerHTML = `
             <li class="list-row list-none">
                <div class="flex items-center gap-2 mb-2">
                <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/1@94.webp"/></div>
                <div>Dio Lupa</div>
                </div>
                <p class="list-col-wrap text-md">
                 ${post.content}
                </p>
                <button class="btn btn-xs delete-btn text-red-500 text-sm" data-post-id="${post.id}">Delete</button>
                <button class="btn btn-xs text-green-500 text-sm" >View</button>
            </li>
        `;
        
        // --- FIX: BUTTON SELECTION AND LISTENER MUST BE INSIDE THE LOOP ---
        const deleteButton = postElement.querySelector('.delete-btn');
        deleteButton.addEventListener('click', () => {
            const postId = deleteButton.getAttribute('data-post-id');
            deletePost(postId);
        });
        // --- END FIX ---

        container.appendChild(postElement);
    });
}

// ----------------------------------------------------
// 3. POST SUBMISSION
// ----------------------------------------------------

form_element.onsubmit = async (e) => {
    e.preventDefault();
    const content = textarea_element.value;
    
    const response = await fetch('http://127.0.0.1:8000/post', { // Changed /post/ to /posts
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content })
    });
    
    if (response.ok) {
        textarea_element.value = ''; // Clear the input
        loadPosts(); // Reload posts to show the new one
    } else {
        alert("Failed to submit post.");
    }
}

// ----------------------------------------------------
// INITIAL EXECUTION
// ----------------------------------------------------
loadPosts();