
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from html import escape

app = FastAPI(title="My First FastAPI Project")


@app.get("/", response_class=HTMLResponse)
def home(name: str = ""):
    greeting = ""

    if name.strip():
        greeting = f"<h2>Hello, {escape(name.strip())}! </h2>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First FastAPI App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .container {{
                background: white;
                padding: 35px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 5px 20px #0002;
                width: 350px;
            }}

            input {{
                padding: 12px;
                width: 90%;
                border: 1px solid #ccc;
                border-radius: 6px;
            }}

            button {{
                margin-top: 15px;
                padding: 12px 25px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }}

            button:hover {{
                background: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>My First FastAPI App </h1>
            <p>Enter your name below.</p>

            <form action="/" method="get">
                <input
                    type="text"
                    name="name"
                    placeholder="Enter your name"
                    required
                >
                <br>
                <button type="submit">Say Hello</button>
            </form>

            {greeting}

            <p>Powered by FastAPI and Python</p>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html)
