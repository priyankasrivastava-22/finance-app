# This file handles all routes (URLs)

from flask import Blueprint, render_template, request, redirect
from app.database import db
from .models import Transaction

# create blueprint
finance = Blueprint('finance', __name__, template_folder='templates')


# -------------------------------
# ROOT ROUTE (VERY IMPORTANT FIX)
# -------------------------------
@finance.route('/')
def home():
    # redirect root URL to finance dashboard
    return redirect('/finance')


# -------------------------------
# DASHBOARD ROUTE
# -------------------------------
@finance.route('/finance')
def dashboard():
    # fetch all transactions
    transactions = Transaction.query.all()

    # initialize totals
    total_income = 0
    total_expense = 0

    # calculate totals
    for t in transactions:
        if t.type == 'income':
            total_income += t.amount
        else:
            total_expense += t.amount

    # calculate balance
    balance = total_income - total_expense

    # send data to HTML
    return render_template(
        'finance_dashboard.html',
        income=total_income,
        expense=total_expense,
        balance=balance,
        transactions=transactions
    )


# -------------------------------
# ADD TRANSACTION
# -------------------------------
@finance.route('/add-transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # get data from form
        type = request.form['type']
        category = request.form['category']
        amount = float(request.form['amount'])

        # create object
        new_transaction = Transaction(
            type=type,
            category=category,
            amount=amount
        )

        # save to DB
        db.session.add(new_transaction)
        db.session.commit()

        # redirect to dashboard
        return redirect('/finance')

    # show form
    return render_template('add_transaction.html')


# -------------------------------
# EDIT TRANSACTION
# -------------------------------
@finance.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_transaction(id):
    transaction = Transaction.query.get(id)

    if request.method == 'POST':
        # update values
        transaction.type = request.form['type']
        transaction.category = request.form['category']
        transaction.amount = float(request.form['amount'])

        db.session.commit()

        return redirect('/finance')

    return render_template('edit_transaction.html', transaction=transaction)


# -------------------------------
# DELETE TRANSACTION
# -------------------------------
@finance.route('/delete/<int:id>')
def delete_transaction(id):
    transaction = Transaction.query.get(id)

    db.session.delete(transaction)
    db.session.commit()

    return redirect('/finance')