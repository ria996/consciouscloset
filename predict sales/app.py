import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def convert_item_to_int(word):
    word_dict = {'Jeans':1, 'Dress':2, 'Jacket':3, 'Shirt':4, 'Crop top':5, 'Hoodie':6, 'Sweatshirt':7}
    return word_dict[word]

def convert_color_to_int(word):
    word_dict = {'Blue':1, 'Red':2, 'White':3, 'Green':4, 'Pink':5, 'Tan':6, 'Black':7, 'Gray':8, 'Beige':9, 'Brown':10, 'Purple':11, 'Yellow':12}
    return word_dict[word]

def convert_size_to_int(word):
    word_dict = {'S':1, 'M':2, 'XS':3, 'XL':4, 'L':5}
    return word_dict[word]

def convert_material_to_int(word):
    word_dict = {'Cotton':1, 'Polyester':2, 'Nylon':3, 'Denim':4, 'Rayon':5, 'Viscose':6, 'Modal':7}
    return word_dict[word]

def convert_int_to_company(word):
    word_dict = {1:'ThredUP', 2:'Poshmark'}
    return word_dict[word]

def convert_company_to_int(word):
    word_dict = {'ThredUP':1, 'Poshmark':2, 'Vinted':3}
    return word_dict[word]

def convert_item_to_link(word):
    word_dict = {'Jeans':"https://www.thredup.com/product/women-cotton-hollister-blue-khakis/143227024", 'Shirt':"https://www.thredup.com/product/women-cotton-urban-outfitters-white-short-sleeve-t-Shirt/144928480?query_id=778046250536452096&result_id=778046257679335424&suggestion_id=778046250590978070"}
    return word_dict[word]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    item_int = convert_item_to_int(request.form.get('Item type'))
    color_int = convert_color_to_int(request.form.get('Color'))
    size_int = convert_size_to_int(request.form.get('Size'))
    material_int = convert_material_to_int(request.form.get('Material'))
    int_features = [item_int, color_int, size_int, material_int]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    company = convert_int_to_company(output)
    clothing_link = ""
        
    
    water_saved = ""
    light_saved = ""
    driving_saved = ""
    you_saved = "You will save: "
    
    if request.form.get('Item type') == "Shirt":
        water_saved = "471.24 glasses of drinking water"
        light_saved = "184.57 hours of powering an LED light"
        driving_saved = "0.87 miles of driving emissions"
        
    if request.form.get('Item type') == "Jeans":
        water_saved = "678.6 glasses of drinking water"
        light_saved = "244.56 hours of powering an LED light"
        driving_saved = "0.66 miles of driving emissions"
        
    if request.form.get('Item type') == "Dress":
        water_saved = "1264.88 glasses of drinking water"
        light_saved = "537.42 hours of powering an LED light"
        driving_saved = "2.61 miles of driving emissions"
        
    if request.form.get('Item type') == "Jacket":
        water_saved = "387.64 glasses of drinking water"
        light_saved = "311.75 hours of powering an LED light"
        driving_saved = "2.14 miles of driving emissions"
        
    if request.form.get('Item type') == "Crop top":
        water_saved = "174.09 glasses of drinking water"
        light_saved = "49.94 hours of powering an LED light"
        driving_saved = "0.27 miles of driving emissions"
        
    if company == convert_int_to_company(output):
        if item_int == 1:
            clothing_link = "https://www.thredup.com/product/women-cotton-hollister-blue-khakis/143227024"
    if company == convert_int_to_company(output):
        if item_int == 4:
            clothing_link = "https://www.thredup.com/product/women-cotton-urban-outfitters-white-short-sleeve-t-Shirt/144928480?query_id=778046250536452096&result_id=778046257679335424&suggestion_id=778046250590978070"    
        

    ptext = "Alternative clothing"
    return render_template('index.html', prediction_text='{}'.format(ptext), p_text = '{}'.format(clothing_link), save_text='{}'.format(you_saved), water_text='{}'.format(water_saved), light_text='{}'.format(light_saved), driving_text='{}'.format(driving_saved))


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)