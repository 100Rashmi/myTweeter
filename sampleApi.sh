curl -X POST \
-d '{"email":"ramesh@git.com","password":"1234","first_name":"ramesh","last_name":"kumar","profile_name":"ramesh_kumar"}' \
'http://localhost:8000/myapp/signup'

curl -X POST \
-d '{   "email"  :  "ramesh@git.com",  "password"  : "1234"  }' \
'http://localhost:8000/myapp/login'

curl -X POST \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
-d '{   "dweet_data"    :"hello dweet"   }' \
'http://127.0.0.1:8000/myapp/dweet'

curl -X POST \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
-d '{   "dweet_id"  :  "d_41254c03-277c-4b14-935e-574d76b67e9f"  ,   "comment"   :   "dweeter"   }' \
'http://127.0.0.1:8000/myapp/comment'

curl -X POST \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
-d '{  "entity_id"  :  "d_41254c03-277c-4b14-935e-574d76b67e9f" }' \
'http://127.0.0.1:8000/myapp/like'

curl -X POST \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
-d '{  "followed_user_id"  :  "d4dbd067-7060-4ce4-a3d5-253842d6fb05"  }' \
'http://127.0.0.1:8000/myapp/follow'

curl -X GET \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
'http://127.0.0.1:8000/myapp/feed'

curl -X GET \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
'http://127.0.0.1:8000/myapp/searchDweet?q=hello'

curl -X GET \
-H 'session-id:14db9d33-ef2e-4f70-a1e5-b0c2ac918153' \
-H 'account-id:6e7b6589-5d12-4075-8a38-c9d9fcb0883a' \
'http://127.0.0.1:8000/myapp/searchUsers?q=ramesh'







