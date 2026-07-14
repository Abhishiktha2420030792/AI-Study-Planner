from watsonx_service import generate_study_plan
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    # Get data from the form
    name = request.form.get("name")
    subjects = request.form.get("subjects")
    study_hours = request.form.get("study_hours")
    exam_date = request.form.get("exam_date")
    goal = request.form.get("goal")
    difficulty = request.form.get("difficulty")

    # -------------------------------
    # Profile Agent
    # -------------------------------
    profile = (
        f"{name} has exams on {exam_date}. "
        f"The student can study {study_hours} hours per day. "
        f"Goal: {goal}."
    )

    # -------------------------------
    # Subject Priority Agent
    # -------------------------------
    priority = (
        f"Focus more on difficult subjects. "
        f"Subjects entered: {subjects}. "
        f"Difficulty Level: {difficulty}."
    )

    # -------------------------------
    # Planning Agent
    # -------------------------------
    planning = (
        f"Study {study_hours} hours daily. "
        "Divide time equally among all subjects."
    )

    # -------------------------------
    # Revision Agent
    # -------------------------------
    revision = (
        "Revise every Sunday. "
        "Take one mock test every week."
    )

    # -------------------------------
    # Motivation Agent
    # -------------------------------
    motivation = (
        "Stay consistent. "
        "Take short breaks after every study session."
    )

    # -------------------------------
    # Final AI Prompt
    # -------------------------------
    ai_prompt = f"""
You are an AI Study Planner.

Student Name:
{name}

Subjects:
{subjects}

Study Hours:
{study_hours}

Exam Date:
{exam_date}

Academic Goal:
{goal}

Difficulty Level:
{difficulty}

Profile Summary:
{profile}

Subject Priority:
{priority}

Planning:
{planning}

Revision:
{revision}

Motivation:
{motivation}

Generate:

1. Personalized Study Plan

2. Daily Timetable

3. Weekly Timetable

4. Subject Priority

5. Revision Schedule

6. Productivity Tips

7. Motivation
"""

    # Temporary output
    # Later this will come from IBM watsonx.ai
    from watsonx_service import generate_study_plan
    ai_response = generate_study_plan(ai_prompt)

    return render_template(
        "result.html",
        name=name,
        subjects=subjects,
        study_hours=study_hours,
        exam_date=exam_date,
        goal=goal,
        difficulty=difficulty,
        ai_response=ai_response
    )


if __name__ == "__main__":
    app.run(debug=True)