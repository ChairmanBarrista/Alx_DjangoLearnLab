# Blog Post Management (CRUD)

## Overview
This module implements full CRUD for Post model:
- List (public): /posts/ or root '/'
- Detail (public): /posts/<pk>/
- Create (authenticated): /posts/new/
- Update (author-only): /posts/<pk>/edit/
- Delete (author-only): /posts/<pk>/delete/

## Key Files
- models.py: Post model with `get_absolute_url`.
- forms.py: `PostForm` (ModelForm for title + content).
- views.py: Class-based views (ListView, DetailView, CreateView, UpdateView, DeleteView).
- urls.py: URL mappings for CRUD endpoints.
- templates/blog/: templates for list, detail, form, and confirmation.

## Permissions
- Create requires login.
- Edit/Delete require user to be the post's author (enforced via `UserPassesTestMixin`).

## How to use
1. Run server: `python manage.py runserver`
2. Visit `/posts/`.
3. Login / Register to create posts.
4. Authors can edit and delete their posts using links on list/detail pages.

## Testing
Manual steps:
- Register -> create a post -> ensure you can edit/delete it.
- Try editing as another user -> should be denied.
- Ensure CSRF tokens present & forms validate.

## Notes
- Post list is paginated (10 per page). Adjust `paginate_by` in `PostListView`.
- If you want friendly URLs (slugs) later, add a `slug` field and update `get_absolute_url` and URLs accordingly.
