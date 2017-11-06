import datetime
from haystack import indexes
from myapp.models import Dweet, User


class DweetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    content = indexes.CharField(model_attr='dweet_data')
    dweet_id = indexes.CharField(model_attr='dweet_id')
    created_time = indexes.DateTimeField(model_attr='created_time')

    def get_model(self):
        return Dweet

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_time__lte=datetime.datetime.now())


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    user_id = indexes.CharField(model_attr='user_id')
    user_first_name = indexes.CharField(model_attr='user_first_name')
    user_last_name = indexes.CharField(model_attr='user_last_name')
    user_profile_name = indexes.CharField(model_attr='user_profile_name')
    modified_time = indexes.DateTimeField(model_attr='modified_time')

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(modified_time__lte=datetime.datetime.now())
