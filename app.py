from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

doctors = [
    {
        "id": 1,
        "name": "Dr. Priya Sharma",
        "specialization": "General Physician",
        "experience": "10 Years",
        "fee": "₹500"
    },
    {
        "id": 2,
        "name": "Dr. Arun Kumar",
        "specialization": "Cardiologist",
        "experience": "12 Years",
        "fee": "₹800"
    },
    {
        "id": 3,
        "name": "Dr. Sneha Reddy",
        "specialization": "Dermatologist",
        "experience": "8 Years",
        "fee": "₹600"
    }
]

appointments = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/doctors")
def doctor_list():
    return render_template("doctors.html", doctors=doctors)


@app.route("/appointment/<int:doctor_id>", methods=["GET", "POST"])
def appointment(doctor_id):
    doctor = next((d for d in doctors if d["id"] == doctor_id), None)

    if doctor is None:
        return "Doctor not found", 404

    if request.method == "POST":
        patient_name = request.form["patient_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        date = request.form["date"]
        time = request.form["time"]
        reason = request.form["reason"]

        appointments.append({
            "patient_name": patient_name,
            "phone": phone,
            "email": email,
            "doctor": doctor["name"],
            "specialization": doctor["specialization"],
            "date": date,
            "time": time,
            "reason": reason
        })

        return redirect(url_for("dashboard"))

    return render_template("appointment.html", doctor=doctor)


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        appointments=appointments
    )


if __name__ == "__main__":
    app.run(debug=True)