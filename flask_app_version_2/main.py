from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Predefined lists
leetcodetest_easy = [1, 20, 26, 27, 35, 69, 70, 125, 136, 155, 167, 169, 217, 219, 225, 232, 242, 268, 278, 283,
                         287, 344, 345, 349, 350, 367, 374, 389, 438, 441, 442, 448, 496, 575, 641, 682, 704, 744, 844,
                         852, 905, 922, 933, 977, 1004, 1047, 1381, 1441]
leetcodetest_hard = [53, 62, 67, 70, 94, 100, 101, 102, 104, 108, 111, 112, 121, 122, 144, 145, 198, 199, 213, 226,
                         257, 309, 394, 513, 515, 559, 583, 589, 617, 669, 700, 714, 746, 938, 965, 1137, 1143, 1480]

@app.route('/', methods=['GET', 'POST'])
def index():
    result1 = result2 = None
    if request.method == 'POST':
        try:
            n1 = int(request.form['n1'])
            n2 = int(request.form['n2'])

            if n1 > len(leetcodetest_easy) or n2 > len(leetcodetest_hard):
                result1, result2 = 'n1 or n2 exceeds list length', None
            else:
                result1 = sorted(random.sample(leetcodetest_easy, n1))
                result2 = sorted(random.sample(leetcodetest_hard, n2))

        except ValueError:
            result1, result2 = 'Invalid input; Please enter integers.', None

    return render_template('index.html', result1=result1, result2=result2)

if __name__ == '__main__':
    app.run(debug=True)
