from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi=0
    category=''
    if request.method == 'POST':
        weight=int(request.form['weight'])
        height=int(request.form['height'])
    #if height:
        bmi=round(weight / (height ** 2), 2)
        if bmi< 18.5:
            category='underweight'
        elif 18.5<= bmi <24.9:
            category='normal weight'
        elif 25 <= bmi < 29.9:
            category='overweight'
        else:
            category='obese'

    #else:
        #bmi="Invalid height"
    return render_template('index.html', bmi=bmi, category=category)
if __name__=='__main__':
    app.run(debug=True)
