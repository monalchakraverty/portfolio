from flask import Flask, request
import csv

app = Flask(__name__)

# Route for the contact form submission
@app.route('/contact', methods=['POST'])
def contact():
    # Get form data from request
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Open a CSV file for writing
    with open('contact_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the form data as a new row in the CSV file
        writer.writerow([name, email, message])

    # You can optionally send a success response or redirect
    return 'Thank you for your message!'

if __name__ == '__main__':
    app.run(debug=True)