def test_create_post(client):
    user = User(username='testuser')
    db.session.add(user)
    db.session.commit()

    response = client.post(f'/users/{user.id}/posts/new', data={
        'title': 'Test Post',
        'content': 'This is a test post.'
    })
    assert response.status_code == 302  # Redirect
    assert Post.query.count() == 1
