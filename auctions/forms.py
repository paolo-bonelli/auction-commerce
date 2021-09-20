from django.forms import ModelForm, TextInput
from .models import AuctionListing, AuctionCategory, Bid, Comment


# Script found in: https://gist.github.com/stefanocoding/4563866cef0ec197d8b1ccb183d1163d
# By stefanocoding at github in https://gist.github.com/stefanocoding
# The porpouse is to create a List from the values given by the User
# The values must be separated by commas otherwise it wont work

class ManyToManyInput(TextInput):
    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            return value.split(',')


class CreateAuctionForm(ModelForm):
    class Meta:
        model = AuctionListing
        fields = ['Title', 'img', 'description',
                  'Starting Price', ]
        # widgets = {
        #     'categories': ManyToManyInput()
        # }

    def is_valid(self):
        print(self.instance.categories)
        return super().is_valid()


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['offer', ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
