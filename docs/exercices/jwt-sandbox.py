"""
Sandbox to show vuln on JWT token.

Dependencies:
    python -m pip install pyjwt flask

References:
    https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application
    https://pyjwt.readthedocs.io/en/latest/usage.html

Run (PowerShell):
    PS> $env:FLASK_ENV = "production"
    PS> $env:FLASK_APP = "jwt-sandbox"
    PS> flask run --host=0.0.0.0 --port=8000 --eager-loading --no-reload --no-debugger --with-threads
"""
import jwt
import io
import base64
import datetime
from datetime import timezone, timedelta
from flask import Flask, request, Response, send_file

SECRET = "ctie2023"
ALGO = "HS256"
MTYPE = "text/plain"
FAVICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADV0lEQVRYhd2W70sTcRzHj6SCetIfEGTuNAj6AUVFBD2K6EnPDIIeVEql32VWaARR04h2kyJqBY5iUv7YffO2SpIyyLayWmVuO39ket8zxXS7uX0XVFDZpwfbzc1WO2tq9IX3g7sH9359ft6XYTJwiuw5e5DAhpHAEtSYuz4T39R89lWvmYsE3UcksBDTwxkFyMdMFhJ0IRWguJFtnlEAhmEYvUO3DQmsB9nZVmTPyZtxgFk5xXb2cLGgOzprAEhgh5CgG5lFgKVLSh3Z2TNm2NA/trGejG2ZLE70/6yu4LqMA2A50oUJhUTxUhhMopJK7v8PgJeoERP6NC2AL+DiRMWQcYAoRHhvOgCjGNgxLeb/HEBD3wBUP+fg4K21UHa/EM56+qcXwGAwzMFy5J4KYHFzcOnRHvUPCGUtRbEsBOzTAsBL9Fhi+i+7UBLAoTubExsRZdTcJkc2YEK/JAJY3FVJAOUt+sRe+Gzs9K/KiLlDDi/iSVievANsfYNgcZ+DktsboaylGIweMrkhe6q8owv/GgATejNqGoYa7x2wdjQALwXSLaKoOoPWvzLnZXpAjbi2+zmYnQVgdhaA1dOoDUBUoEr07/qzyKXQCkzoJxWgvrcHzM59YHYWwHXx4QSAzw+GZ41Q/qAEjjbvgLL7hXDCZYazHb0qxAdTdyB3SuZN72FBqt1f3/sW6t744s83ul9CadNWSLiQxqW3L4dTbbUqRPvF5r752qMn9ComFGz9w3CtvQbqejqAl0KxqENQ29MOlhfnk6YgJYRjBZxpfx2DCF7QZM7LkZ1q01ncVfG6m1374cqTI3DZdSD+Lh0AElg4fHc7cL4RMInKd847uv235rZBqsOERjChYO3AE+a/kBYAJLBwvPW0moUg5x1bnDrtXTAPS/RltOPdYHYWZgwACXlQ6W6JTYXixABZKeoeORet+whceVya1nxqACyU3N4EnHcoth+UimRzObwaEzqOCYUab5Mm86kCIIGFk0+s6lR85bzDyyYaj4Qr46PV1ZbUaJkC0DtWQqW7OXFLliekP6RPmnkpBLb+UU0yegbSyzsAnM8/+eq2Ow5Q/erVXF4KcZjQISzTb1iOjGsRT+i4qTOoXT7lGycq70ydSkU+xlkMwzA/AGJ0YgsiILrEAAAAAElFTkSuQmCC"

app = Flask(__name__)


@app.route("/favicon.ico")
def get_favicon():
    return send_file(io.BytesIO(base64.b64decode(FAVICON_B64)), attachment_filename="favicon.jpeg", mimetype="image/jpg")


@app.route("/", methods=['GET'])
def issue_token():
    claims = {"exp": datetime.datetime.now(tz=timezone.utc) + timedelta(seconds=600), "UserRole": "BASIC"}
    encoded = jwt.encode(claims, SECRET, algorithm=ALGO)
    content = f"[+] JWT Token:\n{encoded}\n"
    content += f"[+] Use POST to validate the token: Add the header 'X-VerifySig' to enable the verification of the signature.\n"
    return Response(content, mimetype=MTYPE)


@app.route("/", methods=['POST'])
def validate_token():
    try:
        token = request.headers.get("X-Token")
        if token is None or token == "":
            content = f"[+] No token provided into the HTTP request header 'X-Token'.\n"
        else:
            ###
            # Add bug validation
            #verify_enabled = False
            decoded = jwt.decode(token, SECRET, algorithms=ALGO)
            #decoded = jwt.decode(token, SECRET, algorithms=ALGO, options={"verify_signature": (request.headers.get("X-VerifySig") is not None), "verify_exp": verify_enabled, "verify_aud": verify_enabled})
            ###
            content = f"SUCCESS: Valid token received:\n{str(decoded)}.\n"
    except Exception as e:
        content = f"FAILURE: Invalid token received:\n{str(e)}.\n"
    return Response(content, mimetype=MTYPE)
