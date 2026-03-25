from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        salary_raw = request.form.get("salary", "").strip()
        expenses = request.form.get("expenses", "")

        try:
            salary = float(salary_raw)
        except:
            return render_template("index.html")

        total = 0
        count = 0
        highest = 0

        # split input (comma separated)
        items = expenses.split(",") if expenses else []

        for item in items:
            try:
                expense = float(item)

                if expense < 0:
                    continue

                total += expense
                count += 1

                if expense > highest:
                    highest = expense

            except:
                continue

        # category
        if total >= 200:
            category = "High Expense"
        elif total >= 130:
            category = "Moderate Expense"
        else:
            category = "Low Expense"

        # ratio
        ratio = salary / total if total != 0 else 0

        # savings
        savings = salary - total

        return render_template("result.html",
                               total=total,
                               count=count,
                               highest=highest,
                               category=category,
                               ratio=ratio,
                               savings=savings)

    return render_template("index.html")
