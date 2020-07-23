# django-learning
django project via django rest framework

##create virutal environment and activate
python3.8 -m venv env

source env/bin/activate

##install required packages
pip install -r requirement.txt


##create a django project
django-admin.py startproject djangolearning .


##enable app for django
python manage.py startapp api


##create user database model


##set custom user model
under settings.py

##make migrations
python3 manage.py makemigrations api

python3 manage.py migrate

error: django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency api.0001_initial on database 'default'.

Delete the _pycache_ and the 0001_initial files.
Delete the db.sqlite3 from the root directory (be careful all your data will go away).

##create super user
python3 manage.py createsuperuser

##enable django admin

##APIView and ViewSet
1.APIView--need full control over your logic
         --processing files and rendering a synchoronous response
         --You are calling other APIs /services
         --Access local files or data

2.ViewSet--takes care of a lot of typical logic for you
         --perfect for standard database operations
         --fastest way to make a database interface
         --a Simple CRUD interface to your database
         --a quick and simple api
         --little to no customization on the logic
         --working with standard data structure

##serializer


##viewset case
1.views creation
2.url router creation


##create profile api

##create profiles viewset


##register profile viewset with url router



##create permission a profile
create a new permission.py file

##add authentication and permissions to viewset


##add search profiles


##add search profiles feature
add new viewsets


##add loging api view
new view: UserLoginApiView
/api/login/   get a token
/api/profile/1  add Authorization  Token xxxx to your request header 
only after that you can have access to modify your profile


##create profile feed api
/api/feed/      list all feed items,get all,post(create feed item for logged in user)

/api/feed/<feed_item_id> manage,get,put/patch/delete feed item

###add new model item
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model as a string"""
        return self.status_text

###create and run model migration
python3 manage.py makemigrations
python3 manage.py  migrate

###add profile feed model to admin
add to admin, then django admin can manage the new feed api
admin.site.register(models.ProfileFeedItem)

###create profile feed item serializer
class ProfileFeedItemSerializer(serializers.ModelSerializer):
      """Serializer profile feed items"""
      class Meta:
            model = models.ProfileFeedItem
            fields = ('id','user_profile','status_text','created_on')
            extra_kwargs = {'user_profile': {'read_only': True}}

###create viewset for our profile feed item
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handle creating,reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileFeedSerializer
    queryset = models.UserProfileFeedItem.objects.all()

    def perform_create(self,serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


###add permissions for feed API


###restrict viewing status updates to logged in users only
