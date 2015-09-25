import metamind.api
from metamind.api import set_api_key, ClassificationData, ClassificationModel, food_image_classifier
#import time
import json
from datetime import date

fruit = ClassificationModel(private=True, name='fruits')

def train_data():
	set_api_key('bHIqZD7ZJgRDn4oDWwMiSkDdGiuX3YvHKeCdNV1VF2WkQJO5gR')
	training_data = ClassificationData(private=True, data_type='image',name='training images')
	training_data.add_samples([
		('./imgs/banana.jpg','fruits'),('./imgs/blueberries.jpg','fruits'),('./imgs/fruit_collection2.jpg','fruits'),('./imgs/fruit_collection.jpg','fruits'),('./imgs/grapefruit.jpg','fruits'),
		('./imgs/grapes.jpg','fruits'),('./imgs/oranges.jpg','fruits'),('./imgs/peaches.jpg','fruits'),('./imgs/pears.jpg','fruits'),('./imgs/strawberries.jpg','fruits'),('./imgs/watermelon.jpg','fruits'),('./imgs/carrots.jpg','vegetables'),('./imgs/lettuce.jpg','vegetables'),('./imgs/radish.jpg','vegetables')], input_type='files')
	training_data.add_samples([
	('http://punchbowlsocial.com/wp-content/uploads/2015/02/eyg.jpg','eggs'),('http://media.thefowlergroup.com.s3.amazonaws.com/wp-content/uploads/2012/05/copywriting-deli-ham.jpg','meat'),('http://www.tyson.com/~/media/Consumer/Call-Outs/fresh-package.ashx?la=en','meat'),('http://homeguides.sfgate.com/DM-Resize/photos.demandstudios.com/gett/article/83/5/86544602_XS.jpg?w=442&h=442&keep_ratio=1','dairy'),('http://i-store.walmart.ca/images/WMTCNPE/155/016/155016_Large_1.jpeg','dairy'),('http://www.10tv.com/content/graphics/2014/08/29/kraft-singles-american.jpg','dairy')], input_type='urls')
	
	fruit.fit(training_data)
#train_data()

def classify(in_img, ingredients):
	train_data()
	specific_descript = food_image_classifier.predict(in_img, input_type='files')
	print(specific_descript)
	general_descript = fruit.predict(in_img, input_type='files')
	entry = date(2015, 10, 11)
	if(general_descript[0]['label'] == 'meat'):
		expiary = date(entry.year, entry.month, entry.day + 5)
	elif(general_descript[0]['label'] == 'vegetables'):
		expiary = date(entry.year, entry.month, entry.day + 14)
	elif(general_descript[0]['label'] == 'fruits'):
		expiary = date(entry.year, entry.month, entry.day + 7)
	elif(general_descript[0]['label'] == 'dairy'):
		expiary = date(entry.year, entry.month, entry.day + 14)
	else:
		expiary = date(entry.year, entry.month, entry.day + 7)
	ingredients.append({'name': specific_descript[0]['label'], 'class': general_descript[0]['label'], 'entry_date': entry, 'exp_date': expiary})
	print(ingredients)
	f = open('./inventory.txt', 'r+b')
	for item in ingredients:
		add = str(item)
		f.write(add)
	f.close()
	

#dict = []
#classify('./imgs/in_01.jpg',dict)
