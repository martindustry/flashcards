from django.test import TestCase
from flashcards.models import Collection, Flashcard
from users.models import User


class CollectionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser',
            password='7,a}MXe+oTJL'
        )
        Collection.objects.create(
            title='CollectionTestTitle',
            author=test_user,
            language1='Polish',
            language2='English',
        )

    def test_title_max_length(self):
        collection = Collection.objects.get(id=1)
        max_length = collection._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_languages_max_length(self):
        collection = Collection.objects.get(id=1)
        max_length1 = collection._meta.get_field('language1').max_length
        self.assertEqual(max_length1, 50)
        max_length2 = collection._meta.get_field('language2').max_length
        self.assertEqual(max_length2, 50)

    def test_default_public_is_false(self):
        collection = Collection.objects.get(id=1)
        self.assertFalse(collection.public)

    def test_object_name_is_correct(self):
        collection = Collection.objects.get(id=1)
        expected_object_name = f"{collection.title} ({collection.id})"
        self.assertEqual(str(collection), expected_object_name)


class FlashcardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser',
            password='7,a}MXe+oTJL'
        )
        collection = Collection.objects.create(
            title='CollectionTestTitle',
            author=test_user,
            language1='Polish',
            language2='English',
        )
        Flashcard.objects.create(
            task='FlashcardTestTask',
            solution='FlashcardTestSolution',
            collection=collection
        )

    def test_task_max_length(self):
        flashcard = Flashcard.objects.get(id=1)
        max_length = flashcard._meta.get_field('task').max_length
        self.assertEqual(max_length, 250)

    def test_solution_max_length(self):
        flashcard = Flashcard.objects.get(id=1)
        max_length = flashcard._meta.get_field('solution').max_length
        self.assertEqual(max_length, 250)

    def test_object_name_is_correct(self):
        flashcard = Flashcard.objects.get(id=1)
        expected_object_name = f'#{flashcard.id}'
        self.assertEqual(str(flashcard), expected_object_name)
