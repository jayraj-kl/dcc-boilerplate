from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_compound_interest(principal, rate, time, compound_frequency):
    """Calculates compound interest.

    Args:
        principal: Initial amount.
        rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
        time: Time in years.
        compound_frequency: Number of times interest is compounded per year.

    Returns:
        A tuple: (final amount, total interest earned)
    """
    rate_per_period = rate / compound_frequency
    total_periods = time * compound_frequency
    amount = principal * (1 + rate_per_period) ** total_periods
    interest = amount - principal
    return amount, interest


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            rate = float(request.form['rate']) / 100  # Convert percentage to decimal
            time = float(request.form['time'])
            compound_frequency = int(request.form['compound_frequency'])

            amount, interest = calculate_compound_interest(principal, rate, time, compound_frequency)
            return render_template('result.html', amount=amount, interest=interest,
                                   principal=principal, rate=rate*100, time=time,
                                   compound_frequency=compound_frequency)

        except ValueError:
            return render_template('index.html', error="Invalid input.  Please enter numbers.")
        except Exception as e: #catch other exceptions
            return render_template('index.html', error=f"An error occurred: {e}")

    return render_template('index.html', error=None)


@app.route('/result') #added to prevent going back to result page with back button.
def result():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)