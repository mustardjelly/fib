"""
Main website handler.
"""
from flask import Flask, render_template, request
from typing import Optional

from src.fibonacci import fibonacci
from src.validators.val_fib import input_is_valid


app: Flask = Flask(__name__)


@app.route('/', methods=['GET'])
def fib_number() -> str:
    """Handle get requests."""
    if request.method == 'GET':
        num: Optional[str] = request.args.get('num')
        if not num:
            return render_template('welcome.html')

        # Validate input
        if not input_is_valid(num):
            return render_template("invalid_input.html")
        
        number: int = int(num)
        try:
            result: int = fibonacci(number)
        except RecursionError:
            return render_template("invalid_input.html")

        return render_template('answer.html', fibnum=result, num=number)
    
    return render_template("invalid_input.html")


if __name__ == '__main__':
    app.run()
