## The Dweeter
Dweeter is an RESTFul web app that is similar to twitter with following functionalities:-
- View all the dweets from followed folks 
- Add new dweets 
- Like someone's dweet 
- Comment on the dweet 
- Search dweeters 
- Follow new dweeters 
- Search dweets 
- Create new account (Auth) 


## API Documentation
### SignUp API:   `/signup` 
```
curl -X POST 
-d '{"email":<email>,"password":<password>,"first_name":<firstname>,"last_name":<lastname>,"profile_name":<profilename>}' 
'http://localhost:8000/myapp/signup'
```

### Login API:   `/login` 
If email-password combination is correct, 
This api returns the `account-id` corresponding to the below emailId and a new `session-id`, with a 30 mins validity,
renewable after every use.  
```
curl -X POST
-d '{   "email"  :  <emailid>,  "password"  : <password>  }'
'http://localhost:8000/myapp/login'
```

### Dweet API: `/dweet`
```
 curl -X POST 
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{   "dweet_data"    :<dweet data>   }'
'http://127.0.0.1:8000/myapp/dweet'
```

### Comment API: `/comment`
```
 curl -X POST 
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{   "dweet_id"  :  <dweet-id>  ,   "comment"   :   <comment>   }'
'http://127.0.0.1:8000/myapp/comment'
```


### Like API: `/like`
```
curl -X POST
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{  "entity_id"  :  <anyTweetId or CommentId> }'
'http://127.0.0.1:8000/myapp/like'
```

### Follow API: `/follow`
```
curl -X POST
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{  "followed_user_id"  :  <userIdToBeFollowed>  }'
'http://127.0.0.1:8000/myapp/follow'
```

### Get Dweets from followed Dweeters in your Feed `/feed`
```
curl -X GET
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
'http://127.0.0.1:8000/myapp/feed'
```

### Search Dweets API: `/searchDweet`
```
curl -X GET
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
'http://127.0.0.1:8000/myapp/searchDweet?q=<keywords>'
```

### Search Users API: `/searchUsers`
```
curl -X GET
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
'http://127.0.0.1:8000/myapp/searchUsers?q=<name>'
```

  ## Tech Stack Used:-
  - Django
  - MySql
  - HayStack
  - Elastic Search


## Data Model:


- Table : Account

| Field          | Type          | Null | Key | Default | Extra |
|----------------|---------------|------|-----|---------|-------|
| account_id     | varchar(50)   | NO   | PRI | NULL    |       |
| account_email  | varchar(50)   | NO   | UNI | NULL    |       |
| account_status | varchar(50)   | NO   |     | NULL    |       |
| login_password | varchar(1024) | NO   | MUL | NULL    |       |

- Table: User

| Field             | Type        | Null | Key | Default | Extra |
|-------------------|-------------|------|-----|---------|-------|
| user_id           | varchar(50) | NO   | PRI | NULL    |       |
| user_first_name   | varchar(50) | NO   |     | NULL    |       |
| user_last_name    | varchar(50) | NO   |     | NULL    |       |
| user_profile_name | varchar(50) | NO   | UNI | NULL    |       |
| created_time      | datetime(6) | NO   |     | NULL    |       |
| modified_time     | datetime(6) | NO   |     | NULL    |       |

- Table: Dweet


| Field        | Type        | Null | Key | Default | Extra |
|--------------|-------------|------|-----|---------|-------|
| account_id   | varchar(50) | NO   |     | NULL    |       |
| dweet_data   | longtext    | NO   |     | NULL    |       |
| dweet_id     | varchar(50) | NO   | PRI | NULL    |       |
| created_time | datetime(6) | NO   |     | NULL    |       |


- Table: Session

| Field          | Type         | Null | Key | Default | Extra |
|----------------|--------------|------|-----|---------|-------|
| session_id     | varchar(254) | NO   | PRI | NULL    |       |
| created_time   | datetime(6)  | NO   |     | NULL    |       |
| account_id     | varchar(50)  | NO   | MUL | NULL    |       |
| last_used_time | datetime(6)  | NO   | MUL | NULL    |       |


- Table : Like

| Field      | Type        | Null | Key | Default | Extra          |
|------------|-------------|------|-----|---------|----------------|
| id         | int(11)     | NO   | PRI | NULL    | auto_increment |
| account_id | varchar(50) | NO   | MUL | NULL    |                |
| entity_id  | varchar(50) | NO   | MUL | NULL    |                |

- Table : Follower

| Field            | Type        | Null | Key | Default | Extra          |
|------------------|-------------|------|-----|---------|----------------|
| id               | int(11)     | NO   | PRI | NULL    | auto_increment |
| user_id          | varchar(50) | NO   | MUL | NULL    |                |
| followed_user_id | varchar(50) | NO   |     | NULL    |                |


- Table : Comment


| Field        | Type        | Null | Key | Default | Extra |
|--------------|-------------|------|-----|---------|-------|
| account_id   | varchar(50) | NO   |     | NULL    |       |
| dweet_id     | varchar(50) | NO   | MUL | NULL    |       |
| comment_id   | varchar(50) | NO   | PRI | NULL    |       |
| comment_data | longtext    | NO   |     | NULL    |       |
| created_time | datetime(6) | NO   | MUL | NULL    |       |





