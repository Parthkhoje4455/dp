from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    mess = ""
    if request.method == "POST":
        nums = list(request.form["nums"])
        amount = int(request.form["amount"])
        market = request.form["market"]

        ank = amount * 16
        dp = int(amount * 0.5)

        ank_str = ""
        dp_str = ""

        for i in nums:
            ank_str += f"{i}={ank}\n"
            dp_str += f"{i}={dp}\n"

        mess = (f"{market}\n"
                f"{ank_str}"
                f"Total {ank * len(nums)}\n\n"
                f"{market}\n"
                f"DP\n"
                f"{dp_str}"
                f"Total {int(len(nums) * amount * 4.5)}")

        # Copy to clipboard
        pyperclip.copy(mess)

    return render_template("index.html", message=mess)

if __name__ == "__main__":
    app.run(debug=True)

