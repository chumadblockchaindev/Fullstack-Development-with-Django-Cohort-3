const container = document.getElementById('post-list');
form_element = document.querySelector('form');
textarea_element = document.getElementById('post-content');

// ----------------------------------------------------
// 1. DELETE FUNCTION
// ----------------------------------------------------

async function deletePost(id) {
    try {
        // Corrected URL: Use :8000 port and ensure the path matches your API
        const id_ = parseInt(id)
        const response = await fetch(`http://127.0.0.1:8000/post/${id_}`, { 
            method: 'DELETE',
        });
        
        if (response.ok) {
            alert(`Post ${id} deleted.`);
            loadPosts(); // Reload posts without refreshing the whole page
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
        container.innerHTML = "<li>No posts available.</li>";
        return;
    }

    // Ensure we handle both array and object data structures
    const postsArray = Array.isArray(data) ? data : Object.values(data);

    postsArray.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = "mb-4 p-4 border rounded shadow-sm";
        postElement.innerHTML = `
            ${post.id} - 
            ${post.content}
            <button class="delete-btn text-red-500 text-sm" data-post-id="${post.id}">Delete</button>
            <button class="text-gray-500 text-sm" > View</button>
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