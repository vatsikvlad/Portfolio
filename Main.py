from flask import Flask, render_template, request
from project import Project
from contact import Contact
from tech_stack import TechStack
from education import Education

app: Flask = Flask(__name__)

projects: list[Project] = [
    Project("Your Plan Application", "A modern Android mobile application for time management, event planning, and daily task organization. ", "https://github.com/vatsikvlad/YourPlanApplication", None),
    Project("List Details", "A modern Android application for hiking and cycling enthusiasts to discover, track, and record their outdoor adventures.", "https://github.com/vatsikvlad/ListDetails", None),
    Project("Weather Website", "A weather application built with a SOLID-compliant architecture.", "https://github.com/vatsikvlad/Weather_website", None),
    Project("Euler's Interpolation", "A mathematical project implementing Hermite interpolation in a desktop application.", "https://github.com/vatsikvlad/EulersInterpolation", None),
    Project("Remote Shutdown System", "An application that allows remote computer shutdown within a local area network.", "https://github.com/vatsikvlad/RemoteShutdownSystem", None),
    Project("Tabu Search", "Project description", "https://github.com/vatsikvlad/TabuSearch_OK", None)
]

contacts: list[Contact] = [
    Contact("GitHub", "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons/github.svg", "https://github.com/vatsikvlad"),
    Contact("LinkedIn", "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons/linkedin.svg", "https://www.linkedin.com/in/vladyslav-vatslavyi-3b53b528a/"),
    Contact("Telegram", "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons/telegram.svg", "https://t.me/vatsikvlad"),
    Contact("Email", "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons/envelope.svg", "mailto:vatsikvlad@gmail.com")
]

tech_stacks: list[TechStack] = [
    TechStack("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain.svg"),
    TechStack("C++", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-plain.svg"),
    TechStack("C", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg"),
    TechStack("C#", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-plain.svg"),
    TechStack("Java", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-plain.svg"),
    TechStack("HTML", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-plain.svg"),
    TechStack("CSS", "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-plain.svg"),
    TechStack("SQL", "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/icons/database.svg")
]

education: list[Education] = [
    Education("Vinncia Liceum No. 2", "Completed high school education with a focus on science and mathematics, developing a strong foundation in analytical thinking and problem-solving skills."),
    Education("Technical School", "Studied programming and computer science fundamentals, gaining practical experience in software development and problem-solving."),
    Education("Poznan University of Technology", "Pursued a degree in Computer Science, focusing on advanced programming concepts, algorithms, and software engineering principles.")
]

@app.route("/", methods=['GET'])
def Index() -> str:
    return render_template('home.html', projects=projects, contacts=contacts, tech_stacks=tech_stacks, education=education)

@app.errorhandler(404)
def NotFound(e: Exception) -> tuple[str, int]:
    return render_template("notFound.html"), 404

@app.route(f"/<project_name>")
def ProjectPage(project_name: str) -> tuple[str, int] | str:
    project: Project | None = next((p for p in projects if p.title.replace(" ", "").replace("\'", "") == project_name), None)
    if not project:
        return NotFound(Exception("Project not found"))
    return render_template('project.html', project=project)

if __name__ == "__main__":
    app.run()
