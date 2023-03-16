from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    def test_get_todo_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_get_add_page(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_list.html')

    def test_get_edit_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_list.html')

    def test_can_add(self):
        response = self.client.post('/add/', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/del/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
