from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return""" <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - RIZSIE</title>
</head>
<body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background-color: #f4f7f6; margin: 0; padding: 20px;">

    <div class="container" style="max-width: 900px; margin: 0 auto; background: #ffffff; padding: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-radius: 8px;">
        
        <header style="text-align: center; border-bottom: 2px solid #2c3e50; padding-bottom: 20px; margin-bottom: 30px;">
            <h1 style="margin: 0; color: #2c3e50; font-size: 3em; text-transform: uppercase; letter-spacing: 2px;">RIZSIE</h1>
            <div style="font-size: 1.5em; color: #3498db; margin-bottom: 10px; font-weight: bold;">Senior Full-Stack Developer & Portfolio</div>
            <div style="font-size: 0.9em; color: #666;">
                email@example.com • (555) 123-4567 • New York, NY<br>
                <a href="#" style="color: #3498db; text-decoration: none; margin: 0 5px;">linkedin.com/in/RIZSIE</a> • 
                <a href="#" style="color: #3498db; text-decoration: none; margin: 0 5px;">github.com/RIZSIE</a>
            </div>
        </header>

        <section style="margin-bottom: 30px;">
            <h2 style="color: #2c3e50; font-size: 1.6em; border-left: 5px solid #3498db; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase;">About Me</h2>
            <p>
                As a results-oriented software engineer with **5+ years of experience**, I specialize in designing and deploying scalable web applications using the **MERN stack** and Python. I've successfully led small development teams and am passionate about tackling complex system architecture challenges to deliver high-performance user experiences.
            </p>
        </section>
        
        <hr style="border: 0; border-top: 1px solid #ddd; margin: 30px 0;">

        <section style="margin-bottom: 30px;">
            <h2 style="color: #2c3e50; font-size: 1.6em; border-left: 5px solid #3498db; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase;">Featured Projects</h2>
            
            <div class="project-entry" style="margin-bottom: 25px; padding: 15px; border: 1px solid #eee; border-radius: 6px;">
                <h3 style="margin: 0; font-size: 1.2em; color: #2c3e50;">E-commerce Platform Redesign</h3>
                <span style="color: #3498db; font-weight: 600; display: block; margin-bottom: 5px; font-size: 0.9em;">React, Node.js, PostgreSQL</span>
                <p style="margin: 5px 0 10px 0;">A full overhaul of the main company website, focusing on a serverless architecture to handle peak load. Managed a 4-person team to implement a new CI/CD pipeline.</p>
                <a href="#" style="color: #3498db; text-decoration: none; font-weight: bold; font-size: 0.9em;">View on GitHub &rarr;</a>
            </div>

            <div class="project-entry" style="margin-bottom: 25px; padding: 15px; border: 1px solid #eee; border-radius: 6px;">
                <h3 style="margin: 0; font-size: 1.2em; color: #2c3e50;">Real-time Data Visualizer</h3>
                <span style="color: #3498db; font-weight: 600; display: block; margin-bottom: 5px; font-size: 0.9em;">Python, Django, WebSockets</span>
                <p style="margin: 5px 0 10px 0;">Developed a dashboard that visualizes streaming financial data, reducing latency by 40% compared to the previous polling-based solution.</p>
                <a href="#" style="color: #3498db; text-decoration: none; font-weight: bold; font-size: 0.9em;">Live Demo &rarr;</a>
            </div>
        </section>
        
        <hr style="border: 0; border-top: 1px solid #ddd; margin: 30px 0;">

        <section style="margin-bottom: 30px;">
            <h2 style="color: #2c3e50; font-size: 1.6em; border-left: 5px solid #3498db; padding-left: 15px; margin-bottom: 20px; text-transform: uppercase;">Technical Skills</h2>
            <div class="skills-grid" style="display: flex; flex-wrap: wrap; gap: 10px;">
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">React.js</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">Node.js (Express)</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">Python (Django/Flask)</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">PostgreSQL & MongoDB</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">AWS (EC2, S3, Lambda)</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">Docker & Kubernetes</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">Git & CI/CD</span>
                <span class="skill-tag" style="background: #eff0f1; color: #2c3e50; padding: 5px 12px; border-radius: 4px; font-size: 0.9em; font-weight: 600;">TypeScript</span>
            </div>
        </section>

    </div>

</body>
</html>"""
@app.route("/about")
def abauta():
    return"""
    <h1> i am home page </h1>
    <h2> i am running flask </h2>
    """
if __name__ == '__main__':
    app.run(debug=True)