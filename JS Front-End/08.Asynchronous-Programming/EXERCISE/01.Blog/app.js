function attachEvents() {
    const postsUrl = 'http://localhost:3030/jsonstore/blog/posts';
    const commentsUrl = 'http://localhost:3030/jsonstore/blog/comments';
    const loadButton = document.getElementById('btnLoadPosts');
    const selectMenu = document.getElementById('posts');
    const viewButton = document.getElementById('btnViewPost');

    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const commentsUl = document.getElementById('post-comments');

    let totalPosts = [];

    loadButton.addEventListener('click', async () => {
        selectMenu.innerHTML = "";
        let response = await fetch(postsUrl);
        let data = await response.json();

        let postsData = Object.values(data);
        postsData.forEach(post => {
            let newOption = document.createElement('option');
            newOption.value = post.id;
            newOption.textContent = post.title;
            totalPosts.push({id: post.id, title: post.title, body: post.body});
        
            selectMenu.appendChild(newOption);
        });
        
    });

    viewButton.addEventListener('click', async () => {
        commentsUl.innerHTML = "";
        let response = await fetch(commentsUrl);
        let data = await response.json();

        let commentsData = Object.values(data);
        let rightPostComments = commentsData.filter(comment => comment.postId == selectMenu.value);
        let rightPost = totalPosts.find(post => post.id === selectMenu.value);

        postTitle.textContent = rightPost.title;
        postBody.textContent = rightPost.body;
        for (let comment of rightPostComments) {
            let newLi = document.createElement('li');
            newLi.textContent = comment.text;
            commentsUl.appendChild(newLi);
        }
    });
}

attachEvents();
