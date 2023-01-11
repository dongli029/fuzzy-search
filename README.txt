This code use fuzzy search way to create a simple adding card function 
for any service which need to restore user's card in there database.    

When user want to add card to there wallet, first, user need to enter 
which bank that the credit card belong to.

Then sys will show credit card that the bank offered, and user just need to 
text the card name at the end, sys will store the card to there wallet.

This code use flask_sqlalchemy to create different api to realize CRUD in database.

You can refer to different function's url description in fuzzy search_add card.py.

wallet_sql.py is used to create database in mysql where i created at GCP VM's docker container.

Support cards and banks are list at suppourt bank.json.

