# Facebook-Marketing-API-System-User-Access-Token
Steps to generate a [system user](https://developers.facebook.com/docs/marketing-api/businessmanager/systemuser/) access token for Facebook Marketing API

1. Create a new Facebook App at [Facebook Developers](https://developers.facebook.com/apps)
2. Generate a short lived access token that has ads_read/ads_management permissions using [Facebook API Graph explorer](https://developers.facebook.com/tools/explorer/)
3. Go to Business Manager -> Business Settings -> Users -> System Users. Click on +Add and create a System Admin User and a regular System user that have access to your accounts.
4. Get the app-scoped ID of your system user using [Facebook API Graph explorer](https://developers.facebook.com/tools/explorer/)

```
https://graph.facebook.com/<API_VERSION>/<BUSINESS_ID>/system_users

```
5. Generate your app secret proof using appsecret_proof.py, by passing your short lived access token from Graph API explorer and your app Secret from FB Apps UI.

```
h = hmac.new(b'Enter your short lived accesss token', 'Enter your app secret'.encode('utf-8'), hashlib.sha256 )
```

6. Import Facebook Ads API Access Token.postman_collection into Postman and pass in your App ID, App Secret Proof, App Scoped System User ID, and Short Lived Access token.

