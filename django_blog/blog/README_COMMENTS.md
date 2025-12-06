# Comments Feature

## Overview
Comments allow users to view, post, edit, and delete comments tied to a Post.

## Model
- Comment: post (FK), author (FK), content, created_at, updated_at

## URLs
- Create:  /posts/<post_pk>/comments/new/      (POST, login required)
- Edit:    /comments/<comment_pk>/edit/       (GET/POST, author only)
- Delete:  /comments/<comment_pk>/delete/     (GET/POST, author only)

## Permissions
- Anyone can read comments.
- Only authenticated users can post.
- Only the comment's author can edit or delete it.

## How to use
1. View a post at `/posts/<pk>/`
2. Scroll to Comments, write in the inline form, and submit.
3. Edit or delete your own comments using the Edit/Delete links next to your comment.

## Notes
- All forms are CSRF-protected.
- Comment content is validated to prevent empty submissions.
