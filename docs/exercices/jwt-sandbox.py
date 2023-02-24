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
    PS> flask run --host=localhost --port=8000 --eager-loading --no-reload --no-debugger --with-threads
"""
import jwt
import io
import base64
from flask import Flask, request, Response, send_file

SECRET = "yolo"
ALGO = "HS256"
MTYPE = "text/plain"
FAVICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADV0lEQVRYhd2W70sTcRzHj6SCetIfEGTuNAj6AUVFBD2K6EnPDIIeVEql32VWaARR04h2kyJqBY5iUv7YffO2SpIyyLayWmVuO39ket8zxXS7uX0XVFDZpwfbzc1WO2tq9IX3g7sH9359ft6XYTJwiuw5e5DAhpHAEtSYuz4T39R89lWvmYsE3UcksBDTwxkFyMdMFhJ0IRWguJFtnlEAhmEYvUO3DQmsB9nZVmTPyZtxgFk5xXb2cLGgOzprAEhgh5CgG5lFgKVLSh3Z2TNm2NA/trGejG2ZLE70/6yu4LqMA2A50oUJhUTxUhhMopJK7v8PgJeoERP6NC2AL+DiRMWQcYAoRHhvOgCjGNgxLeb/HEBD3wBUP+fg4K21UHa/EM56+qcXwGAwzMFy5J4KYHFzcOnRHvUPCGUtRbEsBOzTAsBL9Fhi+i+7UBLAoTubExsRZdTcJkc2YEK/JAJY3FVJAOUt+sRe+Gzs9K/KiLlDDi/iSVievANsfYNgcZ+DktsboaylGIweMrkhe6q8owv/GgATejNqGoYa7x2wdjQALwXSLaKoOoPWvzLnZXpAjbi2+zmYnQVgdhaA1dOoDUBUoEr07/qzyKXQCkzoJxWgvrcHzM59YHYWwHXx4QSAzw+GZ41Q/qAEjjbvgLL7hXDCZYazHb0qxAdTdyB3SuZN72FBqt1f3/sW6t744s83ul9CadNWSLiQxqW3L4dTbbUqRPvF5r752qMn9ComFGz9w3CtvQbqejqAl0KxqENQ29MOlhfnk6YgJYRjBZxpfx2DCF7QZM7LkZ1q01ncVfG6m1374cqTI3DZdSD+Lh0AElg4fHc7cL4RMInKd847uv235rZBqsOERjChYO3AE+a/kBYAJLBwvPW0moUg5x1bnDrtXTAPS/RltOPdYHYWZgwACXlQ6W6JTYXixABZKeoeORet+whceVya1nxqACyU3N4EnHcoth+UimRzObwaEzqOCYUab5Mm86kCIIGFk0+s6lR85bzDyyYaj4Qr46PV1ZbUaJkC0DtWQqW7OXFLliekP6RPmnkpBLb+UU0yegbSyzsAnM8/+eq2Ow5Q/erVXF4KcZjQISzTb1iOjGsRT+i4qTOoXT7lGycq70ydSkU+xlkMwzA/AGJ0YgsiILrEAAAAAElFTkSuQmCC"

app = Flask(__name__)


@app.route("/favicon.ico")
def get_favicon():
    return send_file(io.BytesIO(base64.b64decode(FAVICON_B64)), attachment_filename="favicon.jpeg", mimetype="image/jpg")


@app.route("/", methods=['GET'])
def issue_token():
    encoded = jwt.encode({"UserRole": "BASIC"}, SECRET, algorithm=ALGO)
    content = f"[+] JWT Token:\n{encoded}\n[+] Use POST to validate the token.\n"
    return Response(content, mimetype=MTYPE)


@app.route("/", methods=['POST'])
def validate_token():
    try:
        token = request.headers.get("X-Token")
        verify_signature = ("insecure" not in request.args)
        if token is None or token == "":
            content = f"[+] No token provided into the HTTP request header 'X-Token'.\n"
        else:
            ###
            # ADD VALIDATION VULN HERE
            decoded = jwt.decode(token, SECRET, algorithms=ALGO, options={"verify_signature": verify_signature})
            ###
            content = f"[V] Valid token received:\n{str(decoded)}.\n"
    except Exception as e:
        content = f"[X] Invalid token received:\n{str(e)}.\n"
    content += "[+] Add the query parameter insecure=1 to disable the validation of the signature of the token.\n"
    content += f"[+] Verify signature: {verify_signature}.\n"
    return Response(content, mimetype=MTYPE)
